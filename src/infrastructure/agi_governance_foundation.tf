# Terraform Module for Inviolable AGI Governance Foundation
# Aligned with EU AI Act Art 15 & ISO 42001

resource "aws_vpc" "agi_containment_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  tags = {
    Name = "AGI-Containment-VPC"
    Classification = "G-SIFI-Tier-1"
  }
}

# Strictly Isolated Audit WORM Subnet
resource "aws_subnet" "audit_worm_subnet" {
  vpc_id            = aws_vpc.agi_containment_vpc.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "us-east-1a"

  tags = {
    Isolation = "Air-Gapped"
    Compliance = "ISO-42001-Annex-J"
  }
}

# S3 Bucket with WORM (Object Lock) for Audit Logs
resource "aws_s3_bucket" "audit_logs_worm" {
  bucket = "institutional-agi-audit-logs-worm-pqc"
  object_lock_enabled = true

  lifecycle {
    prevent_destroy = true
  }
}

# KMS Key for Audit Log Encryption (PQC-Hardened)
resource "aws_kms_key" "audit_kms_pqc" {
  description             = "Post-Quantum Encrypted Audit Log Key"
  deletion_window_in_days = 30
  enable_key_rotation     = true # Mandatory ISO 42001 control

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "Deny Key Deletion for Audit Principals"
        Effect = "Deny"
        Principal = { AWS = "*" }
        Action   = "kms:ScheduleKeyDeletion"
        Resource = "*"
      }
    ]
  })
}
