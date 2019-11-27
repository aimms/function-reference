.. aimms:function:: GMP::SolverSession::GetProgramStatus(solverSession)

.. _GMP::SolverSession::GetProgramStatus:

GMP::SolverSession::GetProgramStatus
====================================

The function :aimms:func:`GMP::SolverSession::GetProgramStatus` returns the
program status of the last execution of a solver session.

.. code-block:: aimms

    GMP::SolverSession::GetProgramStatus(
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

    The routines :aimms:func:`GMP::SolverSession::Execute` and :aimms:func:`GMP::SolverSession::GetSolverStatus`.
