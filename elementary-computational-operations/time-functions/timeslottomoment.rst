.. aimms:function:: TimeSlotToMoment(Calendar, ReferenceDate, Timeslot)

.. _TimeSlotToMoment:

TimeSlotToMoment
================

The function :aimms:func:`TimeSlotToMoment` calculates the elapsed time since a
specific reference date for a given time slot in a calendar.

.. code-block:: aimms

    TimeSlotToMoment(
         Calendar,        ! (input) a calendar
         ReferenceDate,   ! (input) an element (time-slot) in the calendar
         Timeslot         ! (input) an element (time-slot) in the calendar
         )

Arguments
---------

    *Calendar*
        An identifier of type calendar.

    *ReferenceDate*
        A specific time-slot in *Calendar* holding the reference time.

    *Timeslot*
        A specific time slot in the calendar.

Return Value
------------

    The function :aimms:func:`TimeSlotToMoment` returns the elapsed time since the
    reference date for the given time slot (measured in the calendar's
    unit).

.. seealso::

    The functions :aimms:func:`MomentToTimeSlot`, :aimms:func:`CurrentToTimeSlot`, :aimms:func:`StringToTimeSlot`.
