# PQC-WORM Architecture Deep Dive: Multi-Algorithm Immutability

## 1. Hybrid Signature Scheme
To protect against future quantum adversaries, the Sentinel stack implements a hybrid signature scheme (FIPS 204 compliant):
- **ML-DSA-65:** Fast, low-overhead signing for per-turn reasoning traces.
- **ML-DSA-87 (CRYSTALS-Dilithium):** High-assurance signing for batch proof committals.
- **SPHINCS+:** Stateless hash-based signatures for the long-term anchoring of the GDL Master Canon.

## 2. Kafka-S3 Ingestion Pipeline
1. **Sidecar:** Emits a frame signed with ML-DSA-65.
2. **Relayer:** Batches 1000 frames and appends a CRYSTALS-Dilithium signature.
3. **Kafka (MSK):** Ensures exactly-once delivery via transactional producers.
4. **S3 Object Lock:** Final persistence in a bucket with `COMPLIANCE` mode enabled and a 10-year retention period.

---
**Status:** CRYPTOGRAPHIC ARCHITECTURE v1.2.0
