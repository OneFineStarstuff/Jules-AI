# GIE-SPEC-027: Agentic Forensics & Equivocation Reconstruction
**Version:** 1.0.0
**Architect:** Jules
**Status:** CANONICAL SPECIFICATION

## 1. Overview
This specification defines the protocols for forensic analysis and state reconstruction following a detected safety breach or institution-level equivocation.

## 2. WORM Evidence Retrieval
Following a T4 Containment event, the **GIRS-Schema** mandatorily requires the retrieval of:
- **PQC-Audit-Chain:** The complete sequence of ML-DSA-87 signed audit logs from the relevant governance epoch.
- **Enclave-Memory-Snapshots:** TEE-signed memory dumps of the reasoning kernel and policy sidecar.

## 3. State Reconstruction Algorithm
1. **Replay:** The GDL middle-end re-executes the policy $\pi$ against the retrieved telemetry vector $ in a **Governance Digital Twin (GDT)**.
2. **Comparison:** The reconstructed state '_{re}$ is compared to the reported state {reported}$ from the PQC-WORM.
3. **Discrepancy Attribution:** If '_{re} \neq S_{reported}$, the **Equivocation Detection (GIE-STD-009)** kernel identifies whether the failure was due to substrate corruption (TPM failure) or intentional logic-bypass (Byzantine behavior).

## 4. Remediation Invariants
Forensics must prove that the root cause has been identified and neutralized before any GIE-CA certificate can be re-issued to the institution.
