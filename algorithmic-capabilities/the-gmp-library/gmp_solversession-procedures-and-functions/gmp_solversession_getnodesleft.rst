.. aimms:function:: GMP::SolverSession::GetNodesLeft(solverSession)

.. _GMP::SolverSession::GetNodesLeft:

GMP::SolverSession::GetNodesLeft
================================

The function :aimms:func:`GMP::SolverSession::GetNodesLeft` returns the number of
unexplored nodes left in the branch-and-bound tree for a solver session.

.. code-block:: aimms

    GMP::SolverSession::GetNodesLeft(
         solverSession   ! (input) a solver session
         )

Arguments
---------

    *solverSession*
        An element in the set :aimms:set:`AllSolverSessions`.

Return Value
------------

    The number of unexplored nodes left in the branch-and-bound tree.

.. note::

    -  This function has only meaning for solver sessions belonging to a GMP
       with type MIP, MIQP or MIQCP.

    -  This function can be used inside a **branch**, **candidate**, **cut**
       or **heuristic** callback.

    -  This function is only supported by CPLEX and GUROBI.

.. seealso::

    The routines :aimms:func:`GMP::Instance::SetCallbackAddCut`, :aimms:func:`GMP::Instance::SetCallbackBranch`, :aimms:func:`GMP::Instance::SetCallbackCandidate`, :aimms:func:`GMP::Instance::SetCallbackHeuristic`, :aimms:func:`GMP::SolverSession::GetNodeNumber` and
    :aimms:func:`GMP::SolverSession::GetNodesUsed`.
