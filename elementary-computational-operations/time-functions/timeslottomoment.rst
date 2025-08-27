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
    reference date for the given time slot (measured in the calendar's unit).


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
	Parameter _p_noDaysToSecond {
		Unit: day;
	}
	Parameter _p_noDays {
		Unit: day;
	}
	ElementParameter _ep_first {
		Range: cal_days;
	}
	ElementParameter _ep_second {
		Range: cal_days;
	}
	ElementParameter _ep_last {
		Range: cal_days;
	}

The code

.. code-block:: aimms

	_ep_first := first( cal_days );
	_ep_second := element( cal_days, 2 );
	_ep_last := last( cal_days );
	_p_noDaysToSecond := TimeslotToMoment(
		Calendar      :  cal_days, 
		ReferenceDate :  _ep_first, 
		Timeslot      :  _ep_second);
	_p_noDays := TimeslotToMoment(
		Calendar      :  cal_days, 
		ReferenceDate :  _ep_first, 
		Timeslot      :  _ep_last);
	display _ep_first, _ep_last, _p_noDaysToSecond, _p_noDays ;


results in:

.. code-block:: aimms

    _ep_first := '2024-01-01' ;
    _ep_last := '2024-01-14' ;
    _p_noDaysToSecond := 1 [day] ;
    _p_noDays := 13 [day] ;


.. seealso::

    - The functions :aimms:func:`MomentToTimeSlot`, :aimms:func:`CurrentToTimeSlot`, :aimms:func:`StringToTimeSlot`.
