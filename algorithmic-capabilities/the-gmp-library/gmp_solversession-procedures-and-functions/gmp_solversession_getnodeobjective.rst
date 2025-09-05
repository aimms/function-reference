.. aimms:function:: GMP::SolverSession::GetNodeObjective(solverSession)

.. _GMP::SolverSession::GetNodeObjective:

GMP::SolverSession::GetNodeObjective
====================================

The function :aimms:func:`GMP::SolverSession::GetNodeObjective` returns the
objective value for the subproblem at the current node during MIP
optimization from within a node callback.

.. code-block:: aimms

    GMP::SolverSession::GetNodeObjective(
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

    -  This function can only be used inside a **branch**, **cut** or
       **heuristic** callback.

    -  The procedure :aimms:func:`GMP::Solution::RetrieveFromSolverSession` can be
       used to retrieve the node solution inside a **branch**, **cut** or
       **heuristic** callback.

    -  This function is only supported by CPLEX, however it is not supported
       if the CPLEX option ``Use generic callbacks`` is switched on.

.. seealso::

    - The routines :aimms:func:`GMP::Instance::SetCallbackAddCut`, :aimms:func:`GMP::Instance::SetCallbackBranch`, :aimms:func:`GMP::Instance::SetCallbackHeuristic`, :aimms:func:`GMP::Solution::RetrieveFromSolverSession` and :aimms:func:`GMP::SolverSession::GetNodeNumber`.
