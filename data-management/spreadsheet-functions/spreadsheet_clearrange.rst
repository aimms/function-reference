.. aimms:procedure:: Spreadsheet::ClearRange(Workbook, Range, Sheet, IncludeCellFormatting)

.. _Spreadsheet::ClearRange:

Spreadsheet::ClearRange
=======================

The procedure :aimms:func:`Spreadsheet::ClearRange` empties the specified range in
the specified sheet.

.. code-block:: aimms

    Spreadsheet::ClearRange(
            Workbook,               ! (input) scalar string expression
            Range,                  ! (input) scalar string expression
            [Sheet],                ! (optional) scalar string expression
            [IncludeCellFormatting] ! (optional) scalar binary expression
            )

Arguments
---------

    *Workbook*
        A scalar string expression representing the Excel or Calc workbook. If
        this argument ends in ``.ods``, OpenOffice Calc is used. Otherwise,
        Excel is used.

    *Range*
        A scalar string expression containing a reference to the range in the
        sheet that should be emptied.

    *Sheet*
        The sheet from which the value should be read. Default is the active
        sheet. If the range is a uniquely named range, no active sheet needs to
        be set, since named ranges already contain a reference to a sheet.

    *IncludeCellFormatting*
        When set to 1, the formatting of the cell (e.g. font size, color, ...)
        is also cleared. If set to 0, only the value of the cell is cleared.

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

    -  Upto AIMMS 3.11 this function was known as ``ExcelClearRange``, which
       has become deprecated as of AIMMS 3.12.
