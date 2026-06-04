# Unified Meta-Invariant Framework (UMIF)
**Methodology:** TLA+ / Coq / Q#

## 1. Core Invariants
- **MI-1: Boundary Integrity:** Agent reasoning cannot propagate beyond the Markov Blanket.
- **MI-2: Homeostatic Stability:** Systemic drift must remain < 15% to avoid SEV-0 IRMI.

## 2. Formal Verification
- **TLA+:** `SentinelContainmentProtocol.tla`.
- **zk-SNARK:** Proof generation via `systemic_risk_aggregator.circom`.
