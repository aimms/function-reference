.. aimms:function:: PeriodToString(Format, Timetable, Period)

.. _PeriodToString:

PeriodToString
==============

With the function :aimms:func:`PeriodToString` you can obtain a description of a
period in a timetable that consists of multiple calendar slots.

.. code-block:: aimms

    PeriodToString(
         Format,              ! (input) a string expression
         Timetable,           ! (input) an AIMMS time table
         Period               ! (input) an element in a horizon
         )

Arguments
---------

    *Format*
        A string that holds the date and time format used in the returned
        string. This format string can contain period specific conversion
        specifiers to generate a description referring to both the beginning and
        end of the period, see Section 33.7

    *Timetable*
        An indexed set in a calendar and defined over a horizon.

    *Period*
        An element in the horizon that is defined by *Timetable*.

Return Value
------------

    The result of :aimms:func:`PeriodToString` is a string describing the
    corresponding moment according to *Format*.

.. seealso::

    The procedure :aimms:procedure:`CreateTimeTable`.
