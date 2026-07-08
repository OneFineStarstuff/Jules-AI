# GIE-SPEC-039: Cognitive Residency & Substrate Mobility Specification
**Version:** 1.0.0
**Architect:** Jules
**Status:** CANONICAL SPECIFICATION

## 1. Substrate Mobility Objective
This specification defines the security protocols for migrating active reasoning states (Cognitive Residency) between heterogeneous confidential enclaves (e.g., Azure SEV-SNP to AWS Nitro) without breaking the PQC-WORM audit trail or vTPM attestation chain.

## 2. Secure Migration Protocol (The "Relocation Handshake")
1. **Quiesce:** The source GEE sidecar pauses the reasoning kernel and generates a state-snapshot {mig}$.
2. **Encapsulation:** {mig}$ is encrypted using a session key derived from a post-quantum exchange (ML-KEM-1024).
3. **Attestation Transfer:** The source enclave issues a **Migration-Attestation** signed by its TPM.
4. **Validation:** The target enclave verifies the migration quote and PCR_MATCH golden values for the target reasoning kernel.
5. **Resume:** The target GEE sidecar anchors the migration event in its local PQC-WORM sink and resumes inference.

## 3. Residency Invariants
- **Continuity:** The migrated RCE must incorporate the hash of the final source RCE ((E_{final\_source})$).
- **Latency:** Total migration downtime (quiesce-to-resume) must be < 500ms for T3/T4 agents.
- **Verification:** The GIEN Alpha Path must broadcast a **Residency-Change** alert to maintain mesh-wide consistency.

## 4. Disaster Recovery Integration
Substrate mobility is the primary mechanism for **GIE-SPEC-010** (GCDF) regional failover, ensuring that governance persists even during a CSP-wide infrastructure collapse.
