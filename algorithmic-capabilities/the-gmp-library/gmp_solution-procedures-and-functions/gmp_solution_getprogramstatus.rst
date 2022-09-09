.. aimms:function:: GMP::Solution::GetProgramStatus(GMP, solution)

.. _GMP::Solution::GetProgramStatus:

GMP::Solution::GetProgramStatus
===============================

The function :aimms:func:`GMP::Solution::GetProgramStatus` retrieves the program
status of a solution in the solution repository of a generated
mathematical program.

.. code-block:: aimms

    GMP::Solution::GetProgramStatus(
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

    The program status is only available if the solution has been retrieved
    from the solver, or if the procedure :aimms:func:`GMP::Solution::SetProgramStatus`
    has been called before.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Solution::GetSolverStatus`, :aimms:func:`GMP::Solution::GetObjective` and :aimms:func:`GMP::Solution::SetProgramStatus`.
