.. aimms:function:: GMP::Solution::GetFirstOrderDerivative(GMP, solution, row, column)

.. _GMP::Solution::GetFirstOrderDerivative:

GMP::Solution::GetFirstOrderDerivative
======================================

The function :aimms:func:`GMP::Solution::GetFirstOrderDerivative` returns the
first order derivative for a column in a row in a solution in the
solution repository of a generated mathematical program.

.. code-block:: aimms

    GMP::Solution::GetFirstOrderDerivative(
         GMP,            ! (input) a generated mathematical program
         solution,       ! (input) a solution
         row,            ! (input) a scalar reference or row number
         column          ! (input) a scalar reference or column number
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

    *column*
        A scalar reference to an existing column in the matrix or an element in the
        set :aimms:set:`Integers` in the range :math:`\{ 0 .. n-1 \}` where :math:`n` is the
        number of columns in the matrix.

Return Value
------------

    The first order derivative of the column in the row.

.. note::

    If this function is called for multiple rows and columns, then AIMMS
    will calculate the first order derivatives more efficiently if this
    function is called row wise instead of column wise. That is, it is
    better to call this function for all columns in a certain row before
    calling it for the next row.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`.
