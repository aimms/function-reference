.. aimms:procedure:: GMP::Solution::Move(GMP, fromSolution, toSolution)

.. _GMP::Solution::Move:

GMP::Solution::Move
===================

The procedure :aimms:func:`GMP::Solution::Move` moves one solution to another
solution in the solution repository of a generated mathematical program.

.. code-block:: aimms

    GMP::Solution::Move(
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

.. note::

    After calling this procedure, the solution at position *fromSolution* in
    the solution repository will be empty. This is not the case if you use
    the procedure :aimms:func:`GMP::Solution::Copy`.

.. seealso::

    - The routines :aimms:func:`GMP::Instance::Generate` and :aimms:func:`GMP::Solution::Copy`.
