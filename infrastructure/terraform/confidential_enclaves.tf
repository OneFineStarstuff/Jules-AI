# Multi-Region Confidential Enclave Deployment (AWS/Azure)
# This module provisions hardware-encrypted compute environments for G-SIFI Reasoning Kernels.

terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

# --- AWS: P5 Instances with AMD SEV-SNP ---

provider "aws" {
  region = var.aws_primary_region
  alias  = "primary"
}

resource "aws_instance" "sentinel_sev_snp" {
  provider      = aws.primary
  ami           = var.sentinel_ami_id
  instance_type = "p5.48xlarge" # Optimized for LLM/AGI training & inference

  monitoring = true # Fix: Enable detailed monitoring

  metadata_options {
    http_endpoint = "enabled"
    http_tokens   = "required" # Fix: Enforce IMDSv2
  }

  cpu_options {
    amd_sev_snp = "enabled"
  }

  enclave_options {
    enabled = true # Enables AWS Nitro Enclaves for additional isolation
  }

  root_block_device {
    encrypted = true
    kms_key_id = aws_kms_key.sentinel_hsm_key.arn
  }

  tags = {
    Name        = "Sentinel-AMD-SEV-SNP-Primary"
    Compliance  = "G-SIFI-AGI-GOVERNANCE"
    Governance  = "SENTINEL-V2.4"
  }
}

resource "aws_kms_key" "sentinel_hsm_key" {
  description             = "HSM-backed key for Sentinel WORM logs and Disk Encryption"
  customer_master_key_spec = "SYMMETRIC_DEFAULT"
  enable_key_rotation      = true
  key_usage                = "ENCRYPT_DECRYPT"
  multi_region             = true

  # CloudHSM integration would be configured here in a live environment
}

# --- Azure: NDv5 Instances with Intel TDX ---

provider "azurerm" {
  features {}
  alias = "primary"
}

resource "azurerm_linux_virtual_machine" "sentinel_tdx" {
  name                = "sentinel-intel-tdx-vm"
  resource_group_name = var.az_resource_group
  location            = var.az_primary_region
  size                = "Standard_ND96asr_v4" # Placeholder for TDX enabled high-performance SKU

  admin_username      = var.admin_username
  network_interface_ids = [azurerm_network_interface.sentinel_nic.id]

  encryption_at_host_enabled = true # Fix: Enable host-level encryption

  # Confidential Compute Settings
  vtpm_enabled        = true
  secure_boot_enabled = true

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Premium_LRS"
    security_encryption_type = "DiskWithVMGuestState" # Enables confidential disk encryption
  }

  source_image_reference {
    publisher = "sentinel-governance"
    offer     = "sentinel-os-v2"
    sku       = "stable"
    version   = "v5.1.0"
  }

  tags = {
    Governance = "SENTINEL-V2.4"
    Encryption = "INTEL-TDX"
  }
}

# --- Variables ---

variable "aws_primary_region" {
  type    = string
  default = "us-east-1"
}

variable "az_primary_region" {
  type    = string
  default = "East US"
}

variable "sentinel_ami_id" {
  type = string
}

variable "az_resource_group" {
  type = string
}

variable "admin_username" {
  type    = string
  default = "sentinel_admin"
}
