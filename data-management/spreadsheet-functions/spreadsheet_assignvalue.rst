.. aimms:procedure:: Spreadsheet::AssignValue(Workbook, Value, Range, Sheet)

.. _Spreadsheet::AssignValue:

Spreadsheet::AssignValue
========================

.. warning::

  :doc:`index` are :doc:`deprecated <deprecation-table>`. One may use the :doc:`Articles/85/85-using-axll-library` or the :doc:`dataexchange/index`.

The procedure :aimms:func:`Spreadsheet::AssignValue` writes a value or formula
from AIMMS to an Excel or OpenOffice Calc cell or range of cells.

.. code-block:: aimms

    Spreadsheet::AssignValue(
            Workbook,       ! (input) scalar string expression
            Value,          ! (input) scalar expression
            Range,          ! (input) scalar string expression
            [Sheet]         ! (optional) scalar string expression
            )

Arguments
---------

    *Workbook*
        A scalar string expression representing the Excel or Calc workbook. If
        this argument ends in ``.ods``, OpenOffice Calc is used. Otherwise,
        Excel is used.

    *Value*
        A scalar numerical, string, element-valued or unit-valued expression
        containing the value to be written to the spreadsheet.

    *Range*
        A scalar string expression containing the range in the spreadsheet to
        which the *Value* should be written.

    *Sheet*
        The sheet to which the *Value* should be written. Default is the active
        sheet.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise. In case of an error
    the pre-defined AIMMS parameter :aimms:set:`CurrentErrorMessage` contains a description of what
    went wrong.

.. note::

    -  By calling the procedure :aimms:func:`Spreadsheet::SetActiveSheet` you can set the active sheet,
       after which the optional sheet argument can be omitted in procedures
       like this one.

    -  A call to this procedure with a specified sheet argument does not
       change the active sheet, except when the workbook does not have an
       active sheet yet.

    -  Upto AIMMS 3.11 this function was known as ``ExcelAssignValue``,
       which has become deprecated as of AIMMS 3.12.
