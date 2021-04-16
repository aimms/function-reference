.. aimms:procedure:: Spreadsheet::AssignParameter(Workbook, Parameter, Range, Sheet, Sparse, Transposed)

.. _Spreadsheet::AssignParameter:

Spreadsheet::AssignParameter
============================

.. warning::

  :doc:`index` are :doc:`deprecated <deprecation-table>`. One may use the :doc:`Articles/85/85-using-axll-library` or the :doc:`dataexchange/index`.

The procedure :aimms:func:`Spreadsheet::AssignParameter` writes data from the
given parameter into the range of the Excel or OpenOffice Calc workbook.

.. code-block:: aimms

    Spreadsheet::AssignParameter(
            Workbook,       ! (input) scalar string expression
            Parameter,      ! (input) identifier
            Range,          ! (input) scalar string expression
            [Sheet],        ! (optional) scalar string expression
            [Sparse],       ! (optional) scalar binary expression
            [Transposed]    ! (optional) scalar binary expression
            )

Arguments
---------

    *Workbook*
        A scalar string expression representing the Excel or Calc workbook. If
        this argument ends in ``.ods``, OpenOffice Calc is used. Otherwise,
        Excel is used.

    *Parameter*
        The AIMMS identifier to be written to the spreadsheet. This can be a
        numerical parameter, an element parameter, a string parameter, a unit
        parameter or a variable. The dimension of this identifier can be 0, 1,
        or 2.

    *Range*
        The range in the workbook into which the *parameter* must be written.

    *Sheet*
        The sheet to which the *Value* should be written. Default is the active
        sheet.

    *Sparse*
        If this argument is 1 (its default value), the default values of the
        parameter will be represented as empty cells in the sheet, instead of
        the real default value.

    *Transposed*
        If this argument is 1, the parameter will be transposed before being
        displayed. The argument does not have any effect on scalar and
        one-dimensional data. The default value of this argument is 0.

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

    -  Upto AIMMS 3.11 this function was known as ``ExcelAssignParameter``,
       which has become deprecated as of AIMMS 3.12.
