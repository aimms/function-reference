.. aimms:function:: StringToMoment(Format, Unit, ReferenceDate, Timeslot)

.. _StringToMoment:

StringToMoment
==============

The function :aimms:func:`StringToMoment` converts a given time string (in a free
time format) to the elapsed time with a respect to a specific reference
date.

.. code-block:: aimms

    StringToMoment(
         Format,             ! (input) a string expression
         Unit,               ! (input) a time unit
         ReferenceDate,      ! (input) a string expression
         Timeslot            ! (input) a string expression
         )

Arguments
---------

    *Format*
        A string that holds the date and time format used in the fourth argument
        *Timeslot*. Valid format strings are described in Section 33.7.

    *Unit*
        The time unit that is used to return the elapsed time.

    *ReferenceDate*
        A string that holds the begin date using the fixed format for date and
        time, see paragraph *Reference date format* on page 544 of the Language
        Reference.

    *Timeslot*
        A string representing a specific date and time moment using the format
        specified in the first argument *Format*.

Return Value
------------

    The result of :aimms:func:`StringToMoment` is the elapsed time in *unit* between
    *reference-date* and *date*.

.. seealso::

    The functions :aimms:func:`MomentToString`, :aimms:func:`CurrentToMoment`.
