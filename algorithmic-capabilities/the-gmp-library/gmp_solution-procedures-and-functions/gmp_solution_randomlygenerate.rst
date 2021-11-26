.. aimms:procedure:: GMP::Solution::RandomlyGenerate(GMP, solution, maxVarBound, startPoint, perturbation)

.. _GMP::Solution::RandomlyGenerate:

GMP::Solution::RandomlyGenerate
===============================

The procedure :aimms:func:`GMP::Solution::RandomlyGenerate` generates random level
values in a solution for all columns in a generated mathematical
program. Each level value is sampled from the uniform distribution by
using the lower and upper bound of the column as parameters.

.. code-block:: aimms

    GMP::Solution::RandomlyGenerate(
         GMP,            ! (input) a generated mathematical program
         solution,       ! (input) a solution
         [maxVarBound],  ! (optional) a scalar value
         [startPoint],   ! (optional) a solution
         [perturbation]  ! (optional) a scalar value
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *solution*
        An integer scalar reference to a solution.

    *maxVarBound*
        The maximal variable bound. If a column has no upper bound then the
        sampled level value will be smaller than the maximal variable bound, and
        if a column has no lower bound then the sampled level value will be
        greater than minus the maximal variable bound. The default is 1000.

    *startPoint*
        An integer scalar reference to a solution representing a starting point.
        If specified then the sampled level value of a column will be around its
        level value in the starting point. By default no starting point is used.

    *perturbation*
        Used in combination with argument *startPoint*. A value between 0 and 1
        that represents the (relative) perturbation around the starting pount.
        The default is 0.1.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  This procedure should be called after calling the function
       :aimms:func:`GMP::Instance::CreatePresolved` if it is used in combination with
       that function. Otherwise the sampled level values might be outside
       the range of the columns in the presolved model.

    -  If argument *startPoint* is specified then for each column the
       sampled value will be in the range

       .. math:: 

       \ where :math:`x` denotes the level value of the column, :math:`lb`
       and :math:`ub` its lower and upper bound respectively, and :math:`p`
       the *perturbation* value.

    -  *startPoint* cannot be equal to *solution*.

.. seealso::

    The function :aimms:func:`GMP::Instance::CreatePresolved`.
