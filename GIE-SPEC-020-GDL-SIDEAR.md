# GIE-SPEC-020: GDL Compiler & Enforcement Sidecar Specification
**Version:** 1.0.0
**Architect:** Jules
**Status:** CANONICAL SPECIFICATION

## 1. GDL Compiler Architecture
The **GDL Compiler** translates narrative policy into a binary format optimized for the **GEE** (Governance Enforcement Engine).
- **Frontend:** EBNF-based validation of GDL scripts.
- **Middle-end:** Invariant preservation check via TLA+ verification.
- **Backend:** Target generation for OPA/Rego and eBPF bytecode.

## 2. Enforcement Sidecar (GEE Sidecar)
The sidecar is a lightweight process injected into every agentic enclave.
- **Zero-Copy Gating:** Uses shared memory to perform inference-time safety scoring without data duplication.
- **Protocols:** Communication with the Supervisory Control Plane (SCP) via gRPC/mTLS.
- **Identity:** Sidecars are issued X.509 SVIDs anchored in the compute node's TPM.

## 3. Bytecode Gating (eBPF)
For sub-millisecond network/disk containment, the sidecar utilizes eBPF programs:
- **Redaction:** Automatic MNPI/PII scrubbing for outgoing network packets.
- **Traffic Shaping:** Rate-limiting agentic API calls upon Tier-2 drift detection.
- **Kill-Signal:** INT 0x1A hardware interrupt trigger for T4 breaches.
