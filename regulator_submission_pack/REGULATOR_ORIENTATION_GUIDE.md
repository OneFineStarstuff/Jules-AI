# Regulator Orientation Guide: Supervisory Control Plane (SCP)

This guide provides the necessary technical and procedural orientation for regulatory staff interacting with the SCP evidence pipeline.

---

## 1. Navigating the Evidence Lifecycle
The SCP generates a continuous stream of cryptographic evidence. Regulators should follow this flow:
1.  **Policy Inquiry:** Start with the **GDL Master Canon** to understand the active safety constraints.
2.  **Telemetry Audit:** Use the **Regulator Verifier Node** to pull Signed Tree Heads (STHs) from the GIEN mesh.
3.  **Proof Validation:** Execute the ZK-verification CLI against the STH to confirm the PLONKY2 proof is valid.
4.  **Forensic Sampling:** Request inclusion proofs for specific Trace IDs to verify they are anchored in the Merkle log.

---

## 2. Operating the Verifier Node
The Verifier Node is a containerized environment (provided as `sentinel-verifier:latest`) that allows regulators to:
- **Subscribe:** Listen to institutional gossip on the GIEN `governance.sth.broadcast` topic.
- **Verify:** Re-calculate Merkle roots and verify ML-DSA-87 signatures.
- **Alert:** Automatically flag silence (missing attestation) or forks (equivocation).

---

## 3. Understanding GSM States
The Governance State Machine (GSM) dictates the operational posture:
- **STEADY:** Normal operations; no intervention required.
- **ELEVATED:** High-frequency risk oscillations; oversight team is active.
- **REFUSAL:** Automated gating active; inference cluster is paused or limited.
- **HALT:** IRMI kill-switch triggered; emergency shutdown.

---

## 4. Troubleshooting & Support
- **Credential Issues:** Contact the Institutional Security Liaison via the GIEN secure channel.
- **Verifier Node Failures:** Refer to the `DE_TELECOM_CHATBOT_GOVERNANCE_BLUEPRINT.md` for infrastructure recovery steps or use the backup Hotspot provided in the Demo Kit.
- **Data Interpretation:** Use the **Causal Inference Explainer** artifacts attached to each Refusal event.

---
**Status:** Canonical Version 1.0
**Encryption Anchor:** PQC-SIGNED-ORIENTATION-GUIDE-0x87A...
