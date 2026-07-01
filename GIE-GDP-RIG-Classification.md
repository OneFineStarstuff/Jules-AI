# GIE Classification: GDP Tiers and RIG Families
**Version:** 1.0.0
**Architect:** Jules

## 1. Governance Data Protection (GDP) Tiers
To ensure confidentiality and regulatory compliance (GDPR, SEC 17a-4), all governance data is classified into four tiers:

| Tier | Sensitivity | Description | Storage Protocol |
| :--- | :--- | :--- | :--- |
| **T1** | Public/Institutional | Aggregated G-SRI scores, compliance statuses. | standard DB / GDL Registry |
| **T2** | Restricted | Policy metadata, non-sensitive telemetry. | Encrypted DB / mTLS |
| **T3** | Confidential | Reasoning traces, goal-decomposition vectors. | TEE Memory / zk-SNARK |
| **T4** | Secret | Cryptographic tokens, PII (hashed), private keys. | Hardware Security Module (HSM) |

## 2. Regulatory Integrity Groups (RIG) Families
RIG families cluster controls to simplify multi-jurisdictional compliance.

### 2.1 Financial-RIG
- **Target:** Basel III/IV, SR 11-7, MAS FEAT, HKMA 2030.
- **Controls:** Capital buffer reports, G-SRI scoring accuracy, fiduciary gating.

### 2.2 Safety-RIG
- **Target:** EU AI Act, NIST AI RMF, ISO 42001.
- **Controls:** Risk management systems, human oversight triggers, transparency logs.

### 2.3 Resilience-RIG
- **Target:** DORA, NIS2, SR 26-2.
- **Controls:** Incident response latency, PQC-WORM continuity, cross-cloud failover.

### 2.4 Privacy-RIG
- **Target:** GDPR Article 22, SEC 17a-4.
- **Controls:** Salted PII hashing, immutable audit trails, right-to-explanation logs.
