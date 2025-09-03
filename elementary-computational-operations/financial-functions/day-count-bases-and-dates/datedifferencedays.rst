.. aimms:function:: DateDifferenceDays(FirstDate, SecondDate, Basis)

.. _DateDifferenceDays:

DateDifferenceDays
==================

The function :aimms:func:`DateDifferenceDays` calculates the number of days
between two dates based on the specified day count basis.

.. code-block:: aimms

    DateDifferenceDays(
        FirstDate,             ! (input) scalar string expression
        SecondDate,            ! (input) scalar string expression
        [Basis]                ! (optional) numerical expression
        )

Arguments
---------

    *FirstDate*
        The first date must be in date format.

    *SecondDate*
        The second date must be in date format, and later than *FirstDate*.

    *Basis*
        The day-count basis method to be used. The default is 1.

Return Value
------------

    The function :aimms:func:`DateDifferenceDays` returns the number of days between
    the two dates.

.. note::

    The function :aimms:func:`DateDifferenceDays` is similar to the Excel function
    ``DAYS300``.

Example
--------

The code

.. code-block:: aimms

    _p_r1 := DateDifferenceDays( "2024-02-01", "2024-03-01", 1 );  
    _p_r2 := DateDifferenceDays( "2024-02-01", "2024-03-01", 2 );  
    _p_r3 := StringToMoment(
        Format        :  "%c%y-%m-%d", 
        Unit          :  [day], 
        ReferenceDate :  "2024-02-01", 
        Timeslot      :  "2024-03-01");

    block where listing_number_precision := 6 ;
        display _p_r1, _p_r2, _p_r3  ;
    endblock ;
   
results in:

.. code-block:: aimms

    _p_r1 := 30 ;
    _p_r2 := 29 ;
    _p_r3 := 29 [day] ;

Remarks:

    #.  The default method of ``DateDifferenceDays`` uses 30 days per month, so one month results in 30.
    
    #.  The more advanced method, method 2, uses the actual number of days per month.

    #.  :aimms:func:`MomentToString` can do the same, but also supports other time units including ``second``.
        Note that the result of this function has a time unit.

.. seealso::

    *   Day count basis :ref:`methods<ff.dcb>`.

    *   :aimms:func:`MomentToString` function.

