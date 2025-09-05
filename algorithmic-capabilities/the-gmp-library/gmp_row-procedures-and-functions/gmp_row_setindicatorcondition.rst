.. aimms:procedure:: GMP::Row::SetIndicatorCondition(GMP, row, column, value)

.. _GMP::Row::SetIndicatorCondition:

GMP::Row::SetIndicatorCondition
===============================

The procedure :aimms:func:`GMP::Row::SetIndicatorCondition` assigns an indicator
column and condition to a row in a generated mathematical program.

.. code-block:: aimms

    GMP::Row::SetIndicatorCondition(
         GMP,            ! (input) a generated mathematical program
         row,            ! (input) a scalar reference or row number
         column,         ! (input) a scalar reference or column number
         value           ! (input) a numerical expression
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *row*
        A scalar reference to an existing row in the matrix or an element in the
        set :aimms:set:`Integers` in the range :math:`\{ 0 .. m-1 \}` where :math:`m` is the
        number of rows in the matrix.

    *column*
        A scalar reference to an existing column in the matrix or an element in the
        set :aimms:set:`Integers` in the range :math:`\{ 0 .. n-1 \}` where :math:`n` is the
        number of columns in the matrix.

    *value*
        A binary value that will be used as indicator condition.

Return Value
------------

    The procedure returns 1 on success, and 0 otherwise.

.. note::

    -  Assigning an indicator column and condition to a row means that the
       row must (only) be satisfied if the level value of the indicator
       column equals the indicator condition.

    -  This procedure fails if the row is nonlinear or if the column is not
       binary.

.. seealso::

    - The routines :aimms:func:`GMP::Row::DeleteIndicatorCondition`, :aimms:func:`GMP::Row::GetIndicatorColumn` and :aimms:func:`GMP::Row::GetIndicatorCondition`.
