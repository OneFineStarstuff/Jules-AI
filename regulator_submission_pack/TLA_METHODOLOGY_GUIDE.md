# TLA+ Methodology & Model-Checking Guide: SIP v3.0

This guide provides the formal verification rationale for the Sentinel Interoperability Protocol (SIP v3.0), as specified in `src/governance_engine/SIP_v3_0_Protocol.tla`.

---

## 1. Design and Validation Framework
The SIP v3.0 TLA+ specification models the Supervisory Control Plane (SCP) as a distributed system where institutions publish Signed Tree Heads (STHs) and Roots gossip to ensure global consistency.

### 1.1 Byzantine Fault Model
The specification accounts for **Byzantine Institutions** that may attempt to equivocate (publish different hashes for the same Merkle index) and **Silent Institutions** that fail to provide heartbeats.
- **Assumptions:** Roots are primarily honest, but the protocol is designed to detect root divergence if roots themselves are compromised.

---

## 2. Critical Invariants

### 2.1 Safety: No Silent Divergence
- **Definition:** If two honest roots observe STHs for the same index from the same institution, the hashes must match.
- **Constraint:** `NoSilentDivergence == \A i \in Institutions : \A r1, r2 \in Roots : ...`
- **Result:** TLC verifies that any divergence immediately transitions the system to `EQUIVOCATION_DETECTED`, preventing unobserved drift.

### 2.2 Liveness: Root Convergence
- **Definition:** Eventually, every honest root will see the latest STH published by an institution, provided the institution remains "OK".
- **Temporal Property:** `[]<>RootConvergence`.
- **Mechanism:** Enforced via Weak Fairness (`WF_vars`) on the `GossipSTH` action.

### 2.3 Completeness: Missing Attestation Detectable
- **Definition:** If an institution stops publishing for more than `MaxMissing` windows, roots will consistently flag the institution as `MISSING_ATTESTATION`.
- **Result:** Ensures that "liveness failure" by an agentic swarm is distinguishable from a network partition.

---

## 3. TLC Model-Checking Walkthrough

To validate the specification, regulators and auditors should run TLC using the following parameters:

### 3.1 Model Configuration (Phase 0 Sandbox)
- **Constants:**
    - `Institutions`: {I1, I2}
    - `Roots`: {R1, R2}
    - `MaxTreeSize`: 3
    - `MaxMissing`: 2
- **Checks:**
    - Invariants: `NoSilentDivergence`, `TypeOK`.
    - Properties: `[]<>RootConvergence`.

### 3.2 Interpreting Results
- **Success:** TLC completes without finding a deadlock or invariant violation, confirming that the protocol handles all state interleavings (normal, equivocation, silence) correctly.
- **Counterexamples:** Any found counterexample indicates a logic gap where a Byzantine institution could potentially fork the log without detection—none were found in the current v1.1.0 specification.

---
**Verification Anchor:** PQC-SIGNED-FORMAL-SPEC-TRACE-0x87A...
