.. aimms:function:: PrinterSetupDialog(None)

.. _PrinterSetupDialog:

PrinterSetupDialog
==================

With the procedure :aimms:func:`PrinterSetupDialog` you can open the standard
printer setup dialog. This same dialog is also available via the menu
command ``File - Print Setup``.

.. code-block:: aimms

    PrinterSetupDialog

Arguments
---------

    *None*

Return Value
------------

    If the setup dialog is cancelled, the procedure :aimms:func:`PrinterSetupDialog`
    returns 0. Otherwise it will return 1.

Example
-------

    You can use the procedure :aimms:func:`PrinterSetupDialog` to make sure that a
    user selects a PDF printer: 

    .. code-block:: aimms

        	isPDFPrinter := 0;
        	Repeat
        		PrinterGetCurrentName(currentPrinter);
        		if FindString(currentPrinter,"PDF") then 
        			isPDFPrinter := 1;
        			break;
        		endif;
        		DialogMessage("Please select a PDF printer.");
        		break when PrinterSetupDialog() = 0;
        	EndRepeat; 

.. seealso::

    The procedures :aimms:func:`PrinterGetCurrentName`.
