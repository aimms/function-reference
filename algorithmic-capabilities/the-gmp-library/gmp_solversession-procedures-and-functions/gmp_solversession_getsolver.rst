.. aimms:function:: GMP::SolverSession::GetSolver(solverSession)

.. _GMP::SolverSession::GetSolver:

GMP::SolverSession::GetSolver
=============================

The function :aimms:func:`GMP::SolverSession::GetSolver` returns the solver
belonging to a solver session.

.. code-block:: aimms

    GMP::SolverSession::GetSolver(
         solverSession     ! (input) a solver session
         )

Arguments
---------

    *solverSession*
        An element in the set :aimms:set:`AllSolverSessions`.

Return Value
------------

    The solver belonging to a solver session as an element of :aimms:set:`AllSolvers`.

.. note::

    Which solver is assigned to the solver session is determined by the
    routines ``GMP::Instance::CreateSolverSession`` and
    ``GMP::Instance::SetSolver``. Note that if the *Solver* argument of
    ``GMP::Instance::CreateSolverSession`` is used then it overrules
    ``GMP::Instance::SetSolver``.

.. seealso::

    The routines :aimms:func:`GMP::Instance::CreateSolverSession` and :aimms:func:`GMP::Instance::SetSolver`.
