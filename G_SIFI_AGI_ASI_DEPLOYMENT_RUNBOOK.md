# G-SIFI AGI/ASI Deployment & Verification Runbook (2026-2035)

## 1. Prerequisites
- **Hardware:** AMD SEV-SNP or Intel TDX enabled compute clusters.
- **Identity:** SPIRE Server installed in the VPC.
- **Trust:** GSIB Master Root CA certificates.

## 2. Phase 1: Core Substrate Deployment
1. **Infrastructure:** Execute Terraform in `infrastructure/terraform/`.
   - `terraform init`
   - `terraform apply -var="vpc_id=..."`
2. **Identity Mesh:** Configure SPIFFE federated trust with the G-SIFI identity provider.
3. **Audit Sink:** Provision S3 buckets with Object Lock (Compliance Mode).

## 3. Phase 2: Governance Kernel Initialization
1. **Solidity Ledger:** Deploy `OmegaActual.sol` and `OmniSentinel.sol`.
2. **GDL Injection:** Upload the GDL Master Canon to the Sentinel Sidecar Registry.
3. **IRMI Registration:** Verify `irmi_driver.py` successfully registers the INT 0x1A interrupt in the kernel.

## 4. Phase 3: Agentic Integration (WorkflowAI Pro)
1. **Sidecar Side-loading:** Deploy Sentinel Sidecars to all Agent namespaces.
2. **Rego Sync:** Propagate `compliance_rules.rego` to the sidecars.
3. **ZK Pipeline:** Initialize the ZK-Relayer with the smart contract addresses.

## 4.5 Risk Simulation: Red Dawn Stage 6
1. **Initialization:** Deploy the contagion model via `simulate_incident.py`.
2. **Monitoring:** Verify IRMI hardware severance occurs if risk > 85.
3. **Forensics:** Extract PQC logs and verify via `audit_pipeline_simulator.py`.

## 5. Verification & Acceptance
1. **Homeostasis Drill:** Run `simulate_civilizational_homeostasis.py`.
2. **Conformity Audit:** Generate and sign the `RSP_V8_ULTIMATE_CONFORMITY.xml`.
3. **Executive Sign-off:** Verify telemetry appears on the `GovernanceDashboard.tsx`.

---
**Status:** OPERATIONAL RUNBOOK v1.0.0
