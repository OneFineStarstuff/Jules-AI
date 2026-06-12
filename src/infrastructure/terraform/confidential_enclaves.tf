# Terraform configuration for G-SIFI Confidential Enclaves (AMD SEV-SNP / Intel TDX)
# AWS Provider (Placeholder for G-SIFI multi-region deployment)

provider "aws" {
  region = var.region
}

variable "region" {
  description = "The AWS region for enclave deployment"
  default     = "us-east-1"
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

resource "aws_s3_bucket_object_lock_configuration" "worm_policy" {
  bucket = aws_s3_bucket.worm_audit_sink.id

  rule {
    default_retention {
      mode = "COMPLIANCE"
      years = 10
    }
  }
}
