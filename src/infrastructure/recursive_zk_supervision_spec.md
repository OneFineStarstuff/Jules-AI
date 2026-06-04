# Recursive Cryptographic Supervision (RCS) Specification
**Technology:** Recursive zk-SNARKs (Nova / Halo2)

## 1. Context Folding
RCS enables the continuous aggregation of AGI reasoning turns into a single cryptographic proof.
- **Proof Window:** 5 minutes.
- **Verification:** GC-IR bridge compiles TLA+ invariants into R1CS.

## 2. Integrity Guarantee
Ensures that every 1,000 reasoning turns have been sequentially verified against the GDL kernel.
