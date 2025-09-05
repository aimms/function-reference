.. warning::

   This article references outdated technology and is provided for historical purposes only. 
   It is not recommended to use this information as a primary source for current projects or documentation. 
   Please refer to the latest documentation for up-to-date information, see more in: :doc:`Articles/85/85-using-axll-library` 
   and the :doc:`dataexchange/index`.

.. aimms:procedure:: Spreadsheet::RetrieveParameter(Workbook, Parameter, Range, Sheet, Transposed)

.. _Spreadsheet::RetrieveParameter:

Spreadsheet::RetrieveParameter
==============================

The procedure :aimms:func:`Spreadsheet::RetrieveParameter` reads data from the
given range in the Excel or OpenOffice Calc workbook into the specified
AIMMS parameter.

.. code-block:: aimms

    Spreadsheet::RetrieveParameter(
            Workbook,       ! (input) scalar string expression
            Parameter,      ! (output) identifier
            Range,          ! (input) scalar string expression
            [Sheet],        ! (optional) scalar string expression
            [Transposed]    ! (optional) scalar binary expression
            )

Arguments
---------

    *Workbook*
        A scalar string expression representing the Excel or Calc workbook. If
        this argument ends in ``.ods``, OpenOffice Calc is used. Otherwise,
        Excel is

    *Parameter*
        The AIMMS identifier to be filled with spreadsheet data. This can be a
        numerical parameter, an element parameter, a string parameter, a unit
        parameter or a variable. The dimension of the parameter can be 0, 1 or
        2.

    *Range*
        The range in the workbook based on which the *parameter* must be filled.

    *Sheet*
        The sheet in which the *Range* lies. Default is the active sheet.

    *Transposed*
        If this argument is 1, the parameter is read transposed from the sheet.
        The argument does not have any effect on scalar and one-dimensional
        data. The default value for this argument is 0.

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

    -  Upto AIMMS 3.11 this function was known as
       ``ExcelRetrieveParameter``, which has become deprecated as of AIMMS
       3.12.
