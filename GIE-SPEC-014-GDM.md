# GIE-SPEC-014: Governance Data Model (GDM)
**Version:** 1.0.0
**Architect:** Jules
**Status:** CANONICAL SPECIFICATION

## 1. Relational Schema
Telemetry is stored in a time-series relational database for high-throughput querying.

### 1.1 Table: telemetry_events
- **id:** UUID (PK)
- **timestamp:** TIMESTAMPTZ
- **agent_id:** STRING
- **gsri_score:** FLOAT
- **cdi_score:** FLOAT
- **pqc_signature:** TEXT
- **pcr_attestation:** TEXT

## 2. Vector Schema
Agentic intent and goal-decompositions are stored in a vector space for semantic drift analysis.

### 2.1 Collection: goal_intent_vectors
- **goal_id:** STRING
- **intent_vector:** VECTOR(1536)
- **policy_anchor_id:** STRING
- **metadata:** JSONB

## 3. Data Protection (GDP) Integration
All GDM implementations must enforce GDP-tier classification at the field level, with T3/T4 data stored exclusively in confidential memory enclaves.
