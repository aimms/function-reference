.. aimms:procedure:: GMP::Solution::SetProgramStatus(GMP, solution, status)

.. _GMP::Solution::SetProgramStatus:

GMP::Solution::SetProgramStatus
===============================

The procedure :aimms:func:`GMP::Solution::SetProgramStatus` sets the program
status of a solution in the solution repository of a generated
mathematical program.

.. code-block:: aimms

    GMP::Solution::SetProgramStatus(
         GMP,            ! (input) a generated mathematical program
         solution,       ! (input) a solution
         status          ! (input) a status
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *solution*
        An integer scalar reference to a solution.

    *status*
        An element in the set :aimms:set:`AllSolutionStates`.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Solution::GetProgramStatus` and :aimms:func:`GMP::Solution::SetSolverStatus`.
