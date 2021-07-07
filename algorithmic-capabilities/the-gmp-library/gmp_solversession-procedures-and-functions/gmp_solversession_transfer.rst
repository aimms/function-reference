.. aimms:procedure:: GMP::SolverSession::Transfer(solverSession, GMP)

.. _GMP::SolverSession::Transfer:

GMP::SolverSession::Transfer
============================

| The procedure :aimms:func:`GMP::SolverSession::Transfer` can be used to transfer
  a solver session from its current GMP to another similar GMP. Both
  GMPs should be created from the same symbolic math program.
|
| Currently this procedure is only supported for stochastic Benders
  decomposition.

.. code-block:: aimms

    GMP::SolverSession::Transfer(
         solverSession,  ! (input) a solver session
         GMP             ! (input) a generated mathematical program
         )

Arguments
---------

    *solverSession*
        An element in the set :aimms:set:`AllSolverSessions`.

    *GMP*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    If each GMP has its own solver session then more memory is required
    which might not be available for large models or if many GMPs are used.
    To save memory this procedure can be used since it allows similar GMPs
    to share one solver session. After transfering a solver session to a
    *GMP*, only the differences between the old and new GMP will be passed
    as updates to the solver.

.. seealso::

    The routines :aimms:func:`GMP::Instance::CreateSolverSession`, :aimms:func:`GMP::Instance::GenerateStochasticProgram` and :aimms:func:`GMP::Stochastic::BendersFindReference`.
