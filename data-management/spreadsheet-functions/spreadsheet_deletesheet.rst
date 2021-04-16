.. aimms:procedure:: Spreadsheet::DeleteSheet(Workbook, Name)

.. _Spreadsheet::DeleteSheet:

Spreadsheet::DeleteSheet
========================

.. warning::

  :doc:`index` are :doc:`deprecated <deprecation-table>`. One may use the :doc:`Articles/85/85-using-axll-library` or the :doc:`dataexchange/index`.

The procedure :aimms:func:`Spreadsheet::DeleteSheet` deletes the given sheet from
the specified Excel or OpenOffice Calc workbook.

.. code-block:: aimms

    Spreadsheet::DeleteSheet(
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
        The name of the sheet to be deleted.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise. In case of an error
    the pre-defined AIMMS parameter :aimms:set:`CurrentErrorMessage` contains a description of what
    went wrong.

.. note::

    -  Upto AIMMS 3.11 this function was known as ``ExcelDeleteSheet``,
       which has become deprecated as of AIMMS 3.12.
