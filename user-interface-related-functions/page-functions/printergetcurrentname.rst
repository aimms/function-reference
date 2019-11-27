.. aimms:procedure:: PrinterGetCurrentName(printerName)

.. _PrinterGetCurrentName:

PrinterGetCurrentName
=====================

With the procedure :aimms:func:`PrinterGetCurrentName` you can retrieve the name
of the currently selected printer.

.. code-block:: aimms

    PrinterGetCurrentName(
            printerName     ! (ouput) scalar string parameter
            )

Arguments
---------

    *printerName*
        On return this string parameter will contain the name of the currently
        selected printer.

Return Value
------------

    The procedure returns 1 if it did retrieve a printer name successfully.
    If it return 0, something is wrong with the printer setup and
    ``printerName`` will be empty.

Example
-------

    You can use the procedure :aimms:func:`PrinterGetCurrentName` to create a PDF
    preview mode for the pages that you want to print: 

    .. code-block:: aimms

                PrinterGetCurrentName(currentPrinter);
        		if FindString(currentPrinter,"PDF") then 
        			PrintStartReport("Report", "output.pdf");
        			PrintPage("MyPrintPage");
        			PrintEndReport;
        			! if there is a PDF viewer installed (like AcrobatReader), you can now open the document with it:
        			OpenDocument("output.pdf");
        		endif;

.. note::

    To change the current printer, you can use the menu item
    ``File - Print Setup`` or make a call to the procedure :aimms:func:`PrinterSetupDialog`.

.. seealso::

    The procedures :aimms:func:`PrinterSetupDialog`.
