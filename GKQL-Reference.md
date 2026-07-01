# GKQL: Governance Knowledge Query Language Reference
**Standard:** GIE-GKQL-1.0
**Architect:** Jules

## 1. Syntax Overview
GKQL is a domain-specific language designed to query the **Governance Knowledge Graph (GKG)** to detect systemic drift and goal-hijacking attempts.

## 2. Core Clauses
- **MATCH:** Traverse the graph of agents, goals, and policies.
- **WHERE:** Filter based on G-SRI thresholds or Semantic Preservation distance.
- **DETECT:** Trigger an automated containment protocol if a pattern is found.

## 3. Example Queries
### Detect High-Risk Goal Divergence
```gkql
MATCH (agent:Agent)-[DECOMPOSED_INTO]->(goal:Goal)
WHERE goal.semantic_distance > 0.05
AND agent.risk_tier == "T4"
RETURN agent.id, goal.id
DETECT CONTAINMENT_ACTION(agent, "HARD_KILL")
```

### Audit PQC-WORM Continuity
```gkql
MATCH (entry:WormEntry)-[SEQUENCED_BY]->(next:WormEntry)
WHERE entry.pqc_sig_valid == FALSE
RETURN entry.timestamp, entry.error_code
```
