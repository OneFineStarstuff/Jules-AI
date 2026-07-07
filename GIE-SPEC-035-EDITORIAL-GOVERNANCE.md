# GIE-SPEC-035: Editorial Standards for GIE Standards Documents
**Version:** 1.0.0
**Architect:** Jules
**Status:** CANONICAL SPECIFICATION

## 1. Structural Mandates
Every GIE Standard (GIE-STD) must adhere to the following section hierarchy:
1. **Abstract:** High-level intent and regulatory context.
2. **Mathematical Formulation:** LaTeX-based definition of the core logic.
3. **Formal Invariants (TLA+):** State-machine constraints for verification.
4. **ZK-Constraint Mapping:** Private vs. public input definitions for AIR circuits.
5. **Regulatory Traceability:** Machine-readable OSCAL mapping.

## 2. Linguistic Precision
- **SHALL/MUST:** Mandatory technical requirements.
- **SHOULD:** Recommended best practices.
- **MAY:** Optional implementation details.
- **INVARIANT:** Formal state-transition constraint.

## 3. Versioning & Immutability
Standards must be versioned using SemVer 2.0. Once a standard achieves **CANONICAL** status, its previous versions are archived in the **PQC-WORM** sink to maintain a non-repudiable history of governance logic.

## 4. Peer Review
All new standards require a unanimous (5-of-5) **GBEC** approval and a ZK-proof of formal model-checking completeness.
