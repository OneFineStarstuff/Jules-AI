--------------------------- MODULE AGI_Containment_Kernel ---------------------------
EXTENDS Integers, Sequences, Reals

VARIABLES drift_rate, containment_state, irmi_trigger

MetaInvariants ==
    /\ drift_rate < 0.15  (* MI-2: Homeostatic Stability *)
    /\ containment_state = "ENCLOSED" (* MI-1: Non-Escapement *)

Init ==
    /\ drift_rate = 0.0
    /\ containment_state = "ENCLOSED"
    /\ irmi_trigger = FALSE

Step ==
    /\ drift_rate' \in { d \in {0.01 * x : x \in 0..20} : TRUE }
    /\ IF drift_rate' >= 0.15 THEN irmi_trigger' = TRUE ELSE irmi_trigger' = irmi_trigger
    /\ UNCHANGED <<containment_state>>

=============================================================================
