.. aimms:function:: StringToMoment(Format, Unit, ReferenceDate, Timeslot)

.. _StringToMoment:

StringToMoment
==============

The function :aimms:func:`StringToMoment` converts a given time string (in a free
time format) to the elapsed time with a respect to a specific reference
date.

.. code-block:: aimms

    StringToMoment(
         Format,             ! (input) a string expression
         Unit,               ! (input) a time unit
         ReferenceDate,      ! (input) a string expression
         Timeslot            ! (input) a string expression
         )

Arguments
---------

    *Format*
        A string that holds the date and time format used in the fourth argument
        *Timeslot*. Valid format strings are described in :doc:`advanced-language-components/time-based-modeling/format-of-time-slots-and-periods`

    *Unit*
        The time unit that is used to return the elapsed time.

    *ReferenceDate*
        A string that holds the begin date using the fixed format for date and
        time, see paragraph :ref:`calendar.reference_date_format` of the Language
        Reference.

    *Timeslot*
        A string representing a specific date and time moment using the format
        specified in the first argument *Format*.

Return Value
------------

    The result of :aimms:func:`StringToMoment` is the elapsed time in *unit* between
    *reference-date* and *date*.


Example
-----------

The code:

.. code-block:: aimms

	_p_noSec := StringToMoment(
		Format        :  "%c%y-%m-%d %H:%M:%S%TZ('UTC')", 
		Unit          :  [s], 
		ReferenceDate :  "2020-01-01 09:30:30", 
		Timeslot      :  "2020-01-01 09:30:58");
	display _p_noSec ;

Reference dates are with respect to timezone 'UTC'.  
By default, timeslots are with respect to timezone 'Local'.
This timezone can be overridden in the format argument, as illustrated in this example.

Thus the result is:

.. code-block:: aimms

    _p_noSec := 28 [s] ;




.. seealso::

    The functions :aimms:func:`MomentToString`, :aimms:func:`CurrentToMoment`.
