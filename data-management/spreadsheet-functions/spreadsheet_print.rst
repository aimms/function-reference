.. warning::

   This article references outdated technology and is provided for historical purposes only. 
   It is not recommended to use this information as a primary source for current projects or documentation. 
   Please refer to the latest documentation for up-to-date information, see more in: :doc:`Articles/85/85-using-axll-library` 
   and the :doc:`dataexchange/index`.

.. aimms:procedure:: Spreadsheet::Print(Workbook, Range, Sheet, ShowPreview, NumberOfCopies, Collate, ActivePrinter)

.. _Spreadsheet::Print:

Spreadsheet::Print
==================

The procedure :aimms:func:`Spreadsheet::Print` makes it possible to print an Excel
or OpenOffice Calc sheet from AIMMS.

.. code-block:: aimms

    Spreadsheet::Print(
            Workbook,         ! (input) scalar string expression
            Range,            ! (input) scalar string expression
            [Sheet],          ! (optional) scalar string expression
            [ShowPreview],    ! (optional) scalar binary expression
            [NumberOfCopies], ! (optional) scalar integer expression
            [Collate],        ! (optional) scalar binary expression
            [ActivePrinter]   ! (optional) scalar string expression

            )

Arguments
---------

    *Workbook*
        A scalar string expression representing the Excel or Calc workbook. If
        this argument ends in ``.ods``, OpenOffice Calc is used. Otherwise,
        Excel is

    *Range*
        The range to be printed.

    *Sheet*
        The sheet on which the range lies.

    *ShowPreview*
        If this argument is 1, Excel or Calc shows a print preview window before
        printing. The visibility mode of the workbook should be 'On' in this
        case. The default value of this argument is 0. In the preview window,
        you can decide whether to actually print or to cancel the printing.

    *NumberOfCopies*
        The number of copies to print. The default value of this argument is 1.

    *Collate*
        If this argument is 1, and more than one copy of the sheet is printed,
        the printed sheets are collated neatly. The default value of this
        argument is 1.

    *ActivePrinter*
        The user can specify the name of the printer to be used for printing the
        sheet. The default printer is used by default.

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

    -  Upto AIMMS 3.11 this function was known as ``ExcelPrint``, which has
       become deprecated as of AIMMS 3.12.
