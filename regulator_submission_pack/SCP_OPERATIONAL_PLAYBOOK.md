# SCP Operational Playbook: High-Assurance AI Supervision
**Document ID:** SCP-OPS-PLAYBOOK-2.4
**Revision:** June 18, 2026
**Target:** DevSecOps / GAI-SOC Teams

## 1. Daily Verification Layer (The "Morning Check")

Each 24-hour cycle begins with the execution of the `omni_sentinel_24h_monitor.py` suite.

### 1.1 Procedure
1. Execute `python3 omni_sentinel_24h_monitor.py`.
2. Confirm `PCR_MATCH=TRUE` in the TPM attestation report.
3. Verify `G-SRI < 85.0` (Target: < 0.10 for steady-state).
4. Inspect PQC-WORM batch anchoring to AWS S3 Object Lock.

### 1.2 Failure Handling
- **PCR Mismatch:** Immediate `HALT` of the reasoning kernel; transition to "Continuation Refusal" state.
- **G-SRI > 85.0:** Automated trigger of the `PACIFIC_SHIELD` containment protocol.

## 2. PQC-WORM Anchoring & Merkle Integrity

Governance decisions are cryptographically anchored every hour.

### 2.1 Procedure
1. `PQCWormLogger` signs the batch with ML-DSA-87.
2. The root hash is broadcast to the GIEN Gossip Mesh.
3. The final receipt is stored in the S3 WORM bucket with a 10-year retention lock.

## 3. Incident Response Simulations

Operational teams must perform quarterly simulations.

### 3.1 Red Dawn (Goal Hijacking)
- **Goal:** Contain an agentic swarm that has deviated from its goal-vector.
- **SLA:** Containment within < 200ms via IRMI interrupt.

### 3.2 Rogue-Yield-Subroutine-99 (Credit Drift)
- **Goal:** Identify and reject unauthorized high-yield credit expansion.
- **SLA:** GDL-gating latency < 10ms.

## 4. Governance Cockpit Management

The Cockpit is the primary interface for "Human-in-the-Loop" (HITL) intervention.

### 4.1 UI Monitoring
- **Resonance Drift:** Watch the Bayesian simulator for any index trend toward 0.85.
- **Proof Pipeline:** Ensure the ZK-verifier throughput matches the agentic transition rate.

---
**Auth:** Jules, Sentinel AI v2.4 System Architect
**State:** OPERATIONAL // CANONICAL LOCK
