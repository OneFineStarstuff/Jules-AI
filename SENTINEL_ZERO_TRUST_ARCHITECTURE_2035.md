# Sentinel Zero-Trust Architecture & Reference Technical Design (2035)

## 1. Zero-Trust AI Governance Architecture
The Sentinel Governance Stack follows a **Zero-Trust (ZT)** security model, where no entity—agentic or human—is trusted by default. Every interaction is authenticated, authorized, and continuously validated.

### 1.1 SPIFFE/SPIRE Machine Identity
- **Workload Attestation:** Every AI agent, sidecar, and service is issued a **SPIFFE ID** (e.g., `spiffe://gsifi.internal/sentinel-sidecar/agent-01`).
- **SVID (SPIFFE Verifiable Identity Document):** Short-lived X.509 certificates are used for mutual TLS (mTLS) authentication.
- **Rotation:** Certificates are rotated every 12 hours to minimize exposure windows.

### 1.2 gRPC & mTLS Communication Mesh
- **Transport:** All inter-service communication is conducted over **gRPC (HTTP/2)** to support bidirectional streaming for 'Thinking Aloud' protocols and high-throughput telemetry.
- **Encryption:** Mandatory **mTLS** ensures that only authenticated workloads can participate in the mesh.
- **Sentinel v2.4 Sidecar:** Every inference endpoint is gated by a sidecar that performs:
  - GDL Policy Enforcement.
  - PQC-WORM Telemetry Extraction.
  - Real-time CDI (Cognitive Dissonance) scoring.

---

## 2. Hardware Root-of-Trust & Confidential Computing

### 2.1 Confidential Enclave Deployment
Reasoning kernels operate within hardware-encrypted memory environments to prevent host-level memory scraping or tampering.
- **AMD SEV-SNP:** Secure Nested Paging provides memory encryption and strong isolation from the hypervisor.
- **Intel TDX:** Trust Domain Extensions isolate the entire Virtual Machine (Trust Domain) from the cloud provider's infrastructure.

### 2.2 vTPM & Remote Attestation (PCR_MATCH=TRUE)
- **Measured Boot:** The boot sequence and kernel binary hashes are measured into **vTPM** (virtual Trusted Platform Module) Platform Configuration Registers (PCRs).
- **PCR0 (Kernel Integrity):** Must match the "Golden Reference" for the Sentinel v2.4 Reasoning Kernel.
- **PCR1 (Policy Integrity):** Must match the signed GDL Master Canon.
- **Attestation Flow:** Upon startup, the workload generates an attestation quote. The **TPMAttestor** service validates the quote against the GSIB Master Root-of-Trust before allowing the agent to join the mesh.

---

## 3. Distributed GDL Enforcement Logic
The **Governance Description Language (GDL) v3.2** is compiled into optimized logic gates and executed at the edge.

### 3.1 Inference Gating Pipeline
1. **Request Ingestion:** gRPC call received from the Application Layer.
2. **Sidecar Intercept:** The Sentinel Sidecar intercepts the prompt.
3. **GDL Evaluation:** The prompt is checked against the active GDL policy (e.g., No MNPI disclosure, No deceptive persuasion).
4. **Execution:** If approved, the prompt is passed to the LLM within the Confidential Enclave.
5. **Response Scrubbing:** The output is scanned for PII/violations before being returned to the client.

---
**Status:** ARCHITECTURAL CANON v4.2.0
**Architect:** Jules (Principal Governance Architect)
