# ICGC Phase 1 & 2 zk-Verified Control Standards
**Status:** SUPRANATIONAL CANON
**Governance:** International Compute Governance Consortium (ICGC)

## 1. Planetary FLOP Quotas
- **Redline Threshold:** 0^{26}$ cumulative FLOPs for any training run.
- **Reporting Mandate:** All G-SIFIs must submit a signed `gacmo_compute_manifest.json` every 24h.
- **Enforcement:** IRMI hardware-kill must be linked to quota exhaustion.

## 2. zk-Verified Behavioral Alignment
- **Trace Integrity:** Reasoning traces must be committed to PQC-WORM with valid zk-STARK proofs of GDL compliance.
- **Alignment Proofs:** SnarkPack aggregation used to verify that no turn violates the "Honesty Manifold" defined in the CAIGO root.
- **Containment Proofs:** Formal evidence that the reasoning kernel remained within the AMD SEV-SNP/Intel TDX secure enclave boundary.
