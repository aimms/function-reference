.. warning::

   This article references outdated technology and is provided for historical purposes only. 
   It is not recommended to use this information as a primary source for current projects or documentation. 
   Please refer to the latest documentation for up-to-date information, see more in: :doc:`aimmsxllibrary/index` 
   and the :doc:`dataexchange/index`.

.. aimms:procedure:: Spreadsheet::AssignTable(Workbook, Parameter, DataRange, RowsRange, ColumnsRange, Sheet, Sparse, RowMode, ColumnMode)

.. _Spreadsheet::AssignTable:

Spreadsheet::AssignTable
========================

The procedure :aimms:func:`Spreadsheet::AssignTable` writes tabular data to the
specified Excel or OpenOffice Calc workbook.

.. code-block:: aimms

    Spreadsheet::AssignTable(
            Workbook,       ! (input) scalar string expression
            Parameter,      ! (input) identifier
            DataRange,      ! (input) scalar string expression
            [RowsRange],    ! (optional) scalar string expression
            [ColumnsRange], ! (optional) scalar string expression
            [Sheet],        ! (optional) scalar string expression
            [Sparse],       ! (optional) scalar binary expression
            [RowMode],      ! (optional) scalar integer expression
            [ColumnMode]    ! (optional) scalar integer expression
            )

Arguments
---------

    *Workbook*
        A scalar string expression representing the Excel or Calc workbook. If
        this argument ends in ``.ods``, OpenOffice Calc is used. Otherwise,
        Excel is used.

    *Parameter*
        The AIMMS parameter to be written to the spreadsheet. This can be a
        numerical parameter, an element parameter, a string parameter, a unit
        parameter or a variable. The identifier must have a dimension greater
        than or equal to 1.

    *DataRange*
        The range in the workbook into which the *Parameter* must be written.

    *RowsRange*
        The range in the workbook into which the row labels must be written. The
        row labels are the elements of the sets that are identified by the first
        indices of *Parameter*. If the *RowsRange* is an
        :math:`m \times n`-matrix, then the row labels are the elements of the
        sets of the first m indices of *Parameter*.

    *ColumnsRange*
        The range in the workbook into which the column labels must be written.
        The column labels are the elements of the sets that are identified by
        the remaining indices of *Parameter* (the indices after those that
        constitute the *RowsRange*).

    *Sheet*
        The sheet to which the *Parameter* should be written. Default is the
        active sheet.

    *Sparse*
        If this argument is 1 (the default value), the default values of the
        *Parameter* will be represented as empty cells in the sheet, instead of
        the real default value.

    *RowMode*
        Possible values are:

        -  0: ``SPARSE_OUTPUT``: Only those rows will be shown in the workbook,
           for which there exists at least one non-default data value. If no
           default data value exists for the row, neither the row labels nor the
           row data are displayed.

        -  1: ``DENSE_OUTPUT``: All rows (both the labels and the data) are
           shown in the workbook, even if all data values for a particular row
           are equal to the default value.

        -  2: ``USER_INPUT``: The row labels for which the data must be
           transferred to the workbook, must already be present in the workbook.
           This way, they serve as input to :aimms:func:`Spreadsheet::AssignTable`.

        -  3: ``NON_EXISTING``: Use this mode to specify that no row labels must
           be printed, i.e. all indices should be represented by column labels.
           In this case the *RowsRange* argument does not need to be specified.

    *ColumnMode*
        Possible values are:

        -  0: ``SPARSE_OUTPUT``: Only those columns will be shown in the
           workbook, for which there exists at least one non-default data value.
           If no default data value exists for the column, neither the column
           labels nor the column data are displayed.

        -  1: ``DENSE_OUTPUT``: All columns (both the labels and the data) are
           shown in the workbook, even if all data values for a particular
           column are equal to the default value.

        -  2: ``USER_INPUT``: The column labels for which the data must be
           transferred to the workbook, must already be present in the workbook.
           This way, they serve as input to :aimms:func:`Spreadsheet::AssignTable`.

        -  3: ``NON_EXISTING``: Use this mode to specify that no column labels
           must be printed, i.e. all indices should be represented by row
           labels. In this case the *ColumnsRange* argument does not need to be
           specified.

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

    -  Upto AIMMS 3.11 this function was known as ``ExcelAssignTable``,
       which has become deprecated as of AIMMS 3.12.
