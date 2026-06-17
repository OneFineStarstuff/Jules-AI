# Supervisory Control Plane: Regulator Demo Script (90 Minutes)

**Objective:** Demonstrate real-time AI governance, ZK-proof verification, and federated oversight.

## Phase 1: Orientation & System Overview (00:00 - 00:15)
- **Speaker:** Lead Architect
- **Handoff:** Lead to Compliance Officer
- **Key Points:**
    - SCP Architecture: The "Supervisory Nervous System".
    - Role of the Governance State Machine (GSM).
    - Introduction to the 2028 G-SIFI Pilot.

## Phase 2: Live Inference & Policy Gating (00:15 - 00:35)
- **Demo Segment:** Triggering a GDL/Rego violation.
- **Visuals:** Dashboard showing G-SRI spiking and GSM transitioning to `CONTINUATION_REFUSAL_STATE`.
- **Handoff:** Compliance to DevSecOps Lead.
- **Fallback:** Pre-recorded "Scenario PHOENIX" video if the live inference cluster is latent.

## Phase 3: The Evidence Pipeline (00:35 - 00:55)
- **Demo Segment:** Decision Trace -> ZK Prover -> PQC-WORM.
- **Live Tooling:**
    - `omni_sentinel_cli.py verify-trace <trace_id>`
    - Inspection of the Merkle STH in the Kafka audit log.
- **Technical Deep Dive:** Explaining ML-DSA-87 and PLONKY2 recursive aggregation.

## Phase 4: Regulator Verification Node (00:55 - 01:15)
- **Demo Segment:** Live Verifier Node CLI.
- **Regulator Perspective:** Running the Verifier container and confirming STH consistency.
- **Live Tooling:** TLA+ Toolbox walkthrough showing SIP v3.0 model checking (NoSilentDivergence invariant).

## Phase 5: Q&A and Tactical Fallbacks (01:15 - 01:30)
- **Moderator:** Engagement Lead
- **Roleplay:** Anticipated questions on TEE boundaries and data privacy.
- **Closing:** Handing over the Digital Takeaway Packet.

---
**Fallback Tactics:**
1.  **Enclave Failure:** Switch to "Simulation Mode" with mocked vTPM attestation traces.
2.  **ZK Latency:** Show pre-computed proof batches.
3.  **Connectivity:** Local hotspot backup for GIEN mesh gossip.
