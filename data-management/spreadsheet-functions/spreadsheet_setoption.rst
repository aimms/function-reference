.. aimms:procedure:: Spreadsheet::SetOption(Name, Value)

.. _Spreadsheet::SetOption:

Spreadsheet::SetOption
======================

.. warning::

  :doc:`index` are :doc:`deprecated <deprecation-table>`. One may use the :doc:`Articles/85/85-using-axll-library` or the :doc:`dataexchange/index`.

The procedure :aimms:func:`Spreadsheet::SetOption` sets a global option that has
an effect in all subsequent calls to the spreadsheet functions.
Currently the following options are supported:

-  ``CalendarElementsAsStrings`` By default elements in an AIMMS
   Calendar are communicated to the spreadsheet in a special date
   format, which is independent of the current time slot format in
   AIMMS. If this option is set to 1, the elements are communicated as a
   string, using the time slot format of the calendar.

-  ``WriteInfValueAsString`` By default a value of INF or -INF in AIMMS
   is passed to the spreadsheet as a huge numeric number (1e150 and
   -1e150 respectively). If you set this option to 1, these values are
   written as a string "INF" or "-INF". Please be aware that in this
   case the cell will not have a numerical content which may cause
   problems in other code that is using the spreadsheet.

.. code-block:: aimms

    Spreadsheet::SetOption(
            Name,       ! (input) scalar string expression
            Value       ! (input) scalar expression
            )

Arguments
---------

    *Name*
        A scalar string representing the name of the option.

    *Value*
        A scalar expression representing the new value for the option.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.
