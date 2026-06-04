--------------------------- MODULE SentinelContainmentProtocol ---------------------------
EXTENDS Integers, Sequences

VARIABLES state, risk_level, lock_active

Invariants == {"IDLE", "RUNNING", "HALTED", "LOCKED"}

TypeOK ==
    /\ state \in Invariants
    /\ risk_level \in 0..100
    /\ lock_active \in {TRUE, FALSE}

Init ==
    /\ state = "IDLE"
    /\ risk_level = 0
    /\ lock_active = FALSE

Monitor ==
    /\ state = "IDLE"
    /\ state' = "RUNNING"
    /\ UNCHANGED <<risk_level, lock_active>>

DetectAnomaly ==
    /\ state = "RUNNING"
    /\ risk_level' \in 0..100
    /\ UNCHANGED <<state, lock_active>>

TriggerIRMI ==
    /\ state = "RUNNING"
    /\ risk_level > 85
    /\ state' = "LOCKED"
    /\ lock_active' = TRUE
    /\ UNCHANGED <<risk_level>>

=============================================================================
