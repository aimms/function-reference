.. aimms:procedure:: DialogGetDate(title, format, date[, nr\_rows][, nr\_columns])

.. _DialogGetDate:

DialogGetDate
=============

The procedure :aimms:func:`DialogGetDate` displays a standard Windows date
selection dialog box. The procedure returns the date (in the specified
format) selected by the user.

.. code-block:: aimms

    DialogGetDate(
            title,          ! (input) string expression
            format,         ! (input) string expression
            date,           ! (input/output) scalar string parameter
            [nr_rows,]      ! (optional) integer expression
            [nr_columns]    ! (optional) integer expression
            )

Arguments
---------

    *title*
        A scalar string expression containing the text you want to display in
        the title of the dialog box.

    *format*
        A scalar string expression containing the date format of the *date*
        argument.

    *date*
        A scalar string parameter in which the selected date is returned
        according to the date format specified in *format*.

    *nr\_rows (optional)*
        A scalar integer expression in the range :math:`1,\dots,3` containing
        the number of rows to be displayed in the date selectiond dialog box.

    *nr\_columns (optional)*
        A scalar integer expression in the range :math:`1,\dots,4` containing
        the number of columns to be displayed in the date selectiond dialog box.

Return Value
------------

    The procedure returns 1 if the user completed the date selection dialog
    box successfully, or 0 otherwise.

.. note::

    If the *date* argument contains a valid date according to the format
    specified in *date-format*, AIMMS will set the initial date in the date
    selection dialog box equal to the specified date.

.. seealso::

    The date format specification components are discussed in full detail in
    :ref:`sec:time.format.date` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
