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

.. seealso::

    The procedures :aimms:procedure:`Aggregate`, :aimms:procedure:`DisAggregate`. For a more detailed description of
    the creation of timetables, see Section 33.4 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
