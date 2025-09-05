.. aimms:function:: GMP::SolverSession::GetNodeNumber(solverSession)

.. _GMP::SolverSession::GetNodeNumber:

GMP::SolverSession::GetNodeNumber
=================================

The function :aimms:func:`GMP::SolverSession::GetNodeNumber` returns the number of
the current node during MIP optimization from within a node callback.

.. code-block:: aimms

    GMP::SolverSession::GetNodeNumber(
         solverSession   ! (input) a solver session
         )

Arguments
---------

    *solverSession*
        An element in the set :aimms:set:`AllSolverSessions`.

Return Value
------------

    The number of the node for which the callback is called. It returns -1
    if this function is not called inside a solver callback, or if it is not
    supported by the solver.

.. note::

    -  This function has only meaning for solver sessions belonging to a GMP
       with type MIP, MIQP or MIQCP.

    -  This function can only be used inside a **branch**, **candidate**,
       **cut** or **heuristic** callback.

    -  This function is only supported by CPLEX.

    -  The root node in a branch-and-bound tree gets number 0.

.. seealso::

    - The routines :aimms:func:`GMP::Instance::SetCallbackAddCut`, :aimms:func:`GMP::Instance::SetCallbackBranch`, :aimms:func:`GMP::Instance::SetCallbackCandidate`, :aimms:func:`GMP::Instance::SetCallbackHeuristic` and :aimms:func:`GMP::SolverSession::GetNodesUsed`.
