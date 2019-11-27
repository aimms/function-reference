.. aimms:function:: Spreadsheet::ColumnName(ColumnNumber)

.. _Spreadsheet::ColumnName:

Spreadsheet::ColumnName
=======================

The function :aimms:func:`Spreadsheet::ColumnName` returns the name of the Excel
or OpenOffice Calc column with the given number.

.. code-block:: aimms

    Spreadsheet::ColumnName(
            ColumnNumber  ! (input) scalar numerical expression
            )

Arguments
---------

    *ColumnNumber*
        A scalar integer expression representing the column number for which to
        determine the name.

Return Value
------------

    The function returns a string representing the column name corresponding
    to the *ColumnNumber*. If it fails, AIMMS issues an error message and
    execution is halted.

.. note::

    -  Upto AIMMS 3.11 this function was known as ``ExcelColumnName``, which
       has become deprecated as of AIMMS 3.12.

.. seealso::

    The function :aimms:func:`Spreadsheet::ColumnNumber`.
