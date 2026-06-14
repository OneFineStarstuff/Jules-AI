# Kafka ACL Provisioning for G-SIFI Telemetry
# Enforces granular, role-based access control for Agent identities.

resource "aws_msk_cluster_policy" "sentinel_acls" {
  cluster_arn = aws_msk_cluster.sentinel_telemetry.arn
  policy      = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          AWS = "arn:aws:iam::${var.account_id}:role/SentinelSidecarRole"
        }
        Action = [
          "kafka-cluster:Connect",
          "kafka-cluster:WriteData"
        ]
        Resource = "arn:aws:kafka:us-east-1:${var.account_id}:topic/sentinel.telemetry.worm"
      },
      {
        Effect = "Allow"
        Principal = {
          AWS = "arn:aws:iam::${var.account_id}:role/AuditorWORMVerifier"
        }
        Action = [
          "kafka-cluster:ReadData"
        ]
        Resource = "arn:aws:kafka:us-east-1:${var.account_id}:topic/sentinel.telemetry.worm"
      }
    ]
  })
}

variable "account_id" {
  type = string
}
