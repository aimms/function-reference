.. aimms:function:: ConvertReferenceDate(ReferenceDate, FromTimezone, ToTimezone, IgnoreDST)

.. _ConvertReferenceDate:

ConvertReferenceDate
====================

The function :aimms:func:`ConvertReferenceDate` converts a reference date from one
timezone to the other.

.. code-block:: aimms

    ConvertReferenceDate(
         ReferenceDate,          ! (input) a string expression
         FromTimezone,           ! (input) an element expression
         ToTimezone,             ! (input) an element expression
         IgnoreDST               ! (optional) a numerical expression (default 0)
         )

Arguments
---------

    *ReferenceDate*
        A string that holds a reference date in *FromTimezone*.

    *FromTimezone*
        An element of :aimms:set:`AllTimeZones` with respect to which *ReferenceDate* is
        expressed.

    *ToTimezone*
        An element of :aimms:set:`AllTimeZones` with respect to which the resulting reference
        date must be expressed.

    *IgnoreDST*
        A numerical expression indicating whether daylight saving time must be
        ignored in the conversion.

Return Value
------------

    The result of :aimms:func:`ConvertReferenceDate` is a reference date in
    *ToTimezone* corresponding to the reference date *ReferenceDate* in
    *FromTimezone*.


Example
-----------

Given a selection of timezones

.. code-block:: aimms

	! Picking a few timezones relative to me.
	_ep_CETTZ    := 'Central European Standard Time' ; ! Where I live.
	_ep_BrazilTZ := 'Central Brazilian Standard Time' ; 
	_ep_IndianTZ := 'India Standard Time' ;


Wondering what time it is in the other timezones when I wake up:

.. code-block:: aimms

	_sp_wakeup := "2020-04-01 06:00" ; ! My alarm rings at 6 AM  
	_sp_refUTC := ConvertReferenceDate(
		ReferenceDate :  _sp_wakeup, 
		FromTZ        :  _ep_CETTZ, 
		ToTZ          :  'UTC', 
		IgnoreDST     :  1);
	_sp_refBrazil := ConvertReferenceDate(
		ReferenceDate :  _sp_wakeup, 
		FromTZ        :  _ep_CETTZ, 
		ToTZ          :  _ep_BrazilTZ, 
		IgnoreDST     :  1);
	_sp_refInda := ConvertReferenceDate(
		ReferenceDate :  _sp_wakeup, 
		FromTZ        :  _ep_CETTZ, 
		ToTZ          :  _ep_IndianTZ, 
		IgnoreDST     :  1);
	display _sp_refUTC, _sp_refBrazil, _sp_refInda ;

Without considering daylight saving time, the result is:

.. code-block:: aimms

    _sp_refUTC    := "2020-04-01 05:00" ;
    _sp_refBrazil := "2020-04-01 01:00" ;
    _sp_refInda   := "2020-04-01 10:30" ;


.. seealso::

    AIMMS support for time zones is discussed in full detail in :ref:`sec:time.format.dst` 
    and :doc:`advanced-language-components/time-based-modeling/working-in-multiple-time-zones` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
