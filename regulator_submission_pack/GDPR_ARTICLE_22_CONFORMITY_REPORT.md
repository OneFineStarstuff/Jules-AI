# GDPR Article 22: Automated Individual Decision-Making Compliance

## 1. Scope
This report details the safeguards implemented for the Sentinel stack regarding automated decision-making (ADM) as per **GDPR Article 22**.

## 2. Right to Explanation
- **EBM Explainers:** WorkflowAI Pro utilizes **Explainable Boosting Machines** to provide feature-level contribution scores for every automated credit/trading decision.
- **Causal Logs:** Reasoning traces stored in the **PQC-WORM** layer include the "Self-Reflection" step where the agent explains its logic in human-readable natural language.

## 3. Human-in-the-Loop (HITL)
- **HALT Protocol:** Any decision with a confidence score < 0.85 (or CDS > 0.05) is automatically halted and routed to the **SACC Dashboard** for human intervention.
- **Override Mechanism:** The **GovernanceDashboard.tsx** allows authorized human officers to override agentic actions, with every override anchored to the **OmniSentinel** blockchain ledger.

## 4. Data Minimization & Privacy
- **Salted Hashing:** All PII identifiers are hashed using **Salted SHA-256** at the ingestion point (src/infrastructure/utils.py).
- **Enclave Isolation:** Data is processed only within hardware-encrypted memory.

---
**Status:** CANONICAL COMPLIANCE LOCK
