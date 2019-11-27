.. aimms:procedure:: PrintStartReport(title[, filename])

.. _PrintStartReport:

PrintStartReport
================

With the procedure :aimms:func:`PrintStartReport` you start printing a report that
consists of the printing of multiple pages (using the procedure
``PrintPage``). The advantage of printing in the form of a report is
that all print request until ``PrintEndReport`` arrive at the printer as
a single print job, and that the pages are numbered correctly.

.. code-block:: aimms

    PrintStartReport(
            title,           ! (input) scalar string expression
            [filename]       ! (optional) scalar string expression
            )

Arguments
---------

    *title*
        A string expression representing the title of the report. This title is
        used in the communication to the printer as the name of the print job.

    *filename (optional)*
        If this file name is specified, then AIMMS will print to the specific
        file and not directly to the printer. If this argument is omitted, then
        AIMMS will print according to the settings of the currently selected
        printer.

Return Value
------------

    The procedure returns 1 on success. If the procedure fails, then the
    pre-defined parameter :aimms:set:`CurrentErrorMessage` will contain a proper error message.

.. note::

    A successful call to :aimms:func:`PrintStartReport` must be followed by a call to
    ``PrintEndReport``, otherwise nothing is printed, and your printer may
    hang.

.. seealso::

    The procedures :aimms:func:`PrintEndReport`, :aimms:func:`PrintPage`.
