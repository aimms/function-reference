.. aimms:procedure:: PageCopyTableToClipboard(pageName, tag, includeHeaders, selectionOnly)

.. _PageCopyTableToClipboard:

PageCopyTableToClipboard
========================

With the procedure :aimms:func:`PageCopyTableToClipboard` you can copy (part of) a
specific table on a specific page to the clipboard, so that you
subsequently can paste it in any other application.

.. code-block:: aimms

    PageCopyTableToClipboard(
            pageName,         ! (input) scalar string expression
            tag,              ! (input) scalar string expression
            includeHeaders,   ! (input) scalar numerical expression
            selectionOnly     ! (input) scalar numerical expression
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

Return Value
------------

    The procedure returns 1 on success. If it fails, then it returns 0 and
    the pre-defined identifier :aimms:set:`CurrentErrorMessage` will contain a proper error
    message.

.. note::

    You can specify a unique tag name for each page object via the object
    properties.

.. seealso::

    The procedure :aimms:func:`PageCopyTableToExcel`.
