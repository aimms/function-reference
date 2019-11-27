.. aimms:procedure:: GMP::Solution::Copy(GMP, fromSolution, toSolution)

.. _GMP::Solution::Copy:

GMP::Solution::Copy
===================

The procedure :aimms:func:`GMP::Solution::Copy` copies one solution to another
solution in the solution repository of a generated mathematical program.

.. code-block:: aimms

    GMP::Solution::Copy(
         GMP,            ! (input) a generated mathematical program
         fromSolution,   ! (input) a solution
         toSolution      ! (input) a solution
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *fromSolution*
        An integer scalar reference to a solution.

    *toSolution*
        An integer scalar reference to a solution.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate` and :aimms:func:`GMP::Solution::Move`.
