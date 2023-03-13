.. aimms:function:: GMP::Row::GetIndicatorColumn(GMP, row)

.. _GMP::Row::GetIndicatorColumn:

GMP::Row::GetIndicatorColumn
============================

The function :aimms:func:`GMP::Row::GetIndicatorColumn` returns, for a row in a
generated mathematical program, the column number of the indicator
column.

.. code-block:: aimms

    GMP::Row::GetIndicatorColumn(
         GMP,            ! (input) a generated mathematical program
         row             ! (input) a scalar reference or row number
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *row*
        A scalar reference to an existing row in the matrix or an element in the
        set :aimms:set:`Integers` in the range :math:`\{ 0 .. m-1 \}` where :math:`m` is the
        number of rows in the matrix.

Return Value
------------

    The function returns the column number if the indicator column exists,
    and -1 otherwise.

.. seealso::

    The routines :aimms:func:`GMP::Row::DeleteIndicatorCondition`, :aimms:func:`GMP::Row::GetIndicatorCondition` and :aimms:func:`GMP::Row::SetIndicatorCondition`.
