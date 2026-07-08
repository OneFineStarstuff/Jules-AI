# GIE-SPEC-001: Technical Specification for GIRI and GEE
**Version:** 1.0.0
**Architect:** Jules
**Status:** CANONICAL SPECIFICATION

## 1. Governance Integrity Response Interface (GIRI)
GIRI is the standardized API surface for triggering containment actions across the Omni-Sentinel mesh.

### 1.1 Endpoint: /v1/containment/trigger
- **Method:** POST (mTLS required, SPIFFE ID authorized)
- **Payload:**
  ```json
  {
    "target_agent_id": "string",
    "action_tier": "T1-T4",
    "reason_code": "enum",
    "pcr_attestation": "base64",
    "auth_quorum_sig": "string"
  }
  ```
- **Actions:**
  - **PAUSE (T2):** Suspends execution state in TEE.
  - **SOFT_KILL (T3):** Terminate process, release non-critical resources.
  - **HARD_KILL (T4):** IRMI hardware power severance.

## 2. Governance Enforcement Engine (GEE)
The GEE is the low-latency, kernel-level executor for GDL logic gates.

### 2.1 Latency Requirements
- **Inference Gating:** < 0.5ms per token-gate.
- **State Transition Validation:** < 1.0ms per transition.
- **Containment Triggering:** < 0.1ms from threshold breach to GIRI call.

### 2.2 Execution Architecture
The GEE operates as a sidecar process within the confidential enclave, utilizing shared memory with the functional agent's inference engine to perform zero-copy safety scoring.

### 2.3 Formal Invariant
The GEE must maintain the following invariant at all times:
$$\forall t: G(t) > 0.85 \implies State(t+1) = CONTAINED$$
Where (t)$ is the real-time G-SRI score.
