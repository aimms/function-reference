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
        end of the period, see :doc:`advanced-language-components/time-based-modeling/format-of-time-slots-and-periods`

    *Timetable*
        An indexed set in a calendar and defined over a horizon.

    *Period*
        An element in the horizon that is defined by *Timetable*.

Return Value
------------

    The result of :aimms:func:`PeriodToString` is a string describing the
    corresponding moment according to *Format*.



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
	Horizon s_horizon {
		Index: i_hor;
		CurrentPeriod: ep_currentPeriod;
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
	StringParameter sp_periodName {
		IndexDomain: i_hor;
	}

And the data preparation:

.. code-block:: aimms

	ep_currentTimeSlot := element( cal_days, 2 );
	ep_currentPeriod := element( s_horizon, 2 );
	CreateTimeTable(
		TimeTable         :  s_timetable, 
		CurrentTimeSlot   :  ep_currentTimeSlot, 
		CurrentPeriod     :  ep_currentPeriod, 
		PeriodLength      :  p_periodLength, 
		LengthDominates   :  bp_lengthDominates, 
		InactiveTimeSlots :  s_inactiveTimeSlots, 
		DelimiterSlots    :  s_delimiterSlots);

The code

.. code-block:: aimms

	sp_periodName( i_hor in s_horizon ) :=
		PeriodToString(
			Format    :  "%B%Aw|AllAbbrWeekdays| %Am|AllAbbrMonths| %d, %c%y - %I%Aw|AllAbbrWeekdays| %Am|AllAbbrMonths| %d, %c%y", 
			Timetable :  s_timetable, 
			Period    :  i_hor);
	block where single_column_display := 1;
		display s_timetable ;
		display sp_periodName ;
	endblock ;

Prints the following in the listing file:

.. code-block:: aimms

    s_timetable := data 
    { p0 : { 2024-01-01 } ,
      p1 : { 2024-01-02, 2024-01-03 } ,
      p2 : { 2024-01-04, 2024-01-05, 2024-01-06 } ,
      p3 : { 2024-01-07, 2024-01-08, 2024-01-09, 2024-01-10 } ,
      p4 : { 2024-01-11, 2024-01-12, 2024-01-13, 2024-01-14 } } ;


    sp_periodName := data 
    { p0 : "Mon Jan 01, 2024 - Mon Jan 01, 2024",
      p1 : "Tue Jan 02, 2024 - Wed Jan 03, 2024",
      p2 : "Thu Jan 04, 2024 - Sat Jan 06, 2024",
      p3 : "Sun Jan 07, 2024 - Wed Jan 10, 2024",
      p4 : "Thu Jan 11, 2024 - Sun Jan 14, 2024" } ;


.. seealso::

    The procedure :aimms:procedure:`CreateTimeTable`.
