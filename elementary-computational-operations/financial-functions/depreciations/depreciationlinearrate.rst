.. aimms:function:: DepreciationLinearRate(PurchaseDate, NextPeriodDate, Cost, Salvage, Period, DepreciationRate, Basis)

.. _DepreciationLinearRate:

DepreciationLinearRate
======================

The function :aimms:func:`DepreciationLinearRate` returns the depreciation of an
asset for the specified period, using linear depreciation. The
accounting periods have a length of one year, but they don't necessary
need to start January 1. The sum of the depreciation amounts of all
periods cannot be higher than the difference between the cost and the
salvage.

.. code-block:: aimms

    DepreciationLinearRate(
        PurchaseDate,             ! (input) scalar string expression
        NextPeriodDate,           ! (input) scalar string expression
        Cost,                     ! (input) numerical expression
        Salvage,                  ! (input) numerical expression
        Period,                   ! (input) numerical expression
        DepreciationRate,         ! (input) numerical expression
        [Basis]                   ! (optional) numerical expression
        )

Arguments
---------

    *PurchaseDate*
        The date of purchase of the asset. *PurchaseDate* must be given in a
        date format. This is the first day that there will be depreciated.

    *NextPeriodDate*
        The next date after the balance is drawn up. *NextPeriodDate* must also
        be in date format. *NextPeriodDate* is the first day of a new period and
        must be further in time than *PurchaseDate*, but not more than one year
        after *PurchaseDate*. When *NextPeriodDate* is an empty string, it will
        get the default value of January 1st of the next year after purchase.

    *Cost*
        The purchase or initial cost of the asset. *Cost* must be a positive
        number.

    *Salvage*
        The value of the asset at the end of its useful life. *Salvage* must be
        a scalar numerical expression in the range :math:`[0, Cost)`.

    *Period*
        The period for which you want to compute the depreciation. *Period* must
        be a positive integer. Period 1 is the (partial) period from
        *PurchaseDate* until *NextPeriodDate*.

    *DepreciationRate*
        The value of the asset declines every period by an amount equal to the
        depreciation rate times the *Cost*. *DepreciationRate* must be a
        numerical expression in the range :math:`[0, \frac{1}{2})`.

    *Basis*
        The day-count basis method to be used. The default is 1.

Return Value
------------

    The function :aimms:func:`DepreciationLinearRate` returns the depreciation of an
    asset for the specified period.

Equation
--------

    The method-dependent depreciation :math:`\tilde{d_i}` is expressed by
    the equation

    .. math::

       \begin{aligned}
        \tilde{d_1} &=f_{PN}rc\\ \tilde{d_i} &=rc \qquad (i \neq 1) \end{aligned}

    \ where :math:`r` is the depreciation rate.

.. note::

    -  The useful life of the asset is determined by the depreciation rate,
       and the requirement that the value of the asset can never drop below
       its salvage value.

    -  The function :aimms:func:`DepreciationLinearRate` is similar to the Excel
       function `AMORLINC <https://support.microsoft.com/en-us/office/amorlinc-function-7d417b45-f7f5-4dba-a0a5-3451a81079a8>`_.


Example
-------

The following code illustrates how to compute the linear depreciation for each period of an investment 
initially costing 100.000, at the end of its useful life having value of 10.000,
with a constant rate of 10%.

.. code-block:: aimms

    _p_life := 10 ;
    _s_periods := ElementRange(1,_p_life  );
    _p_deprec( _i_per ) := DepreciationLinearRate(
        PurchaseDate     :  "2024-03-01", 
        NextPeriodDate   :  "2025-01-01", 
        Cost             :  1e5, 
        Salvage          :  1e4, 
        Period           :  _i_per, 
        DepreciationRate :  0.1,
        Basis            :  1);
    _p_totDeprec := sum( _i_per, _p_deprec( _i_per ) );
    block where single_column_display := 1, listing_number_precision := 6 ;
        display _p_deprec( _i_per ) ;
    endblock ;

The actual values computed are:

.. code-block:: aimms

    _p_deprec(_i_per) := data 
    {  1 :  8333.333333,
       2 : 10000.000000,
       3 : 10000.000000,
       4 : 10000.000000,
       5 : 10000.000000,
       6 : 10000.000000,
       7 : 10000.000000,
       8 : 10000.000000,
       9 : 10000.000000,
      10 :  1666.666667 } ;



.. seealso::

    *   Day count basis :ref:`methods<ff.dcb>`. 
    
    *   General equations for computing :ref:`depreciations<FF.depreq>`.

