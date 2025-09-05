.. aimms:function:: GMP::Solution::GetRowValue(GMP, solution, row, valueType)

.. _GMP::Solution::GetRowValue:

GMP::Solution::GetRowValue
==========================

The function :aimms:func:`GMP::Solution::GetRowValue` returns the level value or
shadow price of a row in a solution in the solution repository of a
generated mathematical program.

.. code-block:: aimms

    GMP::Solution::GetRowValue(
         GMP,            ! (input) a generated mathematical program
         solution,       ! (input) a solution
         row,            ! (input) a scalar reference or row number
         [valueType]     ! (input/optional) a scalar value
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *solution*
        An integer scalar reference to a solution.

    *row*
        A scalar reference to an existing row in the matrix or an element in the
        set :aimms:set:`Integers` in the range :math:`\{ 0 .. m-1 \}` where :math:`m` is the
        number of rows in the matrix.

    *valueType*
        A scalar value specifying the value type. If 0 (the default) then the
        level value as calculated by the solver (or algorithm) will be returned.
        If 1, the shadow price. If 2, the level value after evaluating the row
        using the column values in the solution. If 3, the basic state.

Return Value
------------

    The level value or shadow price of the row.

.. note::

    -  To get the level value of a row, if *valueType* is set to 0, the
       option ``Always Store Constraint Levels`` should be switched on or
       the **Level** property of the corresponding constraint should be set.

    -  To get the shadow price of a row the option
       ``Always Store Marginals`` should be switched on or the
       **ShadowPrice** property of the corresponding constraint should be
       set.

    -  To get the basic state of a row the option
       ``Always Store Basics`` should be switched on or the
       **Basic** property of the corresponding constraint should be set.

    -  This function returns 0 as basic state if the row is **nonbasic**;
       it returns 1 if the row is **basic** and 2 if the row is **superbasic**
       (nonlinear models only).

    -  If the row has a unit then the scaled value is returned (without
       unit). You can get the scale factor by using the function
       :aimms:func:`GMP::Row::GetScale`.

.. seealso::

    - The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Row::GetScale`, :aimms:func:`GMP::Solution::GetColumnValue` and :aimms:func:`GMP::Solution::SetRowValue`.
