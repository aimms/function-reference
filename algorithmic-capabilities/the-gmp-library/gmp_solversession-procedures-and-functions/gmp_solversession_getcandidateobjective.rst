.. aimms:function:: GMP::SolverSession::GetCandidateObjective(solverSession)

.. _GMP::SolverSession::GetCandidateObjective:

GMP::SolverSession::GetCandidateObjective
=========================================

The function :aimms:func:`GMP::SolverSession::GetCandidateObjective` returns the
objective value of a candidate solution during MIP optimization from
within a candidate or lazy constraint callback.

.. code-block:: aimms

    GMP::SolverSession::GetCandidateObjective(
         solverSession     ! (input) a solver session
         )

Arguments
---------

    *solverSession*
        An element in the set :aimms:set:`AllSolverSessions`.

Return Value
------------

    In case of success, the objective value at the current node. Otherwise
    it returns ``UNDF``.

.. note::

    -  This function has only meaning for solver sessions belonging to a GMP
       with type MIP, MIQP or MIQCP.

    -  This function can only be used inside a **candidate** or **lazy
       constraint** callback.

    -  The procedure ``GMP::Solution::RetrieveFromSolverSession`` can be
       used to retrieve a candidate solution inside a **candidate** or
       **lazy constraint** callback.

    -  This function is only supported by CPLEX and Gurobi. Please note that
       the **candidate** callback is not supported by Gurobi.

.. seealso::

    The routines :aimms:func:`GMP::Instance::SetCallbackAddLazyConstraint`, :aimms:func:`GMP::Instance::SetCallbackCandidate` and :aimms:func:`GMP::Solution::RetrieveFromSolverSession`.
