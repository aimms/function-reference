.. aimms:function:: GMP::Solution::GetSolverStatus(GMP, solution)

.. _GMP::Solution::GetSolverStatus:

GMP::Solution::GetSolverStatus
==============================

The function :aimms:func:`GMP::Solution::GetSolverStatus` retrieves the solver
status of a solution in the solution repository of a generated
mathematical program.

.. code-block:: aimms

    GMP::Solution::GetSolverStatus(
         GMP,            ! (input) a generated mathematical program
         solution        ! (input) a solution
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *solution*
        An integer scalar reference to a solution.

Return Value
------------

    An element in the set :aimms:set:`AllSolutionStates`.

.. note::

    The solver status is only available if the solution has been retrieved
    from the solver, or if the procedure ``GMP::Solution::SetSolverStatus``
    has been called before.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Solution::GetProgramStatus` and :aimms:func:`GMP::Solution::GetObjective` and :aimms:func:`GMP::Solution::SetSolverStatus`.
