.. warning::

   This article references outdated technology and is provided for historical purposes only. 
   It is not recommended to use this information as a primary source for current projects or documentation. 
   Please refer to the latest documentation for up-to-date information, see more in: :doc:`aimms-libraries/repository-library/aimmsxllibrary/index` 
   and the :doc:`dataexchange/index`.

.. aimms:procedure:: Spreadsheet::CreateWorkbook(WorkbookName, SheetName)

.. _Spreadsheet::CreateWorkbook:

Spreadsheet::CreateWorkbook
===========================

The procedure :aimms:func:`Spreadsheet::CreateWorkbook` creates a new Excel or
OpenOffice Calc workbook. In the Calc case, the workbook contains three
empty sheets. In the Excel case, it is dependant of an Excel setting how
many sheets the workbook contains. The first sheet is automatically set
as the active sheet.

.. code-block:: aimms

    Spreadsheet::CreateWorkbook(
            WorkbookName,  ! (input) scalar string expression
            [SheetName]    ! (optional) scalar string expression
            )

Arguments
---------

    *WorkbookName*
        The name under which the workbook will be known in AIMMS. In later calls
        to other procedures, *WorkbookName* has to be specified as the
        *Workbook* argument. When the workbook should eventually be saved in a
        particular path, then this path can be included in this argument. If
        this argument ends in ``.ods``, OpenOffice Calc is used. Otherwise,
        Excel is used.

    *SheetName*
        The name of the first sheet of the new workbook. If this argument is
        omitted, the sheet will be determined by the spreadsheet application
        ("Sheet1" in the English version). This sheet will automatically be set
        as the active sheet.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise. In case of an error
    the pre-defined AIMMS parameter :aimms:set:`CurrentErrorMessage` contains a description of what
    went wrong.

.. note::

    -  Upto AIMMS 3.11 this function was known as ``ExcelCreateWorkbook``,
       which has become deprecated as of AIMMS 3.12.
