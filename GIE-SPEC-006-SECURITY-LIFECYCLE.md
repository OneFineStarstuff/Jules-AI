# GIE-SPEC-006: Security & Lifecycle (GISM, GCPM, GSDL, GACF)
**Version:** 1.0.0
**Architect:** Jules
**Status:** CANONICAL SPECIFICATION

## 1. Governance Integrity Security Management (GISM)
**GISM** enforces the zero-trust substrate requirements for the Omni-Sentinel mesh.

### 1.1 Mandatory Standards
- **Inter-service:** gRPC + mTLS with SPIFFE IDs.
- **Identity:** X.509 SVIDs anchored in vTPM.
- **Tokens:** Minimal 32-byte (64 hex characters) cryptographic entropy.

## 2. Governance Compliance Policy Management (GCPM)
**GCPM** manages the lifecycle of OPA/Rego and GDL policy artifacts.

### 2.1 Policy Lifecycle
1. **Creation:** Narrative intent translated to GDL/Rego.
2. **Verification:** TLA+ model checking of policy invariants.
3. **Distribution:** GitOps-based rollout to GEE sidecars.
4. **Audit:** PQC-WORM logging of every policy hit/miss.

## 3. Governance Secure Development Lifecycle (GSDL)
**GSDL** defines the security standards for developing and deploying new governance agents.

### 3.1 GSDL Controls
- **Formalism:** All new agents must have a TLA+ specification.
- **Attestation:** Agents must be compiled for TEE execution (AMD SEV-SNP).
- **Scanning:** Mandatory CodeQL scanning for PII leakage and cryptographic weak-points.

## 4. Governance Automated Compliance Framework (GACF)
**GACF** performs continuous, real-time monitoring of institutional compliance.

### 4.1 Monitoring Invariants
- **Real-time:** Continuous OPA/Rego evaluation of agent transitions.
- **Auto-remediation:** GIRI-triggered containment upon G-SRI > 0.85.
- **Reporting:** Automated GIRS-Schema document generation for regulatory sinks.
