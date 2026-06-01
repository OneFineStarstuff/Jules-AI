# Regulator Reporting & Assurance Specification
## Standard: OSCAL-GSIFI-2035

## 1. Machine-Readable Compliance (OSCAL)
The institution utilizes the **NIST Open Security Controls Assessment Language (OSCAL)** to provide regulators with machine-readable catalogs and profiles of active AGI controls.
*   **Catalog:** Machine-readable definition of all SR 11-7 and EU AI Act Art 11 controls.
*   **Assessment Plan:** Automated schedule for stress-testing and MGK invariant validation.

## 2. ARRE (Automated Regulator Reporting Engine)
The **ARRE** service assembles the **Annex IV Conformity Dossier** in real-time.
1.  **Input:** Kafka WORM logs containing TraceIDs and HEA signatures.
2.  **Mapping:** OPA-based translation of technical traces to regulatory articles.
3.  **Output:** PQC-signed XML/JSON dossiers submitted via the Supervisory API Gateway.

## 3. VAR (Verified Alignment Report)
The VAR is a high-level summary for regulators, generated quarterly, providing:
*   **Alignment Resumee:** Average resonance score across all Reasoning Kernels.
*   **Drift Attestation:** Monthly Capital Drift Index (CDI) trends.
*   **Simulation Trace:** Evidence of successful quarterly "Red Dawn" crisis program execution.

## 4. Supervisory Dashboard (GAI-SOC)
A regulator-scoped view into the bank's GAI-SOC, providing:
*   **Heartbeats:** Functional verification of IRMI kill-switches across global clusters.
*   **Proof Explorer:** Navigation of zk-SNARK proof bundles (CAS-SPP).
*   **Sanction Audit:** Log of all autonomous remediation actions (ARE) taken during the period.

---
*Authorized for Supervisory Access*
*Ref: OSCAL-ARRE-SPEC-2035*
