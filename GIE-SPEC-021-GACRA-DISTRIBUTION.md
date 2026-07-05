# GIE-SPEC-021: Sentinel Registry (GACRA) & Policy Distribution
**Version:** 1.0.0
**Architect:** Jules
**Status:** CANONICAL SPECIFICATION

## 1. Sentinel Artifact & Compliance Registry (GACRA)
GACRA is the immutable source of truth for all governance artifacts.
- **Content:** GDL scripts, OPA policies, TLA+ models, and model weight hashes.
- **Integrity:** Every artifact is hashed and stored in a Merkle tree anchored in the institutional PQC-WORM.

## 2. Policy Distribution (GitOps)
Policy updates are distributed using a GitOps-based pull model:
1. **Commit:** Architects commit signed policy changes to the GDL repository.
2. **Verify:** CI/CD pipeline executes TLA+ model checking and GDT zero-drift verification.
3. **Publish:** Validated artifacts are pushed to GACRA.
4. **Sync:** GEE sidecars periodically poll GACRA and reconcile their local state.

## 3. Propagation Latency
- **Normal Update:** Mesh-wide propagation within < 60 seconds.
- **Emergency Update:** Global 'Omega' override propagated via the GIEN Alpha Path in < 100ms.

## 4. Rollback Invariant
Policies can only be rolled back to a previous state if the GMF proves that the rollback does not violate current safety redlines.
