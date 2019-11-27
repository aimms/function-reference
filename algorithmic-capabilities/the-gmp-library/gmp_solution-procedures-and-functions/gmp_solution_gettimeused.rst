.. aimms:function:: GMP::Solution::GetTimeUsed(GMP, solution)

.. _GMP::Solution::GetTimeUsed:

GMP::Solution::GetTimeUsed
==========================

The function :aimms:func:`GMP::Solution::GetTimeUsed` returns the elapsed time (in
1/100th seconds) used to create a solution in the solution repository of
a generated mathematical program.

.. code-block:: aimms

    GMP::Solution::GetTimeUsed(
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

    The number of 1/100th seconds used to create a solution.

.. seealso::

    The procedure :aimms:func:`GMP::Instance::SetTimeLimit`.
