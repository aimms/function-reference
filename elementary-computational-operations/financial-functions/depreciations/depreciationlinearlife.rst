.. aimms:function:: DepreciationLinearLife(PurchaseDate, NextPeriodDate, Cost, Salvage, Life, Period, Basis)

.. _DepreciationLinearLife:

DepreciationLinearLife
======================

The function :aimms:func:`DepreciationLinearLife` returns the depreciation of an
asset for the specified period, using straight-line depreciation. The
accounting periods have a length of one year, but they don't necessary
need to start January 1. The depreciation amounts are equal for every
period. In case of partial periods, a relatively equal part must be
depreciated.

.. code-block:: aimms

    DepreciationLinearLife(
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

    The function :aimms:func:`DepreciationLinearLife` returns the depreciation of an
    asset for the specified period.

Equation
--------

    The method-dependent depreciation :math:`\tilde{d_i}` is expressed by
    the equation

    .. math::

       \begin{aligned}
        \tilde{d_1} &=f_{PN}\frac{c-s}{L}\\ \tilde{d_i} &= \frac{c-s}{L} \qquad (i \neq 1). \end{aligned}

.. note::

    The function :aimms:func:`DepreciationLinearLife` is similar to the Excel function
    `SLN <https://support.microsoft.com/en-us/office/sln-function-cdb666e5-c1c6-40a7-806a-e695edc2f1c8>`_.



Example
-------

The following code illustrates how to compute the linear depreciation for each period of an investment 
initially costing 100.000, at the end of its useful life having value of 10.000,
over a period of 10 years.

.. code-block:: aimms

	_p_life := 10 ;
	_s_periods := ElementRange(1,_p_life +1 );
	_p_deprec( _i_per ) := DepreciationLinearLife(
		PurchaseDate   :  "2024-03-01", 
		NextPeriodDate :  "2025-01-01", 
		Cost           :  1e5, 
		Salvage        :  1e4, 
		Life           :  10, 
		Period         :  _i_per, 
		Basis          :  1);
	_p_totDeprec := sum( _i_per, _p_deprec( _i_per ) );

	block where single_column_display := 1 ;
		display _p_deprec( _i_per ) ;
	endblock ;

The actual values computed are:

.. code-block:: aimms

    _p_deprec(_i_per) := data 
    {  1 : 7500,
       2 : 9000,
       3 : 9000,
       4 : 9000,
       5 : 9000,
       6 : 9000,
       7 : 9000,
       8 : 9000,
       9 : 9000,
      10 : 9000,
      11 : 1500 } ;

As you can see, the depreciation of the first and last period add up to the 
depreciation for a single year.

.. seealso::

    *   Day count basis :ref:`methods<ff.dcb>`. 
    
    *   General equations for computing :ref:`depreciations<FF.depreq>`.
