.. aimms:function:: GMP::Solution::GetPenalizedObjective(GMP, solution1, solution2, skipObj)

.. _GMP::Solution::GetPenalizedObjective:

GMP::Solution::GetPenalizedObjective
====================================

The function :aimms:func:`GMP::Solution::GetPenalizedObjective` calculates the
penalized objective for a generated mathematical program by using the
level values of the columns in a first solution and the shadow prices in
a second solution as the penalty multipliers for the rows. To avoid a
very large value, the penalized objective value is divided by the square
of the number of rows.

.. code-block:: aimms

    GMP::Solution::GetPenalizedObjective(
         GMP,            ! (input) a generated mathematical program
         solution1,      ! (input) a solution
         solution2,      ! (input) a solution
         [skipObj]       ! (optional, default 0) a scalar value
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *solution1*
        An integer scalar reference to a solution.

    *solution2*
        An integer scalar reference to a solution.

    *skipObj*
        A scalar binary value to indicate whether the objective defining
        constraint should be skipped (value 1) or not (value 0).

Return Value
------------

    In case of success, the penalized objective function value of the *GMP*
    associated with both solutions. Otherwise it returns -1e80 for a
    maximization problem, and 1e80 for a minimization problem (or a
    feasibility problem).

.. note::

    Assume that :math:`x` denotes the level values of the columns in
    *solution1* and :math:`w` the shadow prices of the rows in *solution2*.
    Then the penalized objective function :math:`P(x,w)` is defined as

    .. math:: P(x,w) = \frac{f(x) + dirval * \sum_{i=1}^m \big( w_i * viol(g_i(x)) \big)}{m^2} ,

    \ where :math:`f(x)` denotes the objective function value, :math:`m` is
    the number of rows and the function :math:`viol(g_i(x))` equals the
    absolute amount by which the :math:`i`\ th row is violated at the point
    :math:`x`. Here :math:`dirval` is 1 in case of minization and -1 in case
    of maximization.

.. seealso::

    The procedure :aimms:func:`GMP::Solution::UpdatePenaltyWeights`.
