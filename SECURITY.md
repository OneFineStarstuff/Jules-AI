# Security Policy: Sentinel AI Governance Stack

## Supported Versions

| Version | Supported          | Description |
| ------- | ------------------ | --- |
| 2.4.x   | :white_check_mark: | Active Canonical Lock (2026-2035 Roadmap) |
| 2.3.x   | :x:                | Deprecated |
| 1.x     | :x:                | Legacy |

## Security Hardening Mandates
All deployments MUST adhere to the following:
1. **Confidential Computing:** Mandatory AMD SEV-SNP or Intel TDX isolation.
2. **Identity:** SPIFFE/SPIRE with mTLS. Long-lived API keys are prohibited.
3. **Audit:** All reasoning traces must be signed via HSM with ML-DSA-87 and committed to PQC-WORM storage.
4. **Metadata:** IMDSv2 MUST be enforced for all cloud instances.

## Reporting a Vulnerability
Security vulnerabilities affecting G-SIFI systemic stability should be reported via the **GIEN Relay** using the `VULNERABILITY_DISCLOSURE` signature type, or via encrypted email to security@sentinel.governance.
