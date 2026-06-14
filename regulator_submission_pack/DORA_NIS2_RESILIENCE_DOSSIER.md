# DORA & NIS2: Digital Operational Resilience & Supply Chain Dossier

## 1. ICT Risk Management (DORA Art. 14)
The Sentinel stack ensures real-time ICT risk detection through the **GAI-SOC** telemetry mesh. P99 interaction latency is maintained below 100ms, with immediate fail-over to multi-region SEV-SNP nodes if a regional breach is detected.

## 2. Supply Chain Security (NIS2)
- **BBOM Verification:** Every component in the AI supply chain (kernel, weights, GDL) is cryptographically verified via the **Blockchain Bill of Materials**.
- **PQC Hygiene:** Mandatory use of **ML-DSA-87** signatures for all inter-institutional communications, protecting against supply-chain tampering by quantum-capable actors.

## 3. Incident Reporting
Systemic incidents are gossiped across the **GIEN Relay** and committed to the **PQC-WORM** sink within 1 minute of detection, satisfying the 24-hour initial notification requirement for "Essential Entities."

---
**Status:** RESILIENCE LOCK v1.0
