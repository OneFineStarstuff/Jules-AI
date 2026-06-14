# GSRI Proof Verification Logic: Recursive SNARKs & STARKs

## 1. Local Proving (Inference Sidecar)
Each Sentinel Sidecar generates a **Groth16** proof using the `SystemicRiskAggregator.circom` circuit.
- **Private Inputs:** Local risk vectors (Resonance, CDI, Collusion).
- **Public Outputs:** Boolean compliance result and the aggregated G-SRI delta.

## 2. Recursive Aggregation (ZK Relayer)
The **ZK Relayer** collects proofs from $ sidecars and utilizes **SnarkPack** or **Plonky2** to generate a single "Governance Root Proof."
- **Logic:** The aggregator circuit verifies the signatures of the $ proofs and asserts that the global G-SRI mean is below the Basel IV threshold (0.85).

## 3. Blockchain Committal
The root proof is submitted to the `OmniSentinel.sol` contract. The `verifyProof()` function on-chain (generated via `snarkjs`) validates the transition of the systemic risk state before the ledger is updated.

---
**Status:** ZK ARCHITECTURE v1.2
