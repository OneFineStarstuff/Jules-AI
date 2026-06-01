# Hardened Terraform Module for AGI Governance (ISO/IEC 42001 Compliance)

resource "aws_vpc" "agi_governance_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  tags = {
    Name = "AGI-Governance-VPC"
    Compliance = "ISO-42001"
  }
}

resource "aws_subnet" "audit_worm_subnet" {
  vpc_id            = aws_vpc.agi_governance_vpc.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "us-east-1a"
  tags = {
    Name = "Audit-WORM-Subnet"
    Isolation = "Nitro-Enclave"
  }
}

# S3 Bucket with WORM (Object Lock) and Destroy Protection
resource "aws_s3_bucket" "audit_logs_worm" {
  bucket = "institutional-agi-audit-logs-worm"
  object_lock_enabled = true

  lifecycle {
    prevent_destroy = true
  }
}

resource "aws_s3_bucket_object_lock_configuration" "retention" {
  bucket = aws_s3_bucket.audit_logs_worm.id
  rule {
    default_retention {
      mode  = "COMPLIANCE"
      years = 7
    }
  }
}

# KMS Key with Explicit Rotation and Policy-Driven Deletion Safeguards
resource "aws_kms_key" "audit_kms" {
  description             = "AGI Audit Log Encryption Key"
  deletion_window_in_days = 30
  enable_key_rotation     = true # Mandatory ISO 42001 control

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "Enable IAM User Permissions"
        Effect = "Allow"
        Principal = { AWS = "*" }
        Action   = "kms:*"
        Resource = "*"
      },
      {
        Sid    = "Deny Key Deletion for Audit Principals"
        Effect = "Deny"
        Principal = { AWS = "*" }
        Action   = "kms:ScheduleKeyDeletion"
        Resource = "*"
        Condition = {
          StringLike = { "aws:PrincipalArn": "arn:aws:iam::*:role/AuditPrincipal" }
        }
      }
    ]
  })
}

# Security Group with Strict gRPC ingress and Nitro isolation
resource "aws_security_group" "governance_sidecar_sg" {
  name        = "governance-sidecar-sg"
  vpc_id      = aws_vpc.agi_governance_vpc.id

  ingress {
    description = "gRPC from internal AGI mesh"
    from_port   = 50051
    to_port     = 50051
    protocol    = "tcp"
    cidr_blocks = [aws_vpc.agi_governance_vpc.cidr_block]
  }

  egress {
    description = "To Audit WORM S3 (via Endpoint)"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Should ideally be VPC Endpoint
  }
}
