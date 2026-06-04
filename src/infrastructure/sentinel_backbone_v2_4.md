# Sentinel AI v2.4 Backbone Infrastructure
**Standard:** ISO 42001 / NIST AI RMF

## 1. Zero-Trust Mesh
Rust-based proxies (Envoy/Istio) with SPIRE-Global identity.
- **Logging:** ML-DSA signed WORM audit trails.
- **Compute:** AWS Nitro Enclaves with TPM 2.0 attestation.

## 2. Homeostatic Control
Real-time feedback loop between the CEE (Cognitive Execution Environment) and the SACC.
