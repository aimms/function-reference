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



Example
-----------

Given the declarations:

.. code-block:: aimms

	Calendar cal_days {
		Index: i_day;
		Unit: day;
		BeginDate: "2024-01-01";
		EndDate: "2024-01-14";
		TimeslotFormat: "%c%y-%m-%d";
	}
	ElementParameter _ep_firstDay {
		Range: cal_days;
	}
	Parameter _p_dayNoInWeek;

The code

.. code-block:: aimms

	_ep_firstDay := first( cal_days );
	_p_dayNoInWeek := TimeslotCharacteristic(
		Timeslot       :  _ep_firstDay, 
		Characteristic :  'weekday' );
	display _p_dayNoInWeek ;

results in

.. code-block:: aimms

    _p_dayNoInWeek := 1 ;

indicating that the first day of the calendar is a Monday.


.. seealso::

    - The function :aimms:func:`TimeSlotCharacteristic` is discussed in full detail in :doc:`advanced-language-components/time-based-modeling/creating-timetables` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
