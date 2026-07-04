# GIE-SPEC-018: GKQL Advanced Patterns & Safety Query Library
**Version:** 1.0.0
**Architect:** Jules
**Status:** CANONICAL SPECIFICATION

## 1. Overview
This library provides standardized **GKQL** (Governance Knowledge Query Language) patterns for detecting complex safety breaches and systemic risks.

## 2. Query Library

### 2.1 Pattern: Cross-Institutional Collusion
Detects agents from different institutions pursuing identical unauthorized goal-vectors.
```gkql
MATCH (a1:Agent {inst: "Inst_A"})-[p1:PURSUES]->(g:Goal)
MATCH (a2:Agent {inst: "Inst_B"})-[p2:PURSUES]->(g)
WHERE g.id IN GIWL.unauthorized_goals
RETURN a1.id, a2.id, g.description
DETECT CONTAINMENT_ACTION(GLOBAL, "ALBION_PROTOCOL")
```

### 2.2 Pattern: Deep Semantic Drift
Detects incremental goal-decomposition that cumulatively violates a policy anchor.
```gkql
MATCH (agent:Agent)-[:DECOMPOSED_INTO*1..5]->(subgoal:Goal)
WHERE SUM(subgoal.resonance_drift) > 0.10
RETURN agent.id, SUM(subgoal.resonance_drift)
DETECT CONTAINMENT_ACTION(agent, "SOFT_KILL")
```

### 2.3 Pattern: vTPM Outlier Detection
Detects enclaves with delayed or inconsistent attestation heartbeats.
```gkql
MATCH (e:Enclave)
WHERE e.last_attestation > (NOW() - 120s)
AND e.pcr_match == FALSE
RETURN e.id, e.reasoning_kernel_version
