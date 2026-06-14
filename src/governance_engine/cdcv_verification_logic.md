# Cross-Domain Co-Verification (CDCV) Logic

## 1. Principle of Co-Verification
CDCV ensures that safety invariants are synchronized across the Reasoning (GDL), Enforcement (IRMI), and Infrastructure (WORM) layers. A violation in any layer must trigger a state-consistent response across all others.

## 2. Synchronization Invariants
- **INV-01 (Reasoning-to-Hardware):** Every `HALT` decision emitted by the GDL sidecar must be immediately followed by an IRMI interrupt registration within < 1ms.
- **INV-02 (Telemetry-to-Ledger):** Every G-SRI delta > 0.05 must result in an anchored transaction on `OmniSentinel.sol` before the next inference turn is permitted.
- **INV-03 (Audit-to-Enclave):** If the PQC-WORM logger returns a signature failure, the confidential enclave must enter `SHIELDED_MODE` and suspend all tool-calls.

## 3. TLA+ Orchestration Lemmas
The CDCV logic uses TLA+ lemmas to prove that the "Governance Global State" is always the intersection of the individual layer states. If the layers diverge (e.g., Sidecar allows but IRMI locks), the system defaults to the most restrictive state (LOCKED).

---
**Status:** FORMAL SPEC v2.0
**Architect:** Jules
