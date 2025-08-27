.. aimms:function:: StringToTimeSlot(Format, Calendar, MomentString)

.. _StringToTimeSlot:

StringToTimeSlot
================

The function :aimms:func:`StringToTimeSlot` determines the time slot in a calendar
that corresponds with the a moment that is specified using a free format
string.

.. code-block:: aimms

    StringToTimeSlot(
         Format,         ! (input) a string expression
         Calendar,       ! (input) a calendar
         MomentString    ! (input) a string expression
         )

Arguments
---------

    *Format*
        A string that holds the date and time format used in the third argument
        *MomentString*. Valid format strings are described in :doc:`advanced-language-components/time-based-modeling/format-of-time-slots-and-periods`.

    *Calendar*
        An identifier of type calendar.

    *MomentString*
        A string expression of the moment (using the format given in ``Format``)
        that should be matched with the time slots in the calendar.

Return Value
------------

    The function :aimms:func:`StringToTimeSlot` returns the time slot in the calendar
    that contains the given moment.

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
	ElementParameter _ep_day {
		Range: cal_days;
	}
	ElementParameter _ep_tooLate {
		Range: cal_days;
	}

The code

.. code-block:: aimms

	_ep_day := StringToTimeSlot(
			Format       :  "%m-%d", 
			Calendar     :  cal_days, 
			MomentString :  "01-03");
	_ep_tooLate := StringToTimeSlot(
			Format       :  "%m-%d", 
			Calendar     :  cal_days, 
			MomentString :  "01-20");
	display _ep_day, _ep_tooLate ;

results in:

.. code-block:: aimms

    _ep_day := '2024-01-03' ;
    _ep_tooLate := '' ;


.. seealso::

    - The functions :aimms:func:`CurrentToTimeSlot`, :aimms:func:`MomentToTimeSlot`.
