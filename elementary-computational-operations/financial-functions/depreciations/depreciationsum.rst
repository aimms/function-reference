.. aimms:function:: DepreciationSum(PurchaseDate, NextPeriodDate, Cost, Salvage, Life, StartPeriod, EndPeriod, Factor, Basis, Mode, Switch)

.. _DepreciationSum:

DepreciationSum
===============

The function :aimms:func:`DepreciationSum` returns the depreciation of an asset
for the specified interval, using factor-declining depreciation. The
accounting periods have a length of one year, but they don't necessary
need to start January 1. A parameter Switch is used to indicated that,
when straight-line depreciation results in greater depreciation than
factor-declining depreciation, the calculation of the depreciation has
to be based on that method.

.. code-block:: aimms

    DepreciationSum(
        PurchaseDate,             ! (input) scalar string expression
        NextPeriodDate,           ! (input) scalar string expression
        Cost,                     ! (input) numerical expression
        Salvage,                  ! (input) numerical expression
        Life,                     ! (input) numerical expression
        StartPeriod,              ! (input) numerical expression
        EndPeriod,                ! (input) numerical expression
        Factor,                   ! (input) numerical expression
        [Basis,]                  ! (optional) numerical expression
        [Mode,]                   ! (optional) numerical expression
        [Switch]                  ! (optional) numerical expression
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

    *StartPeriod*
        The starting period of the interval, for which you want to compute the
        sum of depreciation, this may also indicate a partial period.
        *StartPeriod* must be an integer in the range :math:`\{1, Life\}`.
        *StartPeriod* must have the same unit as *Life*.

    *EndPeriod*
        The last period of the interval, for which you want to compute the sum
        of depreciation. *EndPeriod* must be an integer in the range
        :math:`\{StartPeriod, Life\}`. *EndPeriod* must have the same unit as
        *Life*.

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

    *Switch*
        Indicates whether to switch to straight-line depreciation when the
        depreciation amounts will be higher applying that method, or not to
        switch. *Switch* must be binary. If :math:`Switch = 0`: do not switch,
        if :math:`Switch = 1`: switch. The default is 1.

Return Value
------------

    The function :aimms:func:`DepreciationSum` returns the depreciation of an asset
    for the specified period.

.. note::

    The function :aimms:func:`DepreciationSum` is similar to the Excel function
    `VDB <https://support.microsoft.com/en-us/office/vdb-function-dde4e207-f3fa-488d-91d2-66d55e861d73>`_.

Example
-------

Using ``DepreciationSum`` for declining depreciation over a period of 10 years:
 

.. code-block:: aimms

    _p_life := 10 ;
    _s_periods := ElementRange(1,_p_life  );
    _p_deprec( _i_per ) := DepreciationSum(
        PurchaseDate   :  "2024-03-01", 
        NextPeriodDate :  "2025-01-01", 
        Cost           :  1e5, 
        Salvage        :  1e4, 
        Life           :  _p_life, 
        StartPeriod    :  _i_per, 
        EndPeriod      :  _i_per, 
        Factor         :  2, 
        Basis          :  1, 
        Mode           :  1, 
        Switch         :  1);
    _p_totDeprec := sum( _i_per, _p_deprec( _i_per ) );
    block where single_column_display := 1, listing_number_precision := 6 ;
        display _p_deprec( _i_per ) ;
    endblock ;

The actual values computed are:

.. code-block:: aimms

    _p_deprec(_i_per) := data 
    {  1 : 16968.734756,
       2 : 16606.253049,
       3 : 13285.002439,
       4 : 10628.001951,
       5 :  8502.401561,
       6 :  6801.921249,
       7 :  5441.536999,
       8 :  4353.229599,
       9 :  3706.459199,
      10 :  3706.459199 } ;

References
-----------


    *   The functions :aimms:func:`DepreciationNonLinearFactor`, :aimms:func:`DepreciationLinearLife`. 
    
    *   Day count basis :ref:`methods<ff.dcb>`. 
    
    *   General equations for computing :ref:`depreciations<FF.depreq>`.
