.. aimms:procedure:: GMP::Solution::ConstructMean(GMP, solution1, solution2, weight)

.. _GMP::Solution::ConstructMean:

GMP::Solution::ConstructMean
============================

The procedure :aimms:func:`GMP::Solution::ConstructMean` constructs the weighted
average of two solutions of a generated mathematical program by using
the column level values in both solutions. The first solution is
replaced by the resulting mean solution.

.. code-block:: aimms

    GMP::Solution::ConstructMean(
         GMP,            ! (input) a generated mathematical program
         solution1,      ! (input) a solution
         solution2,      ! (input) a solution
         weight          ! (input) a scalar value
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *solution1*
        An integer scalar reference to a solution.

    *solution2*
        An integer scalar reference to a solution.

    *weight*
        The weight used for *solution1*.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    The *weight* argument defines the weight used for *solution1*; for
    *solution2* a weight of 1 is used. The constructed mean solution is
    divided by (*weight*\ +1), and placed in *solution1*.
