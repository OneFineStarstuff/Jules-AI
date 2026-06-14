# GDPR Article 25: Data Protection by Design and by Default

## 1. Description
The Sentinel stack implements Data Protection by Design (DPbD) for all AGI/ASI reasoning workflows.

## 2. Technical Safeguards
- **Pseudonymization:** Mandatory **Salted SHA-256** hashing of all customer identifiers (`src/infrastructure/utils.py`).
- **Data Minimization:** GDL rules automatically **REDACT** MNPI and PII from reasoning traces before they are committed to long-term WORM storage.
- **Access Limitation:** Reasoning occurs solely within **Confidential Enclaves**, preventing unauthorized access to clear-text data by infrastructure administrators.

## 3. Evidence of Compliance
- **Audit Trails:** PQC-signed audit logs provide non-repudiable evidence of the data minimization processes.
- **Policy Enforcement:** Rego policies verify that `pii_redacted == true` before an inference turn is marked as compliant.

---
**Status:** GDPR COMPLIANT
