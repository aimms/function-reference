.. aimms:procedure:: CreateTimeTable(Timetable, CurrentTimeslot, CurrentPeriod, PeriodLength, LengthDominates, InactiveTimeSlots, DelimiterSlots)

.. _CreateTimeTable:

CreateTimeTable
===============

With the procedure :aimms:procedure:`CreateTimeTable` you can create a timetable in
AIMMS.

.. code-block:: aimms

    CreateTimeTable(
         Timetable,             ! (output) an indexed set
         CurrentTimeslot,       ! (input) an element in a calendar
         CurrentPeriod,         ! (input) an element in a horizon
         PeriodLength,          ! (input) one-dimensional integer parameter
         LengthDominates,       ! (input) one-dimensional binary parameter
         InactiveTimeSlots,     ! (input) a subset of a calendar
         DelimiterSlots         ! (input) a subset of a calendar
         )

Arguments
---------

    *Timetable*
        An indexed set in a calendar and defined over the horizon to be linked
        to the calendar. This argument implicitly sets the calendar and horizon
        used for the creation of the timetable. The other arguments of the
        procedure should match with this calendar and horizon.

    *CurrentTimeslot*
        An element of a calendar (a time slot) that should be aligned with the
        *CurrentPeriod* in the horizon.

    *CurrentPeriod*
        An element of a horizon (a period) that should be aligned with the
        *timeslot* in the calendar.

    *PeriodLength*
        A one-dimensional integer parameter, specifying the desired length of
        each period in the horizon in terms of the number of time slots to be
        contained in it.

    *LengthDominates*
        A one-dimensional binary parameter, indicating whether reaching the
        specified *PeriodLength* dominates over the presence of any delimiter
        slot for every period in the horizon.

    *InactiveTimeSlots*
        A subset of the calendar, indicating the time slots that must be
        excluded from the timetable.

    *DelimiterSlots*
        A subset of the calendar, indicating the time slots that will (usually)
        result in starting a new period in the horizon.



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
	Set s_horizon {
		Index: i_hor;
		Definition: ElementRange(0,4,prefix:"p");
	}
	ElementParameter ep_currentTimeSlot {
		Range: cal_days;
	}
	ElementParameter ep_currentPeriod {
		Range: s_horizon;
	}
	Parameter p_periodLength {
		IndexDomain: i_hor;
		Definition: data { p0 : 1,  p1 : 2,  p2 : 3,  p3 : 4,  p4 : 4 };
	}
	Parameter bp_lengthDominates {
		IndexDomain: i_hor;
	}
	Set s_inactiveTimeSlots {
		SubsetOf: cal_days;
	}
	Set s_delimiterSlots {
		SubsetOf: cal_days;
	}
	Set s_timetable {
		IndexDomain: i_hor;
		SubsetOf: cal_days;
	}

The code:

.. code-block:: aimms

	ep_currentTimeSlot := element( cal_days, 2 );
	ep_currentPeriod := element( s_horizon, 2 );
	CreateTimeTable(
		TimeTable         :  s_timetable,         ! Timetable constructed
		CurrentTimeSlot   :  ep_currentTimeSlot,  ! Timeslot 2024-01-02 is linked to
		CurrentPeriod     :  ep_currentPeriod,    ! start of period p1.
		PeriodLength      :  p_periodLength,      ! Lengths are 1, 2, 3, 4, and 4 days  
		LengthDominates   :  bp_lengthDominates,  ! No length dominates
		InactiveTimeSlots :  s_inactiveTimeSlots, ! No inactive periods
		DelimiterSlots    :  s_delimiterSlots);   ! And no delimiter time slots.
	display s_timetable ;

creates the timetable:

.. code-block:: aimms

    s_timetable := data 
    { p0 : { 2024-01-01 } ,
      p1 : { 2024-01-02, 2024-01-03 } ,
      p2 : { 2024-01-04, 2024-01-05, 2024-01-06 } ,
      p3 : { 2024-01-07, 2024-01-08, 2024-01-09, 2024-01-10 } ,
      p4 : { 2024-01-11, 2024-01-12, 2024-01-13, 2024-01-14 } } ;




.. seealso::

    The procedures :aimms:procedure:`Aggregate`, :aimms:procedure:`DisAggregate`. For a more detailed description of
    the creation of timetables, see :doc:`advanced-language-components/time-based-modeling/creating-timetables` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
