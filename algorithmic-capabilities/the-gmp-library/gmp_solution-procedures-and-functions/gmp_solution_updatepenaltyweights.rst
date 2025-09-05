.. aimms:procedure:: GMP::Solution::UpdatePenaltyWeights(GMP, solution1, solution2, minValue)

.. _GMP::Solution::UpdatePenaltyWeights:

GMP::Solution::UpdatePenaltyWeights
===================================

The procedure :aimms:func:`GMP::Solution::UpdatePenaltyWeights` updates the
penalty weights which are stored as shadow prices in a first solution of
a generated mathematical program. The shadow price of a row in this
solution is compared with the shadow price of the same row in the second
solution, and replaced by the maximum of both shadow prices.

.. code-block:: aimms

    GMP::Solution::UpdatePenaltyWeights(
         GMP,            ! (input) a generated mathematical program
         solution1,      ! (input) a solution
         solution2,      ! (input) a solution
         [minValue]      ! (optional) a scalar value
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *solution1*
        An integer scalar reference to a solution.

    *solution2*
        An integer scalar reference to a solution.

    *minValue*
        The minimum value for each shadow price. The default is 0.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    If for a certain row both the shadow prices in *solution1* and
    *solution2* are smaller than *minValue*, the new value assigned to the
    shadow price in *solution1* will be *minValue*.

.. seealso::

    - The function :aimms:func:`GMP::Solution::GetPenalizedObjective`.
