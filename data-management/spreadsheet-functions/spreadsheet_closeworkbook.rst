.. aimms:procedure:: Spreadsheet::CloseWorkbook(Workbook, SaveBeforeClose)

.. _Spreadsheet::CloseWorkbook:

Spreadsheet::CloseWorkbook
==========================

The procedure :aimms:func:`Spreadsheet::CloseWorkbook` closes the specified Excel
or OpenOffice Calc workbook. Internally, AIMMS keeps the workbook open
from the moment that a procedure is applied on it for the first time.
This is good for performance. Nevertheless, the user can specify that he
is finished with the workbook and that the workbook can be closed. If a
workbook is not closed explicitly, and changes have been made to it, the
user is asked whether or not to save it just before closing the AIMMS
project.

.. code-block:: aimms

    Spreadsheet::CloseWorkbook(
            Workbook,         ! (input) scalar string expression
            SaveBeforeClose   ! (input) scalar binary expression
            )

Arguments
---------

    *Workbook*
        A scalar string expression representing the Excel or Calc workbook. If
        this argument ends in ``.ods``, OpenOffice Calc is used. Otherwise,
        Excel is used.

    *SaveBeforeClose*
        If this argument is 1, the workbook is saved before it is closed.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise. In case of an error
    the pre-defined AIMMS parameter :aimms:set:`CurrentErrorMessage` contains a description of what
    went wrong.

.. note::

    -  Upto AIMMS 3.11 this function was known as ``ExcelCloseWorkbook``,
       which has become deprecated as of AIMMS 3.12.
