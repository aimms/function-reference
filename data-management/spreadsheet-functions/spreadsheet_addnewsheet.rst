.. aimms:procedure:: Spreadsheet::AddNewSheet(Workbook, Name, SetAsActive, Hidden)

.. _Spreadsheet::AddNewSheet:

Spreadsheet::AddNewSheet
========================

.. warning::

  :doc:`index` are :doc:`deprecated <deprecation-table>`. One may use the :doc:`Articles/85/85-using-axll-library` or the :doc:`dataexchange/index`.

The procedure :aimms:func:`Spreadsheet::AddNewSheet` adds a new empty sheet to the
specified Excel or OpenOffice Calc workbook.

.. code-block:: aimms

    Spreadsheet::AddNewSheet(
            Workbook,       ! (input) scalar string expression
            Name,           ! (input) scalar string expression
            [SetAsActive],  ! (optional) scalar binary expression
            [Hidden]        ! (optional) scalar binary expression
            )

Arguments
---------

    *Workbook*
        A scalar string expression representing the Excel or Calc workbook. If
        this argument ends in ``.ods``, OpenOffice Calc is used. Otherwise,
        Excel is used.

    *Name*
        The name to assign to the new sheet.

    *SetAsActive*
        If this parameter is 1, the sheet is set as the active sheet. The
        default value of this argument is 1.

    *Hidden*
        If this parameter is 1, the sheet is created as a hidden sheet. The
        default value of this argument is 0.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise. In case of an error
    the pre-defined AIMMS parameter :aimms:set:`CurrentErrorMessage` contains a description of what
    went wrong.

.. note::

    -  Upto AIMMS 3.11 this function was known as ``ExcelAddNewSheet``,
       which has become deprecated as of AIMMS 3.12.
