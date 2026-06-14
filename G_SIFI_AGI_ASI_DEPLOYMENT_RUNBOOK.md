# G-SIFI AGI/ASI Deployment & Verification Runbook (2026-2035)

## 1. Prerequisites
- **Hardware:** AMD SEV-SNP or Intel TDX enabled compute clusters.
- **Identity:** SPIRE Server installed in the VPC; SVID rotation set to 12h.
- **Trust:** GSIB Master Root CA certificates.

## 2. Phase 1: Multi-Jurisdictional Substrate Deployment
1. **Infrastructure:** Execute Terraform in `infrastructure/terraform/`.
   - `terraform init`
   - `terraform apply -var-file="gsifi.tfvars"`
   - **Verification:** Ensure IMDSv2 is enforced on all nodes (`http_tokens = required`).
2. **Identity Mesh:** Configure SPIFFE federated trust across Primary (US-EAST) and Secondary (EU-WEST) regions.
3. **Audit Sink:** Provision MSK Kafka clusters and S3 buckets with 10-year Object Lock (Compliance Mode).

## 3. Phase 2: Governance Kernel Initialization
1. **Solidity Ledger:** Deploy `OmegaActual.sol` and `OmniSentinel.sol` using pinned compiler 0.8.20.
2. **GDL Injection:** Upload the GDL Master Canon to the Sentinel Sidecar Registry.
3. **IRMI Registration:** Verify `irmi_driver.py` successfully registers the INT 0x1A interrupt in the kernel.

## 4. Phase 3: Risk Simulation & Drills
- **Red Dawn Stage 6:** Execute `red_dawn_contagion_sim.py` to verify IRMI kill-switch efficacy for systemic liquidity swarms.
- **Incident T2 Drill:** Execute `simulate_incident.py` to verify latency gating under PACIFIC_SHIELD.
- **Homeostasis:** Run `simulate_civilizational_homeostasis.py` to verify long-term equilibrium monitoring.

## 5. Acceptance & Compliance Verification
1. **Conformity Dossier:** Generate the `RSP_V8_ULTIMATE_CONFORMITY.xml`.
2. **OSCAL Validation:** Verify the `OSCAL_GSIFI_CATALOG_V8.json` against the NIST 1.1.2 schema.
3. **Executive Dashboard:** Verify real-time G-SRI and attestation status on the `GovernanceDashboard.tsx`.

---
**Status:** OPERATIONAL RUNBOOK v1.2.0
**Custodian:** Jules
