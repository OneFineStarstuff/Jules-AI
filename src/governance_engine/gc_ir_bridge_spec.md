# GC-IR Bridge Specification (TLA+ to Circom)
**Status:** EXPERIMENTAL // RESEARCH READINESS

## 1. Overview
The GC-IR (Governance Compiler - Intermediate Representation) bridge defines the formal pipeline for compiling TLA+ safety invariants into Circom R1CS constraints for generating succinct zk-SNARK compliance proofs.

## 2. Compilation Pipeline
1. **TLA+ Source:** Safety invariants (e.g., Non-Escapement MI-1).
2. **IR Emission:** Formal lemma extraction into Boolean satisfiability (SAT) structures.
3. **Circom Mapping:** Compilation into R1CS constraints (SystemicRiskAggregator.circom).
4. **zk-SNARK Generation:** Proof generation via SnarkPack for institutional verification.

## 3. Verified Invariants
- **Resource Containment:** $\forall t: \text{usage}(t) < \text{quota}$.
- **Decision Determinism:** GDL(intent) $\rightarrow$ decision $\in$ {ALLOW, DENY, HALT}.
