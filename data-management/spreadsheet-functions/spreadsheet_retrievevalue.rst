.. aimms:procedure:: Spreadsheet::RetrieveValue(Workbook, Parameter, Range, Sheet)

.. _Spreadsheet::RetrieveValue:

Spreadsheet::RetrieveValue
==========================

.. warning::

  :doc:`index` are :doc:`deprecated <deprecation-table>`. One may use the :doc:`Articles/85/85-using-axll-library` or the :doc:`dataexchange/index`.

The procedure :aimms:func:`Spreadsheet::RetrieveValue` reads the value of an Excel
or OpenOffice Calc cell into a scalar AIMMS parameter.

.. code-block:: aimms

    Spreadsheet::RetrieveValue(
            Workbook,       ! (input) scalar string expression
            Parameter,      ! (output) scalar identifier
            Range,          ! (input) scalar string expression
            [Sheet]         ! (optional) scalar string expression
            )

Arguments
---------

    *Workbook*
        A scalar string expression representing the Excel or Calc workbook. If
        this argument ends in ``.ods``, OpenOffice Calc is used. Otherwise,
        Excel is

    *Parameter*
        A scalar numerical parameter, string parameter, element parameter or
        unit parameter to which the value from the *Range* will be written.

    *Range*
        A scalar string expression containing a reference to the cell in the
        sheet from which the value will be read.

    *Sheet*
        The sheet from which the value should be read. Default is the active
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

    -  Upto AIMMS 3.11 this function was known as ``ExcelRetrieveValue``,
       which has become deprecated as of AIMMS 3.12.
