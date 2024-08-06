.. aimms:function:: DepreciationNonLinearRate(PurchaseDate, NextPeriodDate, Cost, Salvage, Period, DepreciationRate, Basis, Mode)

.. _DepreciationNonLinearRate:

DepreciationNonLinearRate
=========================

The function :aimms:func:`DepreciationNonLinearRate` returns the depreciation of
an asset for the specified period, using factor-declining depreciation.
The *DepreciationRate* determines the factor. The accounting periods
have a length of one year, but they don't necessary need to start
January 1.

.. code-block:: aimms

    DepreciationNonLinearRate(
        PurchaseDate,             ! (input) scalar string expression
        NextPeriodDate,           ! (input) scalar string expression
        Cost,                     ! (input) numerical expression
        Salvage,                  ! (input) numerical expression
        Period,                   ! (input) numerical expression
        DepreciationRate,         ! (input) numerical expression
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

    *Period*
        The period for which you want to compute the depreciation. *Period* an
        integer in the range :math:`\{1, Life + 1\}`. Period 1 is the (partial)
        period from *PurchaseDate* until *NextPeriodDate*.

    *DepreciationRate*
        The value of the asset declines every period by an amount equal to the
        depreciation rate times the *Cost*. *DepreciationRate* must be a
        numerical expression in the range :math:`[0, \frac{1}{2})`.

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

    The function :aimms:func:`DepreciationNonLinearRate` returns the depreciation of
    an asset for the specified period.

Equation
--------

    The method-dependent depreciation :math:`\tilde{d_i}` is expressed by
    the equations

    .. math::

       \begin{aligned}
        \tilde{d_1} &= \begin{cases} f_{PN}rfc & \mbox{for $\textit{Mode} = 0$}\\ \left(1-(1-rf)^{f_{PN}}\right)c & \mbox{for $\textit{Mode} = 1$} \end{cases} \\ \tilde{d_i} &= \begin{cases} rfv_i & ( 1 < i < \tilde{L} - 1) \\ \frac{1}{2}v_i & (i = \tilde{L} - 1) \\ v_i - s & ( i = \tilde{L} ) \end{cases} \end{aligned}

    \ where :math:`r` is the *DepreciationRate*,
    :math:`\tilde{L} = \lceil 1/r\rceil` the useful life of the asset, and
    the depreciation coefficient :math:`f` is determined by

    .. math:: f = \begin{cases} 1.5 & \mbox{for $\frac{1}{4} \leq r < \frac{1}{2}$}\\ 2.0 & \mbox{for $\frac{1}{6} \leq r < \frac{1}{4}$}\\ 2.5 & \mbox{for $r < \frac{1}{6}$}\\ \end{cases}

.. note::

    The function ``DepreciationLinearNonRate`` is similar to the Excel
    function `AMORDEGRC <https://support.microsoft.com/en-us/office/amordegrc-function-a14d0ca1-64a4-42eb-9b3d-b0dededf9e51>`_.



Example
-------

Using ``pr_testDepreciationNonLinearRate`` for declining depreciation over a period of 10 years:
 

.. code-block:: aimms

	_p_life := 10 ;
	_s_periods := ElementRange(1,_p_life  );
	_p_deprec( _i_per ) := DepreciationNonLinearRate(
		PurchaseDate     :  "2024-03-01", 
		NextPeriodDate   :  "2025-01-01", 
		Cost             :  1e5, 
		Salvage          :  1e4, 
		Period           :  _i_per, 
		DepreciationRate :  0.1,
		Basis            :  1,
		Mode             :  1);
	_p_totDeprec := sum( _i_per, _p_deprec( _i_per ) );
	block where single_column_display := 1, listing_number_precision := 6 ;
		display _p_deprec( _i_per ) ;
	endblock ;

The actual values computed are:

.. code-block:: aimms

    _p_deprec(_i_per) := data 
    { 1 : 21316.370243,
      2 : 19670.907439,
      3 : 14753.180579,
      4 : 11064.885435,
      5 :  8298.664076,
      6 :  6223.998057,
      7 :  4667.998543,
      8 :  3500.998907,
      9 :   502.996721 } ;

References
-----------

    *   Day count basis :ref:`methods<ff.dcb>`. 
    
    *   General equations for computing :ref:`depreciations<FF.depreq>`.


