# Annex C: Resilience, Privacy, & Zero-Trust Architecture
**Regulatory Alignment:** DORA, NIS2, GDPR Art. 22, Zero-Trust (NIST 800-207)

## 1. Zero-Trust Deployment
- **Kubernetes Isolation:** eBPF-based network policies (Cilium).
- **Identity:** SPIFFE SVIDs for all services.
- **GitOps:** Continuous reconciliation via ArgoCD with PQC-signed commits.

## 2. Privacy & Explainability
- **GDPR Art. 22:** Causal Inference Explainers (src/governance_engine/explainers.py) provide justification for every automated decision.
- **PQC Encryption:** AES-256-GCM with Kyber-1024 key exchange for inter-enclave data.
