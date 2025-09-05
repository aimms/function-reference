.. aimms:procedure:: GMP::Instance::SetSolver(GMP, solver)

.. _GMP::Instance::SetSolver:

GMP::Instance::SetSolver
========================

The procedure :aimms:func:`GMP::Instance::SetSolver` can be used to select for a
generated mathematical program the solver to be called in subsequent
calls to :aimms:func:`GMP::Instance::Solve`.

.. code-block:: aimms

    GMP::Instance::SetSolver(
         GMP,            ! (input) a generated mathematical program
         solver          ! (input) a solver
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *solver*
        An element in the set :aimms:set:`AllSolvers`.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    The solver set in this procedure will also be assigned to any solver
    session created with the function :aimms:func:`GMP::Instance::CreateSolverSession`
    for the *GMP*, unless the *Solver* argument in the procedure
    :aimms:func:`GMP::Instance::CreateSolverSession` is specified. Note that the
    procedure :aimms:func:`GMP::Instance::SetSolver` cannot be used to change the
    solver assigned to a solver session after
    :aimms:func:`GMP::Instance::CreateSolverSession` has been called.

.. seealso::

    - The routines :aimms:func:`GMP::Instance::CreateSolverSession`, :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::GetSolver` and :aimms:func:`GMP::Instance::Solve`.
