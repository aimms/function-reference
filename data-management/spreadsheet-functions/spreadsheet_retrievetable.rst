.. aimms:procedure:: Spreadsheet::RetrieveTable(Workbook, Parameter, DataRange, RowsRange, ColumnsRange, Sheet, AutomaticallyExtendSets)

.. _Spreadsheet::RetrieveTable:

Spreadsheet::RetrieveTable
==========================

The procedure :aimms:func:`Spreadsheet::RetrieveTable` reads tabular data from the
specified Excel or OpenOffice Calc workbook.

.. code-block:: aimms

    Spreadsheet::RetrieveTable(
            Workbook,                 ! (input) scalar string expression
            Parameter,                ! (output) identifier
            DataRange,                ! (input) scalar string expression
            [RowsRange],              ! (optional) scalar string expression
            [ColumnsRange],           ! (optional) scalar string expression
            [Sheet]                   ! (optional) scalar string expression
            [AutomaticallyExtendSets] ! (optional) scalar binary expression
            )

Arguments
---------

    *Workbook*
        A scalar string expression representing the Excel or Calc workbook. If
        this argument ends in ``.ods``, OpenOffice Calc is used. Otherwise,
        Excel is used.

    *Parameter*
        The AIMMS parameter in which the data read from the spreadsheet will be
        stored. This can be a numerical parameter, an element parameter, a
        string parameter, a unit parameter or a variable. The identifier must
        have a dimension greater than or equal to 1.

    *DataRange*
        The range in the workbook from which the data must be read.

    *RowsRange*
        The range in the workbook from which the row labels must be read. The
        row labels will be added to the sets that are identified by the first
        indices of *Parameter*. If the *RowsRange* is an
        :math:`m \times n`-matrix (*m columns, n rows), then the row labels are
        the elements of the sets of the first :math:`m` indices of Parameter.*

    *ColumnsRange*
        The range in the workbook from which the column labels must be read. The
        column labels will be added to the sets that are identified by the
        remaining indices of *Parameter* (the indices after those that
        constitute the *RowsRange*).

    *Sheet*
        The sheet to which the *Parameter* should be written. Default is the
        active sheet.

    *AutomaticallyExtendSets*
        Indicates whether AIMMS should automatically extend the domain set of an
        identifier if necessary. If not, an error will be generated. The default
        value of this argument is 0.

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

    -  Upto AIMMS 3.11 this function was known as ``ExcelRetrieveTable``,
       which has become deprecated as of AIMMS 3.12.

.. seealso::

    An example of the use of ``ExcelRetrieveTable`` is presented on the
    AIMMS blog post: `Reading multi-dimensional Excel data with
    ExcelRetrieveTable <http://blog.aimms.com/2011/11/reading-multi-dimensional-excel-data-with-excelretrievetable/>`__
    including a pictorial explanation of the use of spreadsheet ranges.
