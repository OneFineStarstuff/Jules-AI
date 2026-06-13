# HSM & KMS Hardening for Sentinel Governance

## 1. AWS KMS Configuration
- **Key Policy:** Strict least-privilege policies restricted to the `SentinelSidecarRole`.
- **Rotation:** `enable_key_rotation = true` (Mandatory).
- **Multi-Region:** Primary in `us-east-1`, Replica in `eu-west-1`.

## 2. Azure Key Vault & HSM
- **Managed HSM:** FIPS 140-2 Level 3 protection for PQC signing keys.
- **RBAC:** `Key Vault Crypto Officer` role assigned only to the Sovereign CAIGO identity.

## 3. PQC Implementation (FIPS 204)
The Sentinel stack utilizes the following algorithms for hardware-anchored audit trails:
- **ML-DSA-87 (Dilithium):** Primary signing algorithm.
- **SPHINCS+:** Used for long-term historical anchoring of the Master Canon.

---
**Status:** HARDENING GUIDE v1.1.0
