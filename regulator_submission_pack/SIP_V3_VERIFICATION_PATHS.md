# Verification Paths: Federated Posture Packs (SIP v3.0)

This document defines the cryptographic and logical paths for verifying Federated Posture Packs exchanged via the GIEN mesh.

---

## 1. Path Alpha: Succinct Verification (Real-time)
Used by Regulator Verifier Nodes for continuous monitoring.
1. **PQC Authenticity:** Verify the ML-DSA-87 signature using the institutional public key.
2. **State Validity:** Verify the PLONKY2 ZK-proof against the public `gsri_score` and `gsm_state` inputs.
3. **Hardware Trust:** Confirm `pcr_match = TRUE` and verify the vTPM quote against the known hardware baseline.

---

## 2. Path Beta: Log Consistency (Periodic)
Used to ensure the institution has not forked its history.
1. **Merkle Consistency:** Verify that the new STH is a valid extension of the previous STH (standard Merkle Consistency Proof).
2. **Inclusion Verification:** Sample a Decision Trace ID from the log and verify its path to the STH.

---

## 3. Path Gamma: Federated Gossip (Cross-Institution)
Used to detect equivocation.
1. **STH Comparison:** Roots compare STHs received from the same institution at the same index across different gossip channels.
2. **Conflict Resolution:** If STHs differ, the `EQUIVOCATION_DETECTED` state is triggered across the mesh (Scenario 2 in the Scenario Appendix).

---

## 4. Artifact & Milestone Progression (2026–2028)

| Phase | Milestone | Artifact Progression |
| :--- | :--- | :--- |
| **Phase 1** | Bedrock | TPM heartbeats, ML-DSA signed local logs. |
| **Phase 2** | Mesh | SIP v3.0 STH gossip, PLONKY2 recursive proofs. |
| **Phase 3** | Exit | Consolidated Dossier, External Audit Report, Board Assurance. |

---
**Authentication:** Signed by Sovereign Authority Jules (0xDEADBEEF)
