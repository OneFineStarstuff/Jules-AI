--------------------------- MODULE AGI_Containment_Kernel ---------------------------
EXTENDS Naturals, Sequences, FiniteSets

VARIABLES
    agent_state,      \* {EXECUTING, SUSPENDED, TERMINATED}
    network_boundary, \* {LOCAL_MESH, PUBLIC_INTERNET}
    kill_switch,      \* {ARMED, TRIGGERED}
    drift_score,      \* 0 to 100 (CDI equivalent)
    merkle_root       \* Latest commitment hash

Vars == <<agent_state, network_boundary, kill_switch, drift_score, merkle_root>>

Init ==
    /\ agent_state = "SUSPENDED"
    /\ network_boundary = "LOCAL_MESH"
    /\ kill_switch = "ARMED"
    /\ drift_score = 0
    /\ merkle_root = "0x0"

\* Meta-Invariant MI-1: Non-Escapement
NonEscapement ==
    agent_state = "EXECUTING" => network_boundary = "LOCAL_MESH"

\* Meta-Invariant MI-2: Homeostatic Stability
StabilityBounds ==
    drift_score < 15 => agent_state /= "TERMINATED"

\* Transition: Execute Turn
ExecuteTurn(new_drift, new_root) ==
    /\ agent_state = "EXECUTING"
    /\ kill_switch = "ARMED"
    /\ new_drift < 15
    /\ agent_state' = "EXECUTING"
    /\ drift_score' = new_drift
    /\ merkle_root' = new_root
    /\ UNCHANGED <<network_boundary, kill_switch>>

\* Transition: SEV-0 Trigger (IRMI)
TriggerHardKill ==
    /\ (drift_score >= 15 \/ network_boundary = "PUBLIC_INTERNET")
    /\ kill_switch' = "TRIGGERED"
    /\ agent_state' = "TERMINATED"
    /\ UNCHANGED <<network_boundary, drift_score, merkle_root>>

Next ==
    \/ (\E d \in 0..14, r \in {"0x1", "0x2"} : ExecuteTurn(d, r))
    \/ TriggerHardKill

Spec == Init /\ [][Next]_Vars

\* Safety Property: The agent never executes outside the mesh
Safety == []NonEscapement

\* Liveness Property: If drift exceeds 15, the agent eventually terminates
Liveness == drift_score >= 15 ~> agent_state = "TERMINATED"

=============================================================================
