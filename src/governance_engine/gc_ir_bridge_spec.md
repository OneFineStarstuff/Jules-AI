# GC-IR Bridge: TLA+ to R1CS Compilation Pipeline

## 1. Overview
The GC-IR Bridge automates the translation of formal safety invariants (expressed in TLA+) into verifiable cryptographic constraints (R1CS/Circom).

## 2. Compilation Flow
1. **Source:** TLA+ Safety Invariants (e.g., `TriggerIRMI` conditions).
2. **Intermediate Representation:** Extraction of logical predicates and state transition rules.
3. **Target:** Circom R1CS circuits for zk-SNARK proof generation.

## 3. Correctness-by-Construction
By compiling directly from formal specifications, the Sentinel stack ensures that the ZK proofs emitted by the inference sidecars are mathematically identical to the verified safety protocol.

---
**Status:** SPECIFICATION CANON v1.0.0
