.. aimms:function:: DaylightSavingStartDate(Year, Timezone)

.. _DaylightSavingStartDate:

DaylightSavingStartDate
=======================

The function :aimms:func:`DaylightSavingStartDate` computes the start date of
daylight saving time for a particular year in a particular time zone.

.. code-block:: aimms

    DaylightSavingStartDate(
         Year,                    ! (input) an element expression
         Timezone                 ! (input) an element expression
         )

Arguments
---------

    *Year*
        An element of a yearly calendar for the end date of daylight saving time
        must be computed.

    *Timezone*
        An element in the predefined set :aimms:set:`AllTimeZones`.

Return Value
------------

    The result of :aimms:func:`DaylightSavingStartDate` is the start date of daylight
    saving time, as a reference date, for the time zone *Timezone* in the
    year *Year*.




Example
-----------

Given the declarations:

.. code-block:: aimms

    Calendar cal_years {
        Index: i_year;
        Unit: year;
        BeginDate: "2024";
        EndDate: "2024";
        TimeslotFormat: "%c%y";
    }
    ElementParameter ep_year {
        Range: cal_years;
    }

Then the code


.. code-block:: aimms

    ep_year := first( cal_years );
    _sp_startDaylightSaving2024 := DaylightSavingStartDate( ep_year, 
        'Central European Standard Time' );
    display _sp_startDaylightSaving2024 ;

results in:

.. code-block:: aimms

    _sp_startDaylightSaving2024 := "2024-03-31 02" ;



.. seealso::

    - AIMMS support for time zones is discussed in full detail in :ref:`sec:time.format.dst` 
    - :doc:`advanced-language-components/time-based-modeling/working-in-multiple-time-zones`.
