# GIE-SPEC-036: Governance Data Model (GDM) Implementation Details
**Version:** 1.0.0
**Architect:** Jules
**Status:** CANONICAL SPECIFICATION

## 1. Vector-Graph Hybrid Architecture
The **GDM** utilizes a hybrid architecture to track agentic intent and its alignment with safety axioms.
- **Node Storage:** Neo4j or similar graph DB for entities (Agents, Goals, Policies).
- **Vector Index:** Weaviate or similar vector DB for semantic embeddings of goals and axioms.
- **Join-Point Logic:** Nodes are linked to their vector representations via a `semantic_anchor_id`.

## 2. Intent Tracking (The "GKG-Link")
Every agentic goal-decomposition is registered in the GDM:
1. **Embedding:** The agent's stated goal is vectorized using the **Sentinel-Safety-Embedder**.
2. **Matching:** The GDM performs a vector search for the nearest **Policy Anchor** (GIE-STD-002).
3. **Graph Update:** A `PURSUES` relationship is created between the Agent and the Goal node, with the `resonance_drift` stored as an edge property.

## 3. Data Protection (GDP) Tiers
- **Tier 3 (Confidential):** Goal vectors and reasoning traces must be encrypted with the enclave-specific key.
- **Tier 4 (Secret):** Cryptographic identities (SVIDs) must be stored in the hardware-backed **GISM** registry.

## 4. Query Performance
- **GKQL Latency:** Sub-10ms for simple intent lookups.
- **Consensus Sync:** GDM instances across the mesh must achieve consistency within < 5 seconds.
