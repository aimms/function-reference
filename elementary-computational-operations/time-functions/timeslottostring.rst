.. aimms:function:: TimeSlotToString(Format, Calendar, Timeslot)

.. _TimeSlotToString:

TimeSlotToString
================

The function :aimms:func:`TimeSlotToString` creates a string representation of a
specific time slot in a calendar.

.. code-block:: aimms

    TimeSlotToString(
         Format,         ! (input) a string expression
         Calendar,       ! (input) a calendar
         Timeslot        ! (input) an element (timeslot) in the calendar
         )

Arguments
---------

    *Format*
        A string that holds the date and time format used in the returned
        string. Valid format strings are described in Section 33.7.

    *Calendar*
        An identifier of type calendar.

    *Timeslot*
        A specific time-slot in the calendar.

Return Value
------------

    The function :aimms:func:`TimeSlotToString` returns a string representation of the
    time slot.

.. seealso::

    The functions :aimms:func:`MomentToString`, :aimms:func:`CurrentToTimeSlot`, :aimms:func:`StringToTimeSlot`.
