.. aimms:function:: TimeSlotCharacteristic(Timeslot, Characteristic, Timezone, IgnoreDST)

.. _TimeSlotCharacteristic:

TimeSlotCharacteristic
======================

The function :aimms:func:`TimeSlotCharacteristic` obtains a numeric value which
characterizes the time slot, in terms of its day of the week, its day in
the year, etc.

.. code-block:: aimms

    TimeSlotCharacteristic(
         Timeslot,       ! (input) an element (time-slot) in a calendar
         Characteristic, ! (input) an element in TimeslotCharacteristics
         Timezone,       ! (optional) an element in AllTimeZones, default Local.
         IgnoreDST       ! (optional) 0-1 expression, default 0.
         )

Arguments
---------

    *Timeslot*
        A element refering to a time-slot in a calendar.

    *Characteristic*
        An element in the predefined set :aimms:set:`TimeSlotCharacteristics`, each element in this set
        refers to a specific value that can be retrieved for a time slot.

    *Timezone*
        A time zone from the predefined set :aimms:set:`AllTimeZones`.

    *IgnoreDST*
        A 0-1 expression indicating whether or not to ignore daylight savings
        time.

Return Value
------------

    The function :aimms:func:`TimeSlotCharacteristic` returns a numerical value for
    the requested time slot characteristic.

.. seealso::

    The function :aimms:func:`TimeSlotCharacteristic` is discussed in full detail in
    Section 33.4 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
