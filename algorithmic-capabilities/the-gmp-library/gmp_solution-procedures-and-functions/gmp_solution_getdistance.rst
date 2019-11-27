.. aimms:function:: GMP::Solution::GetDistance(GMP, solution1, solution2)

.. _GMP::Solution::GetDistance:

GMP::Solution::GetDistance
==========================

The function :aimms:func:`GMP::Solution::GetDistance` calculates the Euclidean
distance between the vectors of column level values in a first and
second solution of a generated mathematical program.

.. code-block:: aimms

    GMP::Solution::GetDistance(
         GMP,            ! (input) a generated mathematical program
         solution1,      ! (input) a solution
         solution2       ! (input) a solution
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *solution1*
        An integer scalar reference to a solution.

    *solution2*
        An integer scalar reference to a solution.

Return Value
------------

    In case of success, the Euclidean distance between both solutions.
    Otherwise it returns ``UNDF``.

.. note::

    The level value of the objective column (if any) is not used.
