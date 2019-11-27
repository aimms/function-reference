.. aimms:function:: MomentToTimeSlot(Calendar, ReferenceDate, Elapsed)

.. _MomentToTimeSlot:

MomentToTimeSlot
================

The function :aimms:func:`MomentToTimeSlot` determines the time slot in a calendar
that corresponds with the a moment that is specified as the elapsed time
since a specific reference date.

.. code-block:: aimms

    MomentToTimeSlot(
         Calendar,           ! (input) a calendar
         ReferenceDate,      ! (input) an element (time-slot) in the calendar
         Elapsed             ! (input) a numerical value
         )

Arguments
---------

    *Calendar*
        An identifier of type calendar.

    *ReferenceDate*
        A specific time-slot in *Calendar* holding the reference time.

    *Elapsed*
        The elapsed time since *ReferenceDate*. This should be an integral
        multiple of the calendar's time unit in order to select the time slot
        that is the return value of this function.

Return Value
------------

    The function :aimms:func:`MomentToTimeSlot` returns the time slot in the calendar
    that contains the given moment. When the time slot is outside the
    calendar the empty element is returned.

.. seealso::

    The functions :aimms:func:`TimeSlotToMoment`, :aimms:func:`CurrentToTimeSlot`, :aimms:func:`StringToTimeSlot`.
