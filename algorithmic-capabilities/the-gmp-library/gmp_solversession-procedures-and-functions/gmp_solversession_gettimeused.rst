.. aimms:function:: GMP::SolverSession::GetTimeUsed(solverSession)

.. _GMP::SolverSession::GetTimeUsed:

GMP::SolverSession::GetTimeUsed
===============================

The function :aimms:func:`GMP::SolverSession::GetTimeUsed` returns the elapsed
time (in 1/100th seconds) needed to execute a solver session.

.. code-block:: aimms

    GMP::SolverSession::GetTimeUsed(
         solverSession   ! (input) a solver session
         )

Arguments
---------

    *solverSession*
        An element in the set :aimms:set:`AllSolverSessions`.

Return Value
------------

    The number of 1/100th seconds used to execute a solver session.

.. seealso::

    - The routines :aimms:func:`GMP::Instance::SetTimeLimit`, :aimms:func:`GMP::SolverSession::Execute`, :aimms:func:`GMP::SolverSession::GetIterationsUsed` and :aimms:func:`GMP::SolverSession::GetMemoryUsed`.
