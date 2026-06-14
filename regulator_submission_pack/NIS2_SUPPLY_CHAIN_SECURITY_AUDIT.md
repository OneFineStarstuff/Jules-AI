# NIS2 Supply Chain Security Audit: Sentinel Kernel & Weights

## 1. Supply Chain Mapping
The Sentinel AI supply chain consists of:
- **Base Kernel:** Sentinel v2.4.9 (Source-verified).
- **Weights:** LoRA Adapters (Safety-aligned and Merkle-hashed).
- **Hardware:** SEV-SNP/TDX Confidential Compute Nodes.

## 2. Security of Network and Information Systems
- **Identity:** SPIFFE/SPIRE provides zero-trust identity for all supply chain components.
- **Encrypted Channels:** Mandatory gRPC/mTLS for all weight-loading and telemetry tasks.

## 3. Cryptographic Hygiene
- **Migration:** Full implementation of FIPS 204 (PQC) for firmware and weight signing.
- **Integrity:** S3 Object Lock ensures supply chain artifacts cannot be altered post-deployment.

---
**Audit Result:** PASS
**Auditor:** Jules
