.. aimms:function:: GMP::Solution::GetColumnValue(GMP, solution, column, valueType)

.. _GMP::Solution::GetColumnValue:

GMP::Solution::GetColumnValue
=============================

The function :aimms:func:`GMP::Solution::GetColumnValue` returns the level value
or reduced cost of a column in a solution in the solution repository of
a generated mathematical program.

.. code-block:: aimms

    GMP::Solution::GetColumnValue(
         GMP,            ! (input) a generated mathematical program
         solution,       ! (input) a solution
         column,         ! (input) a scalar reference or column number
         [valueType]     ! (input/optional) a scalar value
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *solution*
        An integer scalar reference to a solution.

    *column*
        A scalar reference to an existing column in the matrix or the number of
        that column in the range :math:`\{ 0 .. n-1 \}` where :math:`n` is the
        number of columns in the matrix.

    *valueType*
        A scalar value specifying the value type. If 0 (the default) then the
        level value will be returned. If 1, the reduced cost. If 3, the basic state.

Return Value
------------

    The level value or reduced cost of the column.

.. note::

    -  To get the reduced cost of a column the option
       ``Always Store Marginals`` should be switched on or the
       **ReducedCost** property of the corresponding variable should be set.

    -  To get the basic state of a column the option
       ``Always Store Basics`` should be switched on or the
       **Basic** property of the corresponding variable should be set.
    
    -  This function returns 0 as basic state if the column is **nonbasic**;
       it returns 1 if the column is **basic** and 2 if the column is **superbasic**
       (nonlinear models only).

    -  If the column has a unit then the scaled value is returned (without
       unit). You can get the scale factor by using the function
       :aimms:func:`GMP::Column::GetScale`.

.. seealso::

    The routines :aimms:func:`GMP::Column::GetScale`, :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Solution::GetRowValue` and :aimms:func:`GMP::Solution::SetColumnValue`.
