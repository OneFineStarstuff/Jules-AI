# Sovereign API Gateway & EAIP Specification
**Layer:** Edge Enforcement

## 1. Zero-Trust RAG
All Retrieval-Augmented Generation (RAG) requests are intercepted by the Gateway.
- **Redaction:** PII scrubbing using `hash_pii()` utility.
- **Authorization:** zk-SNARK token verification.

## 2. Policy Injection
Direct injection of GDL (Governance Description Language) logic gates into the inference sidecar.
