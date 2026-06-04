# GC-IR Bridge: TLA+ to zk-SNARK Compiler
**Role:** Formal-to-Cryptographic Translation

## 1. Compilation Pipeline
1. **Parser:** Ingests `AGI_Containment_Kernel.tla`.
2. **Intermediate Representation (IR):** Maps TLA+ state transitions to arithmetic constraints.
3. **Circom Generator:** Produces `systemic_risk_aggregator.circom` logic.

## 2. Soundness
Ensures that a valid SNARK proof is computationally equivalent to a formal model check success.
