# Terraform configuration for G-SIFI Confidential Enclaves (AMD SEV-SNP / Intel TDX)
# AWS Provider (Placeholder for G-SIFI multi-region deployment)

provider "aws" {
  region = var.region
}

variable "region" {
  description = "The AWS region for enclave deployment"
  type        = string
  default     = "us-east-1"
}

variable "vpc_id" {
  description = "The VPC ID"
  type        = string
}

variable "ami_id" {
  description = "The AMI ID"
  type        = string
}

variable "kms_key_arn" {
  description = "The KMS Key ARN"
  type        = string
}

variable "allowed_telemetry_cidr" {
  description = "CIDR block for authorized telemetry endpoints"
  type        = string
  default     = "10.0.0.0/8"
}

# Inviolable Audit Subnet
resource "aws_subnet" "audit_subnet" {
  vpc_id                  = var.vpc_id
  cidr_block              = "10.0.100.0/24"
  availability_zone       = "${var.region}a"
  map_public_ip_on_launch = false

  tags = {
    Name        = "Sentinel-Inviolable-Audit-Subnet"
    Governance  = "SENTINEL-V2.4"
    Compliance  = "EU-AI-ACT-ANNEX-IV"
  }
}

# Security Group for the reasoning kernel
resource "aws_security_group" "kernel_sg" {
  name        = "sentinel-kernel-sg"
  description = "Restrictive security group for Sentinel reasoning kernel"
  vpc_id      = var.vpc_id

  # Egress restricted to internal HTTPS telemetry
  egress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = [var.allowed_telemetry_cidr]
    description = "Allow HTTPS egress to internal telemetry"
  }

  tags = {
    Name = "Sentinel-Kernel-Security-Group"
  }
}

# Network Interface for the reasoning kernel
resource "aws_network_interface" "kernel_nic" {
  subnet_id       = aws_subnet.audit_subnet.id
  security_groups = [aws_security_group.kernel_sg.id]
}

# Confidential Compute Instance (AMD SEV-SNP enabled)
resource "aws_instance" "confidential_reasoning_kernel" {
  ami           = var.ami_id
  instance_type = "r7a.xlarge"

  cpu_options {
    amd_sev_snp = "enabled"
  }

  network_interface {
    network_interface_id = aws_network_interface.kernel_nic.id
    device_index         = 0
  }

  ebs_optimized               = true
  monitoring                  = true
  associate_public_ip_address = false

  metadata_options {
    http_endpoint               = "enabled"
    http_tokens                 = "required"
    http_put_response_hop_limit = 1
    instance_metadata_tags      = "enabled"
  }

  root_block_device {
    encrypted             = true
    kms_key_id            = var.kms_key_arn
    delete_on_termination = true
  }

  tags = {
    Name = "Omni-Sentinel-Reasoning-Kernel"
    Security = "TPM-PCR-MATCH-TRUE"
  }
}

# -----------------------------------------------------------------------------
# S3 BUCKET HARDENING
# -----------------------------------------------------------------------------

# Access logging bucket
resource "aws_s3_bucket" "log_bucket" {
  bucket = "gsifi-audit-logs-access"
}

resource "aws_s3_bucket_ownership_controls" "log_bucket_ownership" {
  bucket = aws_s3_bucket.log_bucket.id
  rule {
    object_ownership = "BucketOwnerEnforced"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "log_encryption" {
  bucket = aws_s3_bucket.log_bucket.id
  rule {
    apply_server_side_encryption_by_default {
      kms_master_key_id = var.kms_key_arn
      sse_algorithm     = "aws:kms"
    }
  }
}

resource "aws_s3_bucket_public_access_block" "log_public_access_block" {
  bucket = aws_s3_bucket.log_bucket.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_versioning" "log_versioning" {
  bucket = aws_s3_bucket.log_bucket.id
  versioning_configuration {
    status = "Enabled"
  }
}

# Kafka WORM Archive (S3 with Object Lock)
resource "aws_s3_bucket" "worm_audit_sink" {
  bucket = "gsifi-pqc-worm-audit-ledger"
  object_lock_enabled = true
}

resource "aws_s3_bucket_ownership_controls" "worm_bucket_ownership" {
  bucket = aws_s3_bucket.worm_audit_sink.id
  rule {
    object_ownership = "BucketOwnerEnforced"
  }
}

resource "aws_s3_bucket_versioning" "worm_versioning" {
  bucket = aws_s3_bucket.worm_audit_sink.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "worm_encryption" {
  bucket = aws_s3_bucket.worm_audit_sink.id
  rule {
    apply_server_side_encryption_by_default {
      kms_master_key_id = var.kms_key_arn
      sse_algorithm     = "aws:kms"
    }
  }
}

resource "aws_s3_bucket_public_access_block" "worm_public_access_block" {
  bucket = aws_s3_bucket.worm_audit_sink.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_logging" "worm_logging" {
  bucket = aws_s3_bucket.worm_audit_sink.id
  target_bucket = aws_s3_bucket.log_bucket.id
  target_prefix = "log/"
}

resource "aws_s3_bucket_object_lock_configuration" "worm_policy" {
  bucket = aws_s3_bucket.worm_audit_sink.id
  rule {
    default_retention {
      mode = "COMPLIANCE"
      years = 10
    }
  }
}

# -----------------------------------------------------------------------------
# BUCKET POLICIES (SSL & LOGGING)
# -----------------------------------------------------------------------------

resource "aws_s3_bucket_policy" "worm_ssl_only" {
  bucket = aws_s3_bucket.worm_audit_sink.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid       = "AllowSSLRequestsOnly"
        Action    = "s3:*"
        Effect    = "Deny"
        Principal = "*"
        Resource = [
          aws_s3_bucket.worm_audit_sink.arn,
          "${aws_s3_bucket.worm_audit_sink.arn}/*",
        ]
        Condition = {
          Bool = {
            "aws:SecureTransport" = "false"
          }
        }
      }
    ]
  })
}

resource "aws_s3_bucket_policy" "log_bucket_policy" {
  bucket = aws_s3_bucket.log_bucket.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid       = "AllowSSLRequestsOnly"
        Action    = "s3:*"
        Effect    = "Deny"
        Principal = "*"
        Resource = [
          aws_s3_bucket.log_bucket.arn,
          "${aws_s3_bucket.log_bucket.arn}/*",
        ]
        Condition = {
          Bool = {
            "aws:SecureTransport" = "false"
          }
        }
      },
      {
        Sid = "S3ServerAccessLogsPolicy"
        Effect = "Allow"
        Principal = {
          Service = "logging.s3.amazonaws.com"
        }
        Action = "s3:PutObject"
        Resource = "${aws_s3_bucket.log_bucket.arn}/*"
        Condition = {
          StringEquals = {
            "aws:SourceAccount" = data.aws_caller_identity.current.account_id
          }
        }
      }
    ]
  })
}

data "aws_caller_identity" "current" {}
