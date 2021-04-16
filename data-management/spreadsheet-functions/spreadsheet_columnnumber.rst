.. aimms:function:: Spreadsheet::ColumnNumber(ColumnName)

.. _Spreadsheet::ColumnNumber:

Spreadsheet::ColumnNumber
=========================

.. warning::

  :doc:`index` are :doc:`deprecated <deprecation-table>`. One may use the :doc:`Articles/85/85-using-axll-library` or the :doc:`dataexchange/index`.

The function :aimms:func:`Spreadsheet::ColumnNumber` returns the number of the
Excel or OpenOffice Calc column with the given name.

.. code-block:: aimms

    Spreadsheet::ColumnNumber(
            ColumnName  ! (input) scalar string expression
            )

Arguments
---------

    *ColumnName*
        A scalar string expression representing the column name for which to
        determine the number.

Return Value
------------

    The function returns an integer representing the column number
    corresponding to the *ColumnName*. If it fails, AIMMS issues an error
    message and execution is halted.

.. note::

    -  Upto AIMMS 3.11 this function was known as ``ExcelColumnNumber``,
       which has become deprecated as of AIMMS 3.12.

.. seealso::

    The function :aimms:func:`Spreadsheet::ColumnName`.
