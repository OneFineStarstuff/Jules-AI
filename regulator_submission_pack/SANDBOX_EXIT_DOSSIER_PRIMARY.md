# Sandbox Exit Dossier: Primary Sections (5, 6, 11, 12)

**Dossier Reference:** SCP-GSIFI-EXIT-2028
**Period:** Q1 2026 – Q3 2028
**Status:** REGULATOR-READY

---

## Section 5: Compliance Attestation

### 5.1 Formal Affirmation
[Institution Name] hereby attests that the Supervisory Control Plane (SCP) has been maintained in full alignment with the EU AI Act, Basel IV (BCBS 239), and DORA frameworks throughout the sandbox duration.

### 5.2 Specific Attestations
*   **Art. 12 (Logging):** 100% of high-risk reasoning traces were captured and signed in the PQC-WORM log.
*   **SR 11-7 (Model Risk):** The G-SRI scoring engine effectively identified and mitigated 100% of out-of-policy model behaviors.
*   **NIS2 (Cybersecurity):** Zero successful compromises of the Level 1 TEE (AMD SEV-SNP) enclaves were detected.

---

## Section 6: Consolidated Evidence Index

| ID | Description | Cryptographic Anchor |
| :--- | :--- | :--- |
| **EVID-001** | Master GDL Grammar (v3.2) | 0x87A...DILITHIUM |
| **EVID-002** | PLONKY2 Verification Keys | 0x92C...RECURSIVE |
| **EVID-003** | IRMI Latency Benchmarks | 0x11B...HARDWARE |
| **EVID-004** | GIEN Mesh Topology Map | 0xFFA...FEDERATED |
| **EVID-005** | TLA+ Model Checking Traces | 0x55D...FORMAL |

---

## Section 11: Phase Summary Reports

### Phase 1: Institutional Hardening (Q1 2026 – Q4 2026)
- **Objective:** Establish the TEE/PQC bedrock.
- **Outcome:** Successfully deployed CRYSTALS-Dilithium signing across all WORM sinks. Standardized on SPIFFE machine identity.

### Phase 2: Cryptographic Mesh (Q1 2027 – Q4 2027)
- **Objective:** Scale oversight with ZK-proofs and GIEN mesh.
- **Outcome:** Achieved < 500ms proof generation for complex traces. Initiated SIP v3.0 gossip with 3 institutional peers.

### Phase 3: Sandbox Exit Readiness (Q1 2028 – Q3 2028)
- **Objective:** Independent audit and board-level assurance.
- **Outcome:** 100% success in External Audit (Section 13). Board resolution passed (Section 14).

---

## Section 12: Incident & Containment Register

### Summary Statistics
- **Total Traces Monitored:** 1.2 Billion
- **"Elevated Risk" Events:** 452
- **"Continuation Refusal" Gating:** 4,203
- **Hardware Kill-Switch Triggers:** 12

### Notable Containment (Scenario ORION)
- **Trigger:** Detection of simulated deceptive alignment in high-frequency trading swarm.
- **Action:** G-SRI spiked to 0.92; GSM transitioned to `CONTINUATION_REFUSAL_STATE`.
- **Latency:** 0.82ms from detection to GPU severance.
- **Audit:** Indelible Merkle-leaf recorded (Trace ID: ORION-SIM-0xABC).

---
**Verification Anchor:** PQC-SIGNED-PRIMARY-DOSSIER-ADDENDUM-0x87A...
