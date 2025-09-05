.. warning::

   This article references outdated technology and is provided for historical purposes only. 
   It is not recommended to use this information as a primary source for current projects or documentation. 
   Please refer to the latest documentation for up-to-date information, see more in: :doc:`aimms-libraries/repository-library/aimmsxllibrary/index` 
   and the :doc:`dataexchange/index`.

.. aimms:function:: Spreadsheet::ColumnNumber(ColumnName)

.. _Spreadsheet::ColumnNumber:

Spreadsheet::ColumnNumber
=========================

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
