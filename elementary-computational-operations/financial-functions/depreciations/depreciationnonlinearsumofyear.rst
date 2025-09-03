.. aimms:function:: DepreciationNonLinearSumOfYear(PurchaseDate, NextPeriodDate, Cost, Salvage, Life, Period, Basis)

.. _DepreciationNonLinearSumOfYear:

DepreciationNonLinearSumOfYear
==============================

The function :aimms:func:`DepreciationNonLinearSumOfYear` returns the depreciation
of an asset for the specified period, using sum of years' digits
depreciation. The accounting periods have a length of one year, but they
don't necessary need to start January 1. The depreciation amounts
decline linear for every following period until the value reaches the
salvage.

.. code-block:: aimms

    DepreciationNonLinearSumOfYear(
        PurchaseDate,             ! (input) scalar string expression
        NextPeriodDate,           ! (input) scalar string expression
        Cost,                     ! (input) numerical expression
        Salvage,                  ! (input) numerical expression
        Life,                     ! (input) numerical expression
        Period,                   ! (input) numerical expression
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

    *Life*
        The number of periods until the asset will be fully depreciated, also
        called the useful life of the asset. *Life* must be a positive integer.

    *Period*
        The period for which you want to compute the depreciation. *Period* an
        integer in the range :math:`\{1, Life + 1\}`. Period 1 is the (partial)
        period from *PurchaseDate* until *NextPeriodDate*.

    *Basis*
        The day-count basis method to be used. The default is 1.

Return Value
------------

    The function :aimms:func:`DepreciationNonLinearSumOfYear` returns the depreciation
    of an asset for the specified period.

Equation
--------

    The method-dependent depreciation :math:`\tilde{d_i}` is expressed by
    the equation

    .. math::

       \begin{aligned}
        \tilde{d_1} &= \frac{c-s}{\frac{1}{2}L(L+1)}Lf_{PN} & \\ \tilde{d_i} &= \frac{c-s}{\frac{1}{2}L(L+1)}(L + 2 - i - f_{PN}) & \qquad (i\neq 1). \end{aligned}

.. note::

    The function :aimms:func:`DepreciationNonLinearSumOfYear` is similar to the Excel
    function `SYD <https://support.microsoft.com/en-us/office/syd-function-1be51f4f-62fc-4b9e-a000-b43e6c2ae86f>`_.


Example
-------

Using ``DepreciationNonLinearSumOfYear`` for declining depreciation over a period of 10 years:
 

.. code-block:: aimms

	_p_life := 10 ;
	_s_periods := ElementRange(1,_p_life+1  );
	_p_deprec( _i_per ) := DepreciationNonLinearSumOfYear(
		PurchaseDate     :  "2024-03-01", 
		NextPeriodDate   :  "2025-01-01", 
		Cost             :  1e5, 
		Salvage          :  1e4, 
		Life             :  _p_life,
		Period           :  _i_per, 
		Basis            :  1);
	_p_totDeprec := sum( _i_per, _p_deprec( _i_per ) );
	block where single_column_display := 1, listing_number_precision := 6 ;
		display _p_deprec( _i_per ) ;
	endblock ;

The actual values computed are:

.. code-block:: aimms

    _p_deprec(_i_per) := data 
    {  1 : 13636.363636,
       2 : 15000.000000,
       3 : 13363.636364,
       4 : 11727.272727,
       5 : 10090.909091,
       6 :  8454.545455,
       7 :  6818.181818,
       8 :  5181.818182,
       9 :  3545.454545,
      10 :  1909.090909,
      11 :   272.727273 } ;



.. seealso::
    
    *   Day count basis :ref:`methods<ff.dcb>`. 
    
    *   General equations for computing :ref:`depreciations<FF.depreq>`.
