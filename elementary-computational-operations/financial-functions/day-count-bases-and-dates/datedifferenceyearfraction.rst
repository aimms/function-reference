.. aimms:function:: DateDifferenceYearFraction(FirstDate, SecondDate, Basis)

.. _DateDifferenceYearFraction:

DateDifferenceYearFraction
==========================

The function :aimms:func:`DateDifferenceYearFraction` calculates the year fraction
between two dates based on the specified day count basis.

.. code-block:: aimms

    DateDifferenceYearFraction(
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

    The function :aimms:func:`DateDifferenceYearFraction` returns the difference
    between *FirstDate* and *SecondDate* in fractions of a year.

.. note::

    The function :aimms:func:`DateDifferenceYearFraction` is similar to the Excel
    function ``YEARFRAC``.


Example
--------

The following code illustrates the differences between the various methods supported.

.. code-block:: aimms

    ! Method 1: each month is always 1/12 of a year.
    _p_r1 := DateDifferenceYearFraction( "2024-02-01", "2024-03-01", 1 );  
    _p_r1e := 1 / 12 ;

    ! Method 2: use actual number of days per month and per year (here leap year).
    _p_r2 := DateDifferenceYearFraction( "2024-02-01", "2024-03-01", 2 );
    _p_r2e := 29 / 366 ;
    _p_r2t := StringToMoment(
            Format        :  "%c%y-%m-%d", 
            Unit          :  [day], 
            ReferenceDate :  "2024-02-01", 
            Timeslot      :  "2024-03-01") /
           StringToMoment(
            Format        :  "%c%y-%m-%d", 
            Unit          :  [day], 
            ReferenceDate :  "2024-01-01", 
            Timeslot      :  "2025-01-01") ;

    ! Method 3: use actual number of days per month, but always 360 days per year.
    _p_r3 := DateDifferenceYearFraction( "2024-02-01", "2024-03-01", 3 );  
    _p_r3e := 29 / 360 ;

    ! Method 4: use actual number of days per month, but always 365 days per year.
    _p_r4 := DateDifferenceYearFraction( "2024-02-01", "2024-03-01", 4 );
    _p_r4e := 29 / 365 ;

    ! Method 5: the European variation of method 1.
    _p_r5 := DateDifferenceYearFraction( "2024-02-01", "2024-03-01", 5 );  
    _p_r5e := 1 / 12 ;

    block where listing_number_precision := 6 ;
        display { _p_r1, _p_r1e }, { _p_r2, _p_r2e, _p_r2t }, { _p_r3, _p_r3e }, { _p_r4, _p_r4e }, { _p_r5, _p_r5e } ;
    endblock ;

and the results illustrate that there are small but significant differences:

.. code-block:: aimms

    _p_r1  := 0.083333 ;
    _p_r1e := 0.083333 ;

    _p_r2  := 0.079235 ;
    _p_r2e := 0.079235 ;
    _p_r2t := 0.079235 ;

    _p_r3  := 0.080556 ;
    _p_r3e := 0.080556 ;

    _p_r4  := 0.079452 ;
    _p_r4e := 0.079452 ;

    _p_r5  := 0.083333 ;
    _p_r5e := 0.083333 ;



References
-----------

    *   Day count basis :ref:`methods<ff.dcb>`.


