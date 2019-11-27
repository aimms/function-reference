.. aimms:procedure:: PrintPage(page[, filename][, from\_pagenr][, to\_pagenr][, UseDefaultBitmapPrintSettings])

.. _PrintPage:

PrintPage
=========

With the procedure :aimms:func:`PrintPage` you can print a single print page. If
the page contains a data object for which the available data does not
fit onto a single printed sheet, AIMMS will print as many sheets as
needed.

.. code-block:: aimms

    PrintPage(
            page,            				! (input) scalar string expression
            [filename,]      				! (optional) scalar string expression
            [from_pagenr,]   				! (optional) integer
            [to_pagenr,]     				! (optional) integer
            [UseDefaultBitmapPrintSettings]	! (optional) integer
            )

Arguments
---------

    *page*
        A string expression representing the name of the page that you want to
        print. This name is the unique name as it appears in the Page Manager
        tree.

    *filename (optional)*
        If this file name is specified, then AIMMS will print to the specific
        file and not directly to the printer. If this argument is omitted, then
        AIMMS will print according to the settings of the currently selected
        printer.

    *from\_pagenr (optional)*
        If the objects on the page result in multiple printed sheets, then with
        this argument you can specify the first sheet to print. If omitted, then
        printing will start at the first sheet (from_pagenr = 1).

    *to\_pagenr (optional)*
        If the objects on the page result in multiple printed sheets, then with
        this argument you can specify the last sheet to print. If omitted, then
        printing continues until the last sheet.

    *UseDefaultBitmapPrintSettings (optional)*
        When printing a non-print page, the page is printed by creating an exact
        bitmap copy of the page as it appears on the screen. By default (if the
        argument equals 0), a dialog will appear in which you can specify which
        scale should be applied such that it fits on one or more sheets. By
        settings this argument to 1, this dialog box will be skipped and the
        bitmap print will use the standard settings of the dialog box. If the
        page to print is designed as a print page, then this argument is
        ignored.

Return Value
------------

    The procedure returns the actual number of pages printed if the print
    page is printed successfully. If the procedure fails to print the page
    it returns 0, and the pre-defined parameter :aimms:set:`CurrentErrorMessage` will contain a
    proper error message.

.. seealso::

    The procedures :aimms:func:`PrintPageCount`, :aimms:func:`PrintStartReport`.
