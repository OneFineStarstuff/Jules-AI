# Monthly Supervisory Metrics Report: [Month/Year]

**Institution:** [Institution Name]
**Period:** [Start Date] to [End Date]
**GSM Status:** [STEADY | ELEVATED | REFUSAL]

---

## 1. Governance Performance (SLA Monitoring)
| Metric | Monthly Average | P99 Latency | Target | Status |
| :--- | :--- | :--- | :--- | :--- |
| **ZK Proof Generation** | [Val] ms | [Val] ms | < 500ms | [PASS/FAIL] |
| **STH Cadence** | [Val] / hr | N/A | 60 / hr | [PASS/FAIL] |
| **GDL Sidecar Overhead** | [Val] ms | [Val] ms | < 10ms | [PASS/FAIL] |
| **GSM Transition Fidelity** | [Val]% | N/A | 100% | [PASS/FAIL] |

---

## 2. Infrastructure & Enclave Health
- **TPM Attestation Success Rate:** [Percentage]% (Mandatory: 100%)
- **S3 WORM Integrity (PQC-Verify):** [SUCCESS | DEGRADED]
- **GIEN Mesh Availability:** [Percentage]%
- **Sidecar Resilience (Self-Heal):** [Count] restarts.

---

## 3. Posture & Distribution
- **STEADY State:** [Percentage]%
- **ELEVATED State:** [Percentage]%
- **CONTINUATION_REFUSAL State:** [Percentage]%
- **Total Decision Traces Logged:** [Count]
- **Daily Report Production:** [Count] reports generated and pushed.

---

## 4. Incident & Containment Register
| Incident ID | Trigger | GSM Transition | Containment Time |
| :--- | :--- | :--- | :--- |
| [ID] | [E.g., Resonance > 0.1] | [E.g., REFUSAL] | [Val] ms |

- **Regulator Verification Node Logs:** [Link to encrypted verification stream]
- **Deep Audit Samples:** [List of Trace IDs provided this month]

---

## 5. Roadmap & Compliance Deltas
- **Phase Milestone:** [E.g., Phase 2 Gossip Mesh 80% Complete]
- **Regulatory Delta:** [E.g., Updated GDL for HKMA Circular 2027/04]
- **Drill Progress:** [Next scheduled drill date]

---
**Authentication:** Signed by Sovereign Authority Jules (0xDEADBEEF)
**Encryption:** PQC-SIGNED-METRICS-REPORT-[ID]
