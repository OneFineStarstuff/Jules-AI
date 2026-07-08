# GIE-SPEC-038: Regulatory Handover & Supervisor Read-Access Protocol
**Version:** 1.0.0
**Architect:** Jules
**Status:** CANONICAL SPECIFICATION

## 1. Handover Objective
This specification defines the secure protocol for granting regulatory supervisors (e.g., ECB, FED, MAS) read-only access to the institutional **GIE-SOC** dashboards and **PQC-WORM** audit sinks.

## 2. Supervisor Read-Access Tiers
Access is granted via **Supervisor-SVIDs** issued by the institutional **GIE-CA**:
- **Tier 1 (Metric):** Access to real-time G-SRI and CDI telemetry.
- **Tier 2 (Audit):** Access to PQC-signed audit logs (RCEs) and ZK-proof metadata.
- **Tier 3 (Forensic):** Access to the **GDT** and forensic reconstruction environments.

## 3. Cryptographic Handover Protocol
1. **Request:** Regulator issues a signed CSR (Certificate Signing Request) via the GIEN Alpha Path.
2. **Authorization:** Institutional board (GBEC) validates the request using a 3-of-5 quorum.
3. **Provisioning:** GIE-CA issues a limited-duration (24h) SVID restricted to the /v1/telemetry/readonly namespace.
4. **Anchoring:** The handover event is recorded as a **T4 Governance State Change** in the PQC-WORM.

## 4. Evidence Handover (GIRS)
Standardized regulatory reports (GIRS-Schema) are automatically pushed to the regulator's **Supervisory Control Plane (SCP)** every 24 hours. The regulator verifies the report using the institutional GACRA public key.
