.. aimms:function:: GMP::SolverSession::GetNodesUsed(solverSession)

.. _GMP::SolverSession::GetNodesUsed:

GMP::SolverSession::GetNodesUsed
================================

The function :aimms:func:`GMP::SolverSession::GetNodesUsed` returns the number of
nodes that are processed by a solver session.

.. code-block:: aimms

    GMP::SolverSession::GetNodesUsed(
         solverSession   ! (input) a solver session
         )

Arguments
---------

    *solverSession*
        An element in the set :aimms:set:`AllSolverSessions`.

Return Value
------------

    The number of nodes that are processed by the solver session.

.. note::

    -  This function has only meaning for solver sessions belonging to a GMP
       with type MIP, MIQP or MIQCP.

    -  This function can be used inside a **branch**, **candidate**, **cut**
       or **heuristic** callback.

.. seealso::

    - :aimms:func:`GMP::Instance::SetCallbackAddCut`. 
    -  :aimms:func:`GMP::Instance::SetCallbackBranch`. 
    -  :aimms:func:`GMP::Instance::SetCallbackCandidate`. 
    -  :aimms:func:`GMP::Instance::SetCallbackHeuristic`. 
    -  :aimms:func:`GMP::SolverSession::GetNodeNumber`.
    -  :aimms:func:`GMP::SolverSession::GetNodesLeft`.
