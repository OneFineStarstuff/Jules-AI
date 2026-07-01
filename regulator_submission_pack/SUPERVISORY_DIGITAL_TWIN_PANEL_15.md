# Supervisory Digital Twin: Replays & Guidance (Panel 15)
**Interface Version:** SCP v3.0
**Dossier Reference:** Phase I / Annex 15

## 1. The Panel 15 Interface
Panel 15 of the **Unified AI Supervisory Control Plane (SCP v3.0)** provides regulators with real-time "Time-Travel" replay capabilities. This module allows supervisors to review the **Digital Twin** states leading up to any containment action (HARD_KILL or PAUSE).

## 2. Replay Mechanisms
- **Deterministic Replay:** Every agentic decision is logged with its full cognitive context and PQC-signed model weights.
- **Counterfactual Simulation:** Regulators can modify perturbation parameters in the replay environment to observe alternative containment outcomes.
- **Evidence Locker:** All replays are anchored to the **Governance WORM Repository (GWR)**.

## 3. Supervisory Guidance
### 3.1 Interpreting G-SRI Drift
When observing drift in Panel 15, supervisors should correlate $S_c$ (Cosine Similarity) and $D_{TED}$ (Goal-Tree Edit Distance) to identify "Intentional Malalignment" vs. "Stochastic Noise."

### 3.2 Containment Thresholds
Intervention is mandatory when G-SRI > 0.85. Panel 15 provides a visual "Heat Map" of the agentic mesh to identify systemic nodes approaching this threshold.

---
**Access Key:** `REGULATOR_ELEVATED_V4`
**Session Integrity:** ZK-Attested via `gien_relay.py`
