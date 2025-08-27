.. aimms:function:: CurrentToTimeSlot(Calendar)

.. _CurrentToTimeSlot:

CurrentToTimeSlot
=================

The function :aimms:func:`CurrentToTimeSlot` determines the time slot in a
calendar that corresponds with the current time.

.. code-block:: aimms

    CurrentToTimeSlot(
         Calendar           ! (input) a calendar
         )

Arguments
---------

    *Calendar*
        An identifier of type calendar.

Return Value
------------

    The function :aimms:func:`CurrentToTimeSlot` returns the time slot in the calendar
    that contains the current moment.

.. note::

    There is an option ``Current_Time_in_LocalDST`` that specifies whether
    this function takes into account the effects of daylight savings time.



Example
-----------

Given the following declarations:


.. code-block:: aimms

	Calendar cal_DaysLongGone {
		Index: i_dayGone;
		Unit: day;
		BeginDate: "2000-01-01";
		EndDate: "2000-12-31";
		TimeslotFormat: "%c%y-%m-%d";
	}
	Calendar cal_ForALongTime {
		Index: i_day;
		Unit: day;
		BeginDate: "2024-01-01";
		EndDate: "2064-12-31";
		TimeslotFormat: "%c%y-%m-%d";
	}

The code

.. code-block:: aimms

	ep_past := CurrentToTimeSlot( cal_DaysLongGone );
	ep_curr := CurrentToTimeSlot( cal_ForALongTime );
	display ep_past, ep_curr ;

results in

.. code-block:: aimms

    ep_past := '' ;
    ep_curr := '2024-07-15' ;

when this example was created.

.. seealso::

    - The functions :aimms:func:`StringToTimeSlot`, :aimms:func:`MomentToTimeSlot`.
