# Zero-Knowledge (zk-SNARK) Access Control for AGI Enclaves
## Security Standard: PRIV-ZK-001

## 1. Overview
To maintain privacy while ensuring strict authorization for AGI inference, the institution utilizes zk-SNARKs (Zero-Knowledge Succinct Non-Interactive Arguments of Knowledge). This allows a user (the Prover) to prove they possess a valid CAIO-signed authorization token without revealing the token's specific attributes or their identity to the AGI model (the Verifier).

## 2. Technical Implementation
*   **Circuit Construction:** The Circom circuit verifies the signature of the authorization token and the inclusion of a 'ClearanceLevel' attribute >= required threshold.
*   **Prover:** Generates a proof on the client-side or within a secure TEE (Nitro Enclave) before initiating a request.
*   **Verifier:** Integrated into the Sentinel sidecar (`src/governance-sidecar/app.js`). It verifies the proof in <10ms before allowing the request to hit the Reasoning Kernel.
*   **Nullifiers:** Used to prevent replaying a valid proof across different TraceIDs.

## 3. Compliance Alignment
*   **GDPR:** Minimizes PII exposure to the model and audit logs.
*   **EU AI Act (Art 15):** Enhances cybersecurity by preventing token-theft-based lateral movement into AGI enclaves.

---

# Deterministic Audit Replay Specification
## Forensic Standard: FOR-REPLAY-001

## 1. Objective
Enable regulators (PRA/FCA/MAS) to "replay" any AGI reasoning path to verify if institutional policies were violated.

## 2. Replay Artifacts (RSP v3.0)
The following artifacts from the Kafka WORM log are required for a deterministic replay:
1.  **Model Hash:** Exact signed weight hash (SHA-256).
2.  **Hyperparameter Lock:** Verified values for temperature, top_p, etc.
3.  **Recursive Context Envelope (RCE):** The Merkle-DAG chain of prior turns and retrieved documents.
4.  **Rego Policy Version:** The exact OPA policy hash active at the time of the decision.
5.  **Randomness Seed:** (If applicable) The seed used for non-deterministic sampling, though G-SIFIs mandate a seed=0 for critical operations.

## 3. Replay Workflow
1.  **Isolation:** Spin up a Nitro Enclave with the specified Model Hash.
2.  **Injection:** Load the RCE and Rego Policy into the enclaved sidecar.
3.  **Execution:** Run the original prompt under the locked hyperparameters.
4.  **Verification:** Compare the replayed output hash with the original Audit Log hash. Any mismatch triggers an `AUDIT_INTEGRITY_FAILURE` SEV-1 event.

---
*Authorized for G-SIFI Tier 1 Forensic Operations*
