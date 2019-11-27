.. aimms:procedure:: GMP::Solution::RetrieveFromSolverSession(solverSession, solution)

.. _GMP::Solution::RetrieveFromSolverSession:

GMP::Solution::RetrieveFromSolverSession
========================================

The procedure :aimms:func:`GMP::Solution::RetrieveFromSolverSession` stores the
solution from a solver session into the solution repository of a
generated mathematical program.

.. code-block:: aimms

    GMP::Solution::RetrieveFromSolverSession(
         solverSession,  ! (input) a solver session
         solution        ! (input) a solution
         )

Arguments
---------

    *solverSession*
        An element in the set :aimms:set:`AllSolverSessions`.

    *solution*
        An integer scalar reference to a solution.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  For a solver session belonging to a GMP with type MIP, this procedure
       retrieves the best integer solution found by so far (i.e., the
       incumbent), except when this procedure is called inside a **branch**,
       **cut**, **heuristic** or **lazy constraint** callback. In that case
       this procedure retrieves the LP solution of the current node
       (**branch**, **cut**, **heuristic**) or an integer feasible solution
       (**lazy constraint**).

    -  The function ``GMP::SolverSession::GetNodeObjective`` can be used to
       get the objective value corresponding to the solution retrieved with
       this procedure inside a **branch**, **candidate**, **cut**,
       **heuristic** or **lazy constraint** callback.

    -  By using the procedure ``GMP::SolverSession::RejectIncumbent`` the
       incumbent solution can be rejected inside a **candidate** callback.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::SetCallbackAddCut`, :aimms:func:`GMP::Instance::SetCallbackAddLazyConstraint`, :aimms:func:`GMP::Instance::SetCallbackBranch`, :aimms:func:`GMP::Instance::SetCallbackCandidate`,
    :aimms:func:`GMP::Instance::SetCallbackHeuristic`, :aimms:func:`GMP::Solution::SendToSolverSession`, :aimms:func:`GMP::Solution::RetrieveFromModel`, :aimms:func:`GMP::Solution::SendToModel`, :aimms:func:`GMP::SolverSession::GetNodeObjective` and :aimms:func:`GMP::SolverSession::RejectIncumbent`.
