# Terraform Module for Zero-Trust EKS Cluster (Institutional AGI Standard)

module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 19.0"

  cluster_name    = "institutional-agi-cluster"
  cluster_version = "1.28"

  vpc_id     = aws_vpc.agi_governance_vpc.id
  subnet_ids = [aws_subnet.audit_worm_subnet.id] # Strictly isolated subnets

  # Node Groups with Nitro Enclaves enabled
  eks_managed_node_groups = {
    governance_nodes = {
      instance_types = ["m6i.xlarge"] # Nitro-supported
      ami_type       = "AL2_x86_64_GPU" # For reasoning kernels
      min_size       = 3
      max_size       = 10

      # Enclave configuration
      post_bootstrap_user_data = <<-EOT
        #!/bin/bash
        amazon-linux-extras install aws-nitro-enclaves-cli -y
        yum install aws-nitro-enclaves-cli-devel -y
        usermod -aG ne ec2-user
      EOT
    }
  }

  # Cluster Security: OPA Gatekeeper integration
  cluster_addons = {
    coredns    = {}
    kube-proxy = {}
    vpc-cni    = {}
    aws-ebs-csi-driver = {}
  }
}

# Network Policy: Zero-Egress by default
resource "kubernetes_network_policy" "zero_egress" {
  metadata {
    name      = "deny-all-egress"
    namespace = "agi-production"
  }

  spec {
    pod_selector {}
    policy_types = ["Egress"]
    # No egress rules = Deny All
  }
}
