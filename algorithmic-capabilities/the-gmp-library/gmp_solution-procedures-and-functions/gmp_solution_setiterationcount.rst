.. aimms:procedure:: GMP::Solution::SetIterationCount(GMP, solution, iterationCount)

.. _GMP::Solution::SetIterationCount:

GMP::Solution::SetIterationCount
================================

The procedure :aimms:func:`GMP::Solution::SetIterationCount` sets the iteration
count of a solution in the solution repository of a generated
mathematical program.

.. code-block:: aimms

    GMP::Solution::SetIterationCount(
         GMP,            ! (input) a generated mathematical program
         solution,       ! (input) a solution
         iterationCount  ! (input) iteration count
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *solution*
        An integer scalar reference to a solution.

    *iterationCount*
        An integer scalar.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::SolverSession::GetIterationsUsed` and :aimms:func:`GMP::Solution::SetProgramStatus`.
