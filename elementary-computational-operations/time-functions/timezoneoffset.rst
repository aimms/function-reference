.. aimms:function:: TimeZoneOffSet(FromTZ, ToTZ[, UseDST])

.. _TimeZoneOffSet:

TimeZoneOffSet
==============

The function :aimms:func:`TimeZoneOffSet` computes, in minutes, the offset between
two time zones.

.. code-block:: aimms

    TimeZoneOffSet(
         FromTZ,     ! (input) an element expression
         ToTZ        ! (input) an element expression
         [UseDST]    ! (optional) 0 or 1
         )

Arguments
---------

    *FromTZ*
        An element from the set :aimms:set:`AllTimeZones`.

    *ToTZ*
        An element from the set :aimms:set:`AllTimeZones`.

    *UseDST (optional)*
        A scalar expression specifying whether or not the current setting for
        daylight saving time (DST) in both time zones should be taken into
        account. The default is 0, indicating DST is not used.

Return Value
------------

    The result of :aimms:func:`TimeZoneOffSet` is the offset, in minutes, between
    *FromTZ* and *ToTZ*.

.. note::

    The result of the function has an associated unit, namely minutes. If
    *FromTZ* is UTC, the offset of *ToTZ* is the usual offset with respect
    to UTC (or GMT).


Example
-----------

Given the declarations:

.. code-block:: aimms

	Parameter p_tzOffset {
		IndexDomain: IndexTimezones;
		Unit: minute;
		Definition: TimezoneOffset('UTC',IndexTimeZones,0);
	}
	Set s_orderedTimeZones {
		SubsetOf: AllTimeZones;
		Index: i_otz;
		OrderBy: -p_tzOffset(IndexTimezones);
		Definition: Alltimezones-data{local,localdst};
	}

In these declarations/definitions, first the offset with respect to UTC is computed.
Based on that offset, the timezones are ordered.

The code:

.. code-block:: aimms

	block where single_column_display := 1;
		display p_tzOffset(i_otz) ;
	endblock ;

This display statement uses the ordering of timezones above, and the first few lines are:

.. code-block:: aimms

    ( p_tzOffset(i_otz) ) [minute] := data 
    { 'Line Islands Standard Time'      :  840,
      'Samoa Standard Time'             :  780,
      'Tonga Standard Time'             :  780,
      UTC+13                            :  780,
      'Chatham Islands Standard Time'   :  765,
      'Fiji Standard Time'              :  720,
      'Kamchatka Standard Time'         :  720,
      'New Zealand Standard Time'       :  720,
    ...


.. seealso::

    - AIMMS support for time zones is discussed in full detail in :ref:`sec:time.format.dst`.
    - :doc:`advanced-language-components/time-based-modeling/working-in-multiple-time-zones`.
