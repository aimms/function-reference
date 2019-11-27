.. aimms:procedure:: PageCopyTableToExcel(pageName, tag, includeHeaders, selectionOnly, ExcelWorkbook, Range, Sheet)

.. _PageCopyTableToExcel:

PageCopyTableToExcel
====================

With the procedure :aimms:func:`PageCopyTableToExcel` you can copy (part of) a
specific table on a specific page directly to a range in Excel.

.. code-block:: aimms

    PageCopyTableToExcel(
            pageName,         ! (input) scalar string expression
            tag,              ! (input) scalar string expression
            includeHeaders,   ! (input) scalar numerical expression
            selectionOnly,    ! (input) scalar numerical expression
            ExcelWorkbook,    ! (input) scalar string expression
            Range,            ! (input) scalar string expression
            [Sheet]           ! (optional) scalar string expression
            )

Arguments
---------

    *pageName*
        A string expression representing the name of the page containing the
        table.

    *tag*
        A string expression representing the tag name of the table for which you
        want to copy the current displayed data. This can be a Composite Table,
        a Pivot Table or an standard Table object.

    *includeHeaders*
        A scalar numerical expression to control whether or not the headers
        should be copied as well. If ``includeHeaders`` is not equal to 0 then
        the headers are included.

    *selectionOnly*
        A scalar numerical expression to control whether the entire table or
        only the currently selected cells should be copied. If ``selectionOnly``
        is not equal to 0 then only the currently selected cells (with or
        without the corresponding headers, based on the value of
        ``includeHeaders``) are copied.

    *ExcelWorkbook*
        A scalar string expression representing the Excel workbook.

    *Range*
        A scalar string expression containing the (named) range in the Excel
        sheet to which the table should be copied.

    *Sheet*
        The sheet to which the table should be copied. Default is the active
        sheet.

Return Value
------------

    The procedure returns 1 on success. If it fails, then it returns 0 and
    the pre-defined identifier :aimms:set:`CurrentErrorMessage` will contain a proper error
    message.

.. note::

    -  By calling the procedure ``ExcelSetActiveSheet`` you can set the
       active sheet, after which the optional sheet argument can be omitted
       in procedures like this one.

    -  A call to this procedure with a specified sheet argument does not
       change the active sheet, except when the workbook does not have an
       active sheet yet.

    -  When the dimensions of the specified range do no match the dimensions
       of the table on the clipboard, then the standard Excel rules for
       pasting are applied. That is:

       -  if the range is only one column wide, then the range will
          automatically be expanded horizontally to match the number of
          columns on the clipboard,

       -  else if the number of columns in the range is smaller than the
          number of columns on the clipboard then only the first columns
          that fit will be copied,

       -  else if the number of columns in the range is larger than the
          number of columns on the clipboard, the range is made smaller.

       A similar algorithm is used for the number of rows. So if you want to
       make sure that the entire contents of the copied table is pasted in
       Excel, you can best specify a range of exactly one cell.

    -  You can specify a unique tag name for each page object via the object
       properties.

.. seealso::

    The procedure :aimms:func:`PageCopyTableToClipboard`.
