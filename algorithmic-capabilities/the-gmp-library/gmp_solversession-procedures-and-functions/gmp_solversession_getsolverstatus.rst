.. aimms:function:: GMP::SolverSession::GetSolverStatus(solverSession)

.. _GMP::SolverSession::GetSolverStatus:

GMP::SolverSession::GetSolverStatus
===================================

The function :aimms:func:`GMP::SolverSession::GetSolverStatus` returns the solver
status of the last execution of a solver session.

.. code-block:: aimms

    GMP::SolverSession::GetSolverStatus(
         solverSession   ! (input) a solver session
         )

Arguments
---------

    *solverSession*
        An element in the set :aimms:set:`AllSolverSessions`.

Return Value
------------

    An element in the set :aimms:set:`AllSolutionStates`.

.. seealso::

    - The routines :aimms:func:`GMP::SolverSession::Execute` and :aimms:func:`GMP::SolverSession::GetProgramStatus`.
