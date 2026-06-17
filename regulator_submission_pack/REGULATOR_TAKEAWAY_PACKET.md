# Regulator Takeaway Packet: Supervisory Control Plane

## 1. Lifecycle Architecture Map
- **Stage 1 (Ingress):** SPIFFE-attested inference events.
- **Stage 2 (Enforcement):** GDL/Rego sidecars.
- **Stage 3 (Evidence):** ZK-Prover & Evidence Binder.
- **Stage 4 (Persistence):** PQC-WORM (ML-DSA-87) in S3.
- **Stage 5 (Verification):** GIEN Mesh & Regulator Verifier Nodes.

## 2. Regulator Orientation Guide
- **How to verify a proof:** Use the `sentinel-verify` binary against public STHs.
- **How to read the audit log:** Access the read-only S3 bucket; check for ML-DSA signatures.
- **Understanding GSM States:** Reference the state-transition diagram in Section 4.

## 3. Frequently Asked Questions (FAQ)
- **Q: Can the regulator see the raw model weights?**
    - A: No. The SCP uses ZK-proofs to prove compliance *without* exposing model intellectual property or raw weights.
- **Q: How is data privacy handled?**
    - A: Salted SHA-256 hashing at the edge (Zero-PII policy) and hardware-encrypted TEE memory isolation.
- **Q: What happens if the IRMI kill-switch is triggered?**
    - A: GPU power is severed at the hardware level within < 1ms, halting all inference.

---
**Access Link:** [Digital Evidence Vault - G-SIFI-2028-Pilot]
