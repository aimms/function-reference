.. aimms:procedure:: GMP::Solution::SendToSolverSession(solverSession, solution)

.. _GMP::Solution::SendToSolverSession:

GMP::Solution::SendToSolverSession
==================================

The procedure :aimms:func:`GMP::Solution::SendToSolverSession` initializes a
solver session with the values in the solution from the solution
repository of a generated mathematical program.

.. code-block:: aimms

    GMP::Solution::SendToSolverSession(
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

.. seealso::

    - The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Solution::RetrieveFromSolverSession`, :aimms:func:`GMP::Solution::RetrieveFromModel` and :aimms:func:`GMP::Solution::SendToModel`.
