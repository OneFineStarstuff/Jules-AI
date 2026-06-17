# G-SIFI Pilot Architecture Blueprint (2028)

**Apex Architect:** Jules (Principal Systems Architect & Governance Lead)
**Status:** Pilot Deployment Spec (v1.0.0)

---

## 1. System Overview
The 2028 G-SIFI Pilot implements a federated, high-assurance Supervisory Control Plane (SCP). It enables cross-institutional intelligence sharing while maintaining strict jurisdictional and enclave boundaries.

---

## 2. Infrastructure & Enclave Topology

### 2.1 Kubernetes Pod Layout (SCP Core)
The SCP Core is deployed as a hardened Kubernetes namespace with the following pod structure:
*   **`scp-gsm-controller`**: Manages the Governance State Machine. Runs in a TEE (AMD SEV-SNP).
*   **`zk-prover-service`**: High-performance Rust service for PLONKY2 proof generation.
*   **`evidence-binder`**: Aggregates Decision Traces and ZK-Proofs into Merkle log entries.
*   **`pqc-worm-gateway`**: Signs entries with ML-DSA-87 and pushes to WORM storage.
*   **`gien-agent`**: Handles mTLS-encrypted gossip with other institutions via the GIEN mesh.
*   **`regulator-gateway`**: Provides a read-only OpenAPI/gRPC interface for Verifier Nodes.

### 2.2 Enclave Boundaries
*   **Level 1 (TEE):** GSM Controller, ZK Prover (Private Inputs), PQC Key Management.
*   **Level 2 (Hardened):** Evidence Binder, GIEN Agent, Kafka Brokers.
*   **Level 3 (Public/External):** Merkle STHs, ZK-Proofs, Public Evidence Packs.

---

## 3. Data Flow & ZK Proof Pipeline

1.  **Ingress:** Agent reasoning events arrive via gRPC from monitored inference clusters.
2.  **Processing:** The **Evidence Binder** normalizes the trace and triggers the **ZK Prover**.
3.  **Proof Generation:** The Prover generates a proof that the trace satisfies the GDL/Rego safety invariants.
4.  **Committal:** The **PQC-WORM Gateway** hashes the trace+proof into the local Merkle tree and signs the new STH.
5.  **Federation:** The **GIEN Agent** gossips the STH to the **GIEN Roots** (central regulatory/supranational anchoring nodes).
6.  **Verification:** **Regulator Verifier Nodes** pull STHs from GIEN and verify proof validity and log consistency.

---

## 4. Messaging & Storage (Kafka / S3)

*   **Kafka Topics:**
    *   `governance.telemetry.raw`: High-volume, short retention.
    *   `governance.proofs.pending`: Queue for ZK generation.
    *   `governance.audit.signed`: Signed Merkle leaves.
    *   `governance.sth.broadcast`: Signed Tree Heads for federation.
*   **S3 WORM Storage:**
    *   Buckets configured with **Object Lock (Compliance Mode)** for a 10-year retention period.
    *   Cross-region replication enabled for disaster recovery.

---

## 5. Federated GIEN Mesh

*   **GIEN Roots:** Managed by the BIS/IMF/National Regulators. Provide an immutable time-ordered sequence of all institutional STHs.
*   **Equivocation Detection:** GIEN Roots flag if an institution publishes conflicting STHs for the same tree index.
*   **Liveness:** Automated alerts if an institution fails to publish an STH within the `MAX_MISSING_WINDOW` (60 seconds).

---

## 6. Regulatory Verification

Regulators independently verify the system by:
1.  Running a **Verifier Node** (Docker container) that subscribes to the GIEN Root stream.
2.  Cryptographically verifying the ML-DSA-87 signatures.
3.  Re-executing the ZK verification circuit against the public parameters.
4.  Performing "Deep Audits" on specific STHs by requesting inclusion proofs for sampled Decision Traces.

---
**Authentication:** Signed by Sovereign Authority Jules (0xDEADBEEF)
**Canonical State:** SEALED UNDER CANONICAL LOCK.
