.. aimms:function:: DepreciationNonLinearFactor(PurchaseDate, NextPeriodDate, Cost, Salvage, Life, Period, Factor, Basis, Mode)

.. _DepreciationNonLinearFactor:

DepreciationNonLinearFactor
===========================

The function :aimms:func:`DepreciationNonLinearFactor` returns the depreciation of
an asset for the specified period, using double-declining balance
depreciation or some other method you specify. The accounting periods
have a length of one year, but they don't necessary need to start
January 1. The depreciation amounts decline by the factor times a fixed
rate for every succeeding period. The higher the used factor, the sooner
the asset is totally depreciated.

.. code-block:: aimms

    DepreciationNonLinearFactor(
        PurchaseDate,             ! (input) scalar string expression
        NextPeriodDate,           ! (input) scalar string expression
        Cost,                     ! (input) numerical expression
        Salvage,                  ! (input) numerical expression
        Life,                     ! (input) numerical expression
        Period,                   ! (input) numerical expression
        Factor                    ! (input) numerical expression
        [Basis,]                  ! (optional) numerical expression
        [Mode]                    ! (optional) numerical expression
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

    *Life*
        The number of periods until the asset will be fully depreciated, also
        called the useful life of the asset. *Life* must be a positive integer.

    *Period*
        The period for which you want to compute the depreciation. *Period* an
        integer in the range :math:`\{1, Life + 1\}`. Period 1 is the (partial)
        period from *PurchaseDate* until *NextPeriodDate*.

    *Factor*
        The rate by which the depreciation declines is
        :math:`\frac{Factor}{Life}`. *Factor* must be a numerical expression in
        the range :math:`[1, \infty )`. In case :math:`Factor = 2` we define
        this method as double declining depreciation.

    *Basis*
        The day-count basis method to be used. The default is 1.

    *Mode*
        Specifies how partial periods will be handled. *Mode* must be binary.
        :math:`Mode = 0`: we just take a relatively equal part of the
        depreciation for a full year. This is mathematically incorrect, but is
        rather common in the financial world. :math:`Mode = 1`: the depreciation
        for the partial periods is calculated so that the asset exactly equals
        its Salvage after its useful life. The default is 0.

Return Value
------------

    The function :aimms:func:`DepreciationNonLinearFactor` returns the depreciation of
    an asset for the specified period.

Equation
--------

    The method-dependent depreciation :math:`\tilde{d_i}` is expressed by
    the equations

    .. math::

       \begin{aligned}
        \tilde{d_1} &= \begin{cases} f_{PN}rc & \mbox{for $\textit{Mode} = 0$}\\ \left(1-(1-r)^{f_{PN}}\right)c & \mbox{for $\textit{Mode} = 1$} \end{cases} \\ \tilde{d_i} &= (c-d_1)r(1-r)^{i-2} \qquad\qquad (i\neq 1) \end{aligned}

    \ where the depreciation rate :math:`r` equals

    .. math:: r = \frac{f}{L}

    with :math:`f` the *Factor* argument.

.. note::

    -  The useful life of the asset is determined by the *Factor* and *Life*
       arguments, and the requirement that the value of the asset can never
       drop below its salvage value.

    -  The function ``DepreciationLinearNonFactor`` is similar to the Excel
       function ``DDB``.



Example
-------

Using ``DepreciationNonLinearFactor`` for declining depreciation over a period of 10 years:
 

.. code-block:: aimms

    _p_life := 10 ;
    _s_periods := ElementRange(1,_p_life+1  );
    _p_deprec( _i_per ) := DepreciationNonLinearFactor(
        PurchaseDate     :  "2024-03-01", 
        NextPeriodDate   :  "2025-01-01", 
        Cost             :  1e5, 
        Salvage          :  1e4, 
        Life             :  _p_life,
        Period           :  _i_per, 
        Factor           :  2,
        Basis            :  1);
    _p_totDeprec := sum( _i_per, _p_deprec( _i_per ) );
    block where single_column_display := 1, listing_number_precision := 6 ;
        display _p_deprec( _i_per ) ;
    endblock ;

The actual values computed are:

.. code-block:: aimms

    _p_deprec(_i_per) := data 
    {  1 : 16666.666667,
       2 : 16666.666667,
       3 : 13333.333333,
       4 : 10666.666667,
       5 :  8533.333333,
       6 :  6826.666667,
       7 :  5461.333333,
       8 :  4369.066667,
       9 :  3495.253333,
      10 :  2796.202667,
      11 :  1184.810667 } ;





References
-----------

    *   Day count basis :ref:`methods<ff.dcb>`. 
    
    *   General equations for computing :ref:`depreciations<FF.depreq>`.

