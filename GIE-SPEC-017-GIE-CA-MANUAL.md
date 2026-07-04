# GIE-SPEC-017: GIE Certification Authority (GIE-CA) Operational Manual
**Version:** 1.0.0
**Architect:** Jules
**Status:** CANONICAL SPECIFICATION

## 1. Overview
The **GIE Certification Authority (GIE-CA)** is the decentralized entity responsible for issuing ZK-attested compliance certificates to G-SIFIs.

## 2. Certification Lifecycle
1. **Application:** Institution submits its **GIMM-L1/L2** baseline telemetry.
2. **Audit:** Specialized **Auditor-Agents** (AGA) perform continuous non-destructive probing for 90 days.
3. **Verification:** The **ZKAF** pipeline verifies the institutional state-root and PQC-WORM continuity.
4. **Issuance:** GIE-CA issues a **ZK-Certificate** signed with the Global-GACMO key.

## 3. Auditor-Agent Roles
- **Prober:** Executes GKQL queries against the GKG to detect hidden goal-divergence.
- **Validator:** Verifies the integrity of SnarkPack proof aggregations.
- **Sentinel:** Monitors the GIEN mesh for evidence of Byzantine equivocation.

## 4. Certificate Revocation
A certificate is automatically revoked if:
- G-SRI > 0.85 for more than 5 consecutive governance epochs.
- A valid Equivocation-Proof is circulated in the GIEN mesh.
- TPM PCR_MATCH fails for the primary reasoning kernel.
