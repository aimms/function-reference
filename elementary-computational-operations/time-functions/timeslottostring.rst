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
        string. Valid format strings are described in :doc:`advanced-language-components/time-based-modeling/format-of-time-slots-and-periods`

    *Calendar*
        An identifier of type calendar.

    *Timeslot*
        A specific time-slot in the calendar.

Return Value
------------

    The function :aimms:func:`TimeSlotToString` returns a string representation of the
    time slot.

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

The code:

.. code-block:: aimms

	_sp_day1 := TimeslotToString(
		Format   :  "%Aw|AllAbbrWeekDays| %Am|AllAbbrMonths| %d, %c%y", 
		Calendar :  cal_days, 
		Timeslot :  first(cal_days));
	display _sp_day1 ;

Results in:

.. code-block:: aimms

    _sp_day1 := "Mon Jan 01, 2024" ;

.. seealso::

    The functions :aimms:func:`MomentToString`, :aimms:func:`CurrentToTimeSlot`, :aimms:func:`StringToTimeSlot`.
