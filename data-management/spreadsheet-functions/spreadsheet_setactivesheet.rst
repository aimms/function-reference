.. aimms:procedure:: Spreadsheet::SetActiveSheet(Workbook, Name)

.. _Spreadsheet::SetActiveSheet:

Spreadsheet::SetActiveSheet
===========================

The procedure :aimms:func:`Spreadsheet::SetActiveSheet` sets the active sheet for
the given Excel or OpenOffice Calc workbook.

.. code-block:: aimms

    Spreadsheet::SetActiveSheet(
            Workbook,       ! (input) scalar string expression
            Name            ! (input) scalar string expression
            )

Arguments
---------

    *Workbook*
        A scalar string expression representing the Excel or Calc workbook. If
        this argument ends in ``.ods``, OpenOffice Calc is used. Otherwise,
        Excel is

    *Name*
        A scalar string expression representing the sheet to be selected as the
        active sheet.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise. In case of an error
    the pre-defined AIMMS parameter :aimms:set:`CurrentErrorMessage` contains a description of what
    went wrong.

.. note::

    -  By calling this procedure explicitly before other procedures, the
       optional sheet argument can be omitted in those procedures.

    -  A call to another procedure with a specified sheet argument does not
       change the active sheet, except when the workbook does not have an
       active sheet yet.

    -  Upto AIMMS 3.11 this function was known as ``ExcelSetActiveSheet``,
       which has become deprecated as of AIMMS 3.12.
