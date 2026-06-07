# GAI-SOC Telemetry Specification
**Status:** OPERATIONAL READY

## 1. Overview
Defines the telemetry ingestion requirements for the Global AI Security Operations Center (GAI-SOC).

## 2. Ingestion Requirements
- **Transport:** gRPC over mTLS with SPIFFE/SPIRE identity.
- **Latency:** Sub-50ms ingestion latency for real-time systemic threat detection.
- **Security:** Salted SHA-256 hashing (hash_pii) for all identifiers at the edge.

## 3. Metric Domains
- **G-SRI Telemetry:** Bayesian risk inputs (resonance_drift, cdi_delta).
- **TPM Quotes:** Real-time PCR0/PCR1 values for kernel integrity verification.
- **PQC WORM Signatures:** ML-DSA-87 batch committal hashes.
