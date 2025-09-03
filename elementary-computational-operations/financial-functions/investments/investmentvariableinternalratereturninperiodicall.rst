.. aimms:function:: InvestmentVariableInternalRateReturnInPeriodicAll(Value, Date, Mode, IRR, NumberSolutions, Basis)

.. _InvestmentVariableInternalRateReturnInPeriodicAll:

InvestmentVariableInternalRateReturnInPeriodicAll
=================================================

The procedure :aimms:func:`InvestmentVariableInternalRateReturnInPeriodicAll`
returns the internal rate of return for an investment based on a series
of in-periodic cash flows. The internal rate of return is the interest
rate received for an investment.

.. code-block:: aimms

    InvestmentVariableInternalRateReturnInPeriodicAll(
        Value,                   ! (input) one-dimensional numerical expression
        Date,                    ! (input) one-dimensional string expression
        Mode,                    ! (input) numerical expression
        IRR,                     ! (output) one-dimensional numerical expression
        NumberOfSolutions,       ! (output) numerical expression
        [Basis]                  ! (optional) numerical expression
        )

Arguments
---------

    *Value*
        The payments (positive or negative). *Value* is an one-dimensional
        parameter of real numbers. *Value* given by positive numbers represent
        incoming amounts and *Value* given by negative numbers represent
        outgoing amounts. *Value* must contain at least one positive and at
        least one negative number.

    *Date*
        The dates on which the payments occur. *Date* and *Value* must have the
        same order. *Date* is an one-dimensional parameter of dates given in a
        date format. The first payment date indicates the beginning of the
        schedule of payments. All other dates must be later than this date, but
        they may occur in any order. *Date* should contain as many dates as the
        number of values given by *Value*.

    *Mode*
        Indicates whether all the solutions need to be found or just one.
        :math:`Mode = 0`: the search for solutions stops after one solution is
        found. :math:`Mode = 1`: the search for solutions continues till all
        solutions are found.

    *IRR*
        The internal rate of return for the investment. There is not always a
        unique solution for *IRR*. Dependent on *Mode* one solution or all the
        solutions will be given. Solutions smaller than -1 are not supposed to
        be relevant, so the search for solutions is limited to the area greater
        than -1.

    *NumberSolutions*
        The number of solutions found. When :math:`Mode = 0` the
        *NumberSolutions* will be 1.

    *Basis*
        The day-count basis method to be used. The default is 1.

Equation
--------

    The internal rate of return :math:`r` is a solution of the equation

    .. math:: \sum_{i=1}^n \frac{p_i}{(1+r)^{f_i}} = 0

    \ where :math:`p_i` are the periodic payments, and :math:`f_i` is the
    difference between date :math:`i` and the first date (so,
    :math:`f_1 = 0`), according to the selected day-count basis method.

.. note::

    -  When you want to use the procedure in an objective function or
       constraint you have to use
       ``InvestmentVariableInternalRateReturnInPeriodic``.

    -  The procedure :aimms:func:`InvestmentVariableInternalRateReturnInPeriodicAll`
       is similar to the Excel function `XIRR <https://learn.microsoft.com/en-us/office/troubleshoot/excel/algorithm-of-xirr-funcation>`_.

Example
-------

Often, internal rate of return is an investment first, (period 0, negative value),
and then return cashflows in following periods. 

.. code-block:: aimms

    _s_periods := ElementRange(0,4);
    _p_val('0') := -100 ;
    _p_val('1') := 25 ;
    _p_val(_i_per | _i_per > '1') := _p_val(_i_per-1) * 1.1 ;
    _sp_startQuarter(_i_per) := MomentToString(
        Format        :  "%c%y-%m-%d", 
        unit          :  [month], 
        ReferenceDate :  "2024-01-01", 
        Elapsed       :  ((ord(_i_per)-1)*3)[month]);
    _s_sols := ElementRange(1,5);

    InvestmentVariableInternalRateReturnInPeriodicAll(
        value             :  _p_val, 
        date              :  _sp_startQuarter,
        Mode              :  1, 
        NumberOfSolutions :  _p_sols, 
        IRR               :  _p_irr(_i_sol) );
    block where single_column_display := 1, listing_number_precision := 6 ;
        display { _p_val, _sp_startQuarter }, _p_sols, _p_irr ;
    endblock ;

This results in the following IRR:

.. code-block:: aimms

    Composite table:
        _i_per         _p_val  _sp_startQuarter
    !   ------    -----------  ----------------
             0    -100.000000  "2024-01-01"    
             1      25.000000  "2024-04-01"    
             2      27.500000  "2024-07-01"    
             3      30.250000  "2024-10-01"    
             4      33.275000  "2025-01-01"    
        ;

        _p_sols := 1 ;


        _p_irr := data 
        { 1 : 0.258815 } ;
      

.. seealso::

    *   The functions :aimms:func:`InvestmentVariableInternalRateReturn`.
    *   :aimms:func:`InvestmentVariableInternalRateReturnInPeriodic`. 
    *   Day count basis :ref:`methods<ff.dcb>`.
