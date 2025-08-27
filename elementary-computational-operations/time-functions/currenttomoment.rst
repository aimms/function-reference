.. aimms:function:: CurrentToMoment(Unit, ReferenceDate)

.. _CurrentToMoment:

CurrentToMoment
===============

The function :aimms:func:`CurrentToMoment` converts the current time to the
elapsed time with respect to a specific reference date.

.. code-block:: aimms

    CurrentToMoment(
         Unit,                    ! (input) a time unit
         ReferenceDate            ! (input) a string expression
         )

Arguments
---------

    *Unit*
        The time unit that is used to return the elapsed time.

    *ReferenceDate*
        A string that holds the begin date using the fixed format for date and
        time, see paragraph :ref:`calendar.reference_date_format` of the Language
        Reference.

Return Value
------------

    The result of :aimms:func:`CurrentToMoment` is the elapsed time in *Unit* since
    *ReferenceDate*.

Example
-----------

Given the declarations:

.. code-block:: aimms

	Parameter _p_secs {
		Unit: s;
	}
	Parameter _p_mins {
		Unit: minute;
	}

The code

.. code-block:: aimms

	_p_secs := CurrentToMoment(
		Unit          :  [s], 
		Referencedate :  "2020-01-01 00:00:00");
	_p_mins := CurrentToMoment(
		Unit          :  [minute], 
		Referencedate :  "2020-01-01 00:00:00");
	display _p_secs, _p_mins ;

resulted in...

.. code-block:: aimms

    _p_secs := 142691236 [s] ;
    _p_mins := 2378187.267 [minute] ;

when this example was created.

.. seealso::

    -  The function :aimms:func:`StringToMoment`.

    -  :any:`Articles/144/144-Stopwatch`
       illustrates the use of some time functions. The purpose of
       :aimms:func:`CurrentToMoment` in that post is to compute the time since a
       starting point.
