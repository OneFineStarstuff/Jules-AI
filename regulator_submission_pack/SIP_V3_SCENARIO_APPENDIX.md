# Scenario Appendix: SIP v3.0 TLA+ TLC Walkthroughs

This appendix details the model-checking scenarios verified using the formal specification in `src/governance_engine/SIP_v3_0_Protocol.tla`.

## Scenario 1: Normal Convergence (Honest Path)
- **Setup:** 2 Institutions, 2 Roots, MaxTreeSize=3.
- **Workflow:**
    1. Institution A publishes STH-1.
    2. Root 1 and Root 2 both gossip STH-1.
- **Verification:** `RootConvergence` invariant holds. `NoSilentDivergence` remains true.
- **Regulator View:** Verifier nodes see a consistent, growing log of Signed Tree Heads.

## Scenario 2: Equivocation Detection (Byzantine Institution)
- **Setup:** Institution A is Byzantine and attempts to fork its Merkle Log.
- **Workflow:**
    1. Institution A publishes STH-X to Root 1.
    2. Institution A publishes STH-Y (where X /= Y) to Root 2 for the same tree index.
- **Verification:**
    - The `GossipSTH` action detects the conflict via the `IsEquivocating` operator.
    - `system_state` transitions to `EQUIVOCATION_DETECTED`.
- **Regulator View:** Verifier nodes immediately flag the institution for non-compliance and trigger the `CONTINUATION_REFUSAL_STATE` in the SCP.

## Scenario 3: Missing Attestation (Silent Institution)
- **Setup:** Institution A stops publishing STHs.
- **Workflow:**
    1. `SkipWindow(A)` is called repeatedly.
    2. `observed_missing[A]` increments.
- **Verification:**
    - When `observed_missing[A] = MaxMissing`, `system_state` transitions to `MISSING_ATTESTATION`.
- **Regulator View:** Automated alerts notify the Sandbox Office that the institution's supervisory heartbeat has failed.

## Scenario 4: No Protocol Error
- **Verification:** `TypeOK` invariant ensures that no action leads to an undefined state or type violation, confirming the protocol's robustness.
