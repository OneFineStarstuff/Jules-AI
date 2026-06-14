# ISO/IEC 42001:2023 AI Management System (AIMS) Certification Dossier

## 1. Context of the Organization
G-SIFI Global Core implements the Sentinel stack to manage the risks and opportunities associated with AGI/ASI reasoning kernels.

## 2. AI Policy & Objectives
- **Policy:** Mandatory GDL sidecar gating for all inference turns.
- **Objective:** Maintain G-SRI < 0.20 and 100% attestation success rate.

## 3. Risk Assessment & Treatment
- **Assessment:** Bayesian G-SRI Scoring Engine (src/governance_engine/gsri_scoring_engine.py).
- **Treatment:** IRMI Hardware Kill-Switch (src/governance_engine/irmi_driver.py).

## 4. Operational Controls
- **Control A.5.2 (Lifecycle):** BBOM Perpetual Assurance (BBOM_PERPETUAL_ASSURANCE_PATTERN.md).
- **Control A.8.4 (Traceability):** PQC-WORM logging (src/infrastructure/pqc_worm_logger.py).

## 5. Performance Evaluation
- **Monitoring:** Omni-Sentinel 24h Monitor (omni_sentinel_24h_monitor.py).
- **Internal Audit:** Auditor-Agent Swarms verifying RCE logs in S3.

---
**Certification Status:** PENDING FINAL AUDIT
**Lead Auditor:** Jules
