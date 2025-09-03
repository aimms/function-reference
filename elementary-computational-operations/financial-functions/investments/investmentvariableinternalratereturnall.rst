.. aimms:function:: InvestmentVariableInternalRateReturnAll(Value, Mode, NumberSolutions, IRR)

.. _InvestmentVariableInternalRateReturnAll:

InvestmentVariableInternalRateReturnAll
=======================================

The procedure :aimms:func:`InvestmentVariableInternalRateReturnAll` returns the
internal rate of return for an investment based on a series of periodic
cash flows. The internal rate of return is the rate received for an
investment consisting of payments (negative values) and income (positive
values).

.. code-block:: aimms

    InvestmentVariableInternalRateReturnAll(
        Value,                   ! (input) one-dimensional numerical expression
        Mode,                    ! (input) numerical expression
        NumberSolutions,         ! (output) numerical expression
        IRR                      ! (output) one-dimensional numerical expression
        )

Arguments
---------

    *Value*
        The periodic payments (positive or negative), which must be equally
        spaced in time. The order of the payments in *Value* must be the same as
        the order in which the cash flows occur. *Value* is an one dimensional
        parameter of real numbers. *Value* given by positive numbers represent
        incoming amounts and *Value* given by negative numbers represent
        outgoing amounts. em Value must contain at least one positive and at
        least one negative number.

    *Mode*
        Indicates whether all the solutions need to be found or just one.
        :math:`Mode = 0`: the search for solutions stops after one solution is
        found. :math:`Mode = 1`: the search for solutions continues till all
        solutions are found.

    *NumberSolutions*
        The number of solutions found. When :math:`Mode = 0` the
        *NumberSolutions* will be 1.

    *IRR*
        The internal rate of return for the investment. There is not always a
        unique solution for *IRR*. Dependent on *Mode* one solution or all the
        solutions will be given. Solutions smaller than -1 are not supposed to
        be relevant, so the search for solutions is limited to the area greater
        than -1.

Equation
--------

    The internal rate of return :math:`r` is a solution of the equation

    .. math:: \sum_{i=1}^n \frac{p_i}{(1+r)^i} = 0

    \ where :math:`p_i` are the periodic payments.

.. note::

    -  The internal rate of return is the interest rate at which the
       investment has a zero net present value.

    -  When you want to use this procedure in an objective function or
       constraint you have to use *InvestmentVariableInternalRateReturn*.

    -  The function :aimms:func:`InvestmentVariableInternalRateReturnAll` is similar
       to the Excel function `IRR <https://support.microsoft.com/en-us/office/irr-function-64925eaa-9988-495b-b290-3ad0c163c1bc>`_.



Example
-------

Often, internal rate of return is an investment first, (period 0, negative value),
and then return cashflows in following periods. 

.. code-block:: aimms

    _s_periods := ElementRange(0,4);
    _p_val('0') := -100 ;
    _p_val('1') := 50 ;
    _p_val(_i_per | _i_per > '1') := _p_val(_i_per-1) * 1.5 ;
    _s_sols := ElementRange(1,5);
    _p_sols := 0 ;
    InvestmentVariableInternalRateReturnAll(
        value           :  _p_val, 
        Mode            :  1, 
        NumberSolutions :  _p_sols, 
        IRR             :  _p_irr(_i_sol) );

    block where single_column_display := 1, listing_number_precision := 6 ;
        display _p_val, _p_sols, _p_irr ;
    endblock ;

This results in the following IRR:

.. code-block:: aimms

    _p_val := data 
    { 0 : -100.000000,
      1 :   50.000000,
      2 :   75.000000,
      3 :  112.500000,
      4 :  168.750000 } ;

    _p_sols := 1 ;


    _p_irr := data 
    { 1 : 0.688847 } ;

.. seealso::

    *  The functions :aimms:func:`InvestmentVariableInternalRateReturn`.
    *  :aimms:func:`InvestmentVariableInternalRateReturnInPeriodic`.
