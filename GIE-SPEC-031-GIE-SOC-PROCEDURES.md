# GIE-SPEC-031: GIE-SOC Operational Procedures
**Version:** 1.0.0
**Architect:** Jules
**Status:** CANONICAL SPECIFICATION

## 1. Governance Intelligence Operations Center (GIE-SOC)
The **GIE-SOC** is the 24/7 technical monitoring hub for institutional governance.

## 2. Monitoring Invariants
Operators must maintain continuous visual oversight of:
- **G-SRI Dashboard:** Trigger T3 containment if G > 0.60 for more than 60 seconds.
- **TPM Heartbeat:** Trigger T2 pause if more than 5% of enclaves fail PCR_MATCH.
- **WORM Sync:** Triage latency spikes exceeding 120 seconds.

## 3. Incident Triage Workflow
1. **Detection:** GKQL-based automated alert from GKG.
2. **Analysis:** Auditor-Agent (AGA) performs deep semantic probe of the relevant RCE.
3. **Escalation:** If breach confirmed, mobilize GBEC for 3-of-5 quorum signature.
4. **Enforcement:** Execute manual IRMI kill if automated GIRI fails.

## 4. Shift Handover
Shift handovers require a signed **Handover-Attestation** containing:
- Summary of all T2/T3 events in the last 8 hours.
- PQC-WORM root consistency verification.
- Status of active GDT shadow-simulations.
