.. aimms:set:: CurrentSolver

.. _CurrentSolver:

CurrentSolver
=============

The predefined element parameter :aimms:set:`CurrentSolver` contains, for every
mathematical programming type, the name of the solver that AIMMS will
currently use to solve models of that type.

.. code-block:: aimms

        ElementParameter CurrentSolver {
            IndexDomain  :  IndexMathematicalProgrammingTypes;
            Range        :  AllSolvers;
        }

Definition
----------

    The contents of the element parameter :aimms:set:`CurrentSolver` are, for all
    types of mathematical programs, the names of the currently active solver
    for solving mathematical programs of each type, as set through the
    **Solver Configuration** dialog box.

Updatability
------------

    The value of :aimms:set:`CurrentSolver` can also be modified programmatically
    from within an AIMMS model, and then determines the solver that will be
    used to solve subsequent problems of the specified type. Modifying the
    values of :aimms:set:`CurrentSolver` will, however, not modify the (default)
    settings in the **Solver Configuration** dialog box, that will be loaded
    at startup.

.. note::

    -  The procedure :aimms:func:`GMP::Instance::Solve` takes :aimms:set:`CurrentSolver`
       into account unless a solver has been assigned using the procedure
       :aimms:func:`GMP::Instance::SetSolver`.

    -  The procedures :aimms:func:`GMP::SolverSession::Execute` and
       :aimms:func:`GMP::SolverSession::AsynchronousExecute` take :aimms:set:`CurrentSolver`
       into account unless a solver has been assigned using the function
       :aimms:func:`GMP::Instance::CreateSolverSession` or the procedure
       :aimms:func:`GMP::Instance::SetSolver`.

.. seealso::

    -  The sets :aimms:set:`AllMathematicalProgrammingTypes` and :aimms:set:`AllSolvers`.

    -  Solver configuration is discussed in full detail in :doc:`miscellaneous/project-settings-and-options/solver-configuration`.
