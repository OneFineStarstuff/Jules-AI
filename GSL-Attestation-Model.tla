---------------- MODULE GSL_Attestation_Model ----------------
EXTENDS Naturals, Sequences

VARIABLES enclaves, mesh_state

\* Constants representing Enclave states
CONSTANT SUCCESS, FAILURE, UNKNOWN

\* Type invariant
TypeOK == enclaves \in [1..5 -> {SUCCESS, FAILURE, UNKNOWN}]

\* Initial state: all enclaves start as UNKNOWN
Init == enclaves = [i \in 1..5 |-> UNKNOWN]

\* State Transition: Enclave performs local attestation
Attest(i) == /\ enclaves[i] = UNKNOWN
             /\ enclaves' = [enclaves EXCEPT ![i] = SUCCESS]

\* Mesh Consensus: Transition to COMPLIANT if majority (3/5) are SUCCESS
Consensus == /\ \A i \in 1..5 : enclaves[i] \in {SUCCESS, FAILURE}
             /\ IF (Cardinality({i \in 1..5 : enclaves[i] = SUCCESS}) >= 3)
                THEN mesh_state = "COMPLIANT"
                ELSE mesh_state = "NON_COMPLIANT"

Next == \E i \in 1..5 : Attest(i)
--------------------------------------------------------------
