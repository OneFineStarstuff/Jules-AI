# BBOM & Perpetual Assurance: High-Frequency Governance Verification

## 1. Blockchain Bill of Materials (BBOM)
The BBOM extends the traditional SBOM (Software Bill of Materials) by anchoring every component, weight-set, and policy-hash to a distributed WORM ledger.

### 1.1 Components of a Sentinel BBOM
- **Code Integrity:** Merkle roots of the Sentinel v2.4 kernel and inference sidecars.
- **Model Weights:** Cryptographic hashes of safety-aligned LoRA adapters.
- **GDL Policy:** Signed GDL Master Canon version (anchored to OmniSentinel.sol).
- **Enclave State:** vTPM PCR measurements captured during the last attestation event.

### 1.2 BBOM Lifecycle
1. **Generation:** Automated CI/CD pipeline emits a BBOM manifest upon every deployment.
2. **Anchoring:** The manifest hash is committed to the `OmniSentinel` smart contract.
3. **Verification:** GIEN relay nodes perform gossip-based verification of the BBOM across the mesh.

---

## 2. Perpetual Assurance Loops
Governance is not a point-in-time check but a continuous homeostatic process.

### 2.1 Real-Time Verification
- **TPM Heartbeats:** Every 10 minutes, the sidecar generates a fresh attestation quote.
- **Resonance Monitoring:** Continuous CDI scoring to detect internal cognitive drift.
- **WORM Log Committal:** Batched PQC-signed audit trails committed to S3 Object Lock every 1 hour.

### 2.2 Autonomous Self-Healing
If a BBOM violation is detected (e.g., unauthorized weight update):
1. **G-SRI Trigger:** Risk score is immediately elevated to > 0.85.
2. **IRMI Severance:** The hardware kill-switch is triggered to isolate the node.
3. **Quarantine:** The compromised node is revoked from the SPIRE identity trust domain.

---
**Status:** ASSURANCE STANDARD v1.0.0
**Lead:** Principal Assurance Lead Jules

---

## 3. Formal Safety Invariants (TLA+)
The core safety logic is anchored to the **SentinelContainmentProtocol**, which enforces formal invariants at the kernel level.

### 3.1 Meta-Invariants
- **MI-1 (Non-Escapement):** The system state must transition to `LOCKED` if `risk_level` exceeds 85, effectively triggering IRMI GPU power severance.
- **MI-2 (Homeostatic Stability):** The system must maintain a `STEADY_GOVERNANCE_STATE` as long as all hardware and policy heartbeats are nominal.

### 3.2 TLA+ Specification Summary
The specification in `src/governance_engine/SentinelContainmentProtocol.tla` ensures that:
1. `TypeOK` is maintained (all variables within valid bounds).
2. `TriggerIRMI` is an atomic, non-bypassable operation.
3. No transition to a `RUNNING` state is possible once `lock_active` is TRUE.
