# Terraform configuration for G-SIFI Confidential Enclaves (AMD SEV-SNP / Intel TDX)
# AWS Provider (Placeholder for G-SIFI multi-region deployment)

provider "aws" {
  region = var.region
}

variable "region" {
  description = "The AWS region for enclave deployment"
  default     = "us-east-1"
}

variable "vpc_id" {
  description = "The VPC ID"
}

variable "ami_id" {
  description = "The AMI ID"
}

variable "kms_key_arn" {
  description = "The KMS Key ARN"
}

# Inviolable Audit Subnet
resource "aws_subnet" "audit_subnet" {
  vpc_id            = var.vpc_id
  cidr_block        = "10.0.100.0/24"
  availability_zone = "${var.region}a"

  tags = {
    Name        = "Sentinel-Inviolable-Audit-Subnet"
    Governance  = "SENTINEL-V2.4"
    Compliance  = "EU-AI-ACT-ANNEX-IV"
  }
}

# Network Interface for the reasoning kernel
resource "aws_network_interface" "kernel_nic" {
  subnet_id = aws_subnet.audit_subnet.id
}

# Confidential Compute Instance (AMD SEV-SNP enabled)
resource "aws_instance" "confidential_reasoning_kernel" {
  ami           = var.ami_id
  instance_type = "r7a.xlarge" # AMD EPYC based instance with SEV-SNP support

  cpu_options {
    amd_sev_snp = "enabled"
  }

  network_interface {
    network_interface_id = aws_network_interface.kernel_nic.id
    device_index         = 0
  }

  ebs_optimized = true
  monitoring    = true

  metadata_options {
    http_endpoint               = "enabled"
    http_tokens                 = "required" # IMDSv2 mandatory
    http_put_response_hop_limit = 1
    instance_metadata_tags      = "enabled"
  }

  root_block_device {
    encrypted = true
    kms_key_id = var.kms_key_arn
  }

  tags = {
    Name = "Omni-Sentinel-Reasoning-Kernel"
    Security = "TPM-PCR-MATCH-TRUE"
  }
}

# Kafka WORM Archive (S3 with Object Lock)
resource "aws_s3_bucket" "worm_audit_sink" {
  bucket = "gsifi-pqc-worm-audit-ledger"

  object_lock_enabled = true

  tags = {
    StorageMode = "WORM"
    PQC_Algorithm = "ML-DSA-87"
  }
}

# Enforce encryption and public access blocking for S3 WORM sink
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

resource "aws_s3_bucket_object_lock_configuration" "worm_policy" {
  bucket = aws_s3_bucket.worm_audit_sink.id

  rule {
    default_retention {
      mode = "COMPLIANCE"
      years = 10
    }
  }
}
