.. aimms:function:: GMP::SolverSession::GetIterationsUsed(solverSession)

.. _GMP::SolverSession::GetIterationsUsed:

GMP::SolverSession::GetIterationsUsed
=====================================

The function :aimms:func:`GMP::SolverSession::GetIterationsUsed` returns the
number of iterations used by a solver session.

.. code-block:: aimms

    GMP::SolverSession::GetIterationsUsed(
         solverSession   ! (input) a solver session
         )

Arguments
---------

    *solverSession*
        An element in the set :aimms:set:`AllSolverSessions`.

Return Value
------------

    The number of iterations used by the solver session.

.. seealso::

    The routines :aimms:func:`GMP::SolverSession::Execute`, :aimms:func:`GMP::Instance::SetIterationLimit`, :aimms:func:`GMP::SolverSession::GetMemoryUsed` and :aimms:func:`GMP::SolverSession::GetTimeUsed`.
