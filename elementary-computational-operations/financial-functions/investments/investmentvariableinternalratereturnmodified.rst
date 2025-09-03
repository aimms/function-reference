.. aimms:function:: InvestmentVariableInternalRateReturnModified(Value, FinanceRate, ReinvestRate)

.. _InvestmentVariableInternalRateReturnModified:

InvestmentVariableInternalRateReturnModified
============================================

The function :aimms:func:`InvestmentVariableInternalRateReturnModified` returns
the modified internal rate of return for an investment based on a series
of periodic cash flows. It considers both the cost made for the
investment and the interest received on the reinvestment of cash flows.

.. code-block:: aimms

    InvestmentVariableInternalRateReturnModified(
        Value,                   ! (input) one-dimensional numerical expression
        FinanceRate,             ! (input) numerical expression
        ReinvestRate             ! (input) numerical expression
        )

Arguments
---------

    *Value*
        The periodic payments (positive or negative), which must be equally
        spaced in time. The order of the payments in *Value* must be the same as
        the order in which the cash flows occur. *Value* is an one dimensional
        parameter of real numbers. *Value* given by positive numbers represent
        incoming amounts and *Value* given by negative numbers represent
        outgoing amounts. *Value* must contain at least one positive and at
        least one negative number.

    *FinanceRate*
        Interest rate you pay on money used in negative cash flows.
        *FinanceRate* must be a numerical expression in the range
        :math:`[-1, \infty)`.

    *ReinvestRate*
        Interest rate you receive on the positive cash flows as you reinvest
        them. *ReinvestRate* must be a numerical expression in the range
        :math:`[-1, \infty)`.

Return Value
------------

    The function :aimms:func:`InvestmentVariableInternalRateReturnModified` returns
    the modified internal rate of return for the investment.

Equation
--------

    The internal rate of return :math:`r` is the solution of the equation

    .. math:: (1+r)^{n-1} = -\frac{\mbox{NPV}(v^+,r_r)(1+r_r)^n}{\mbox{NPV}(v^-,r_f)(1+r_f)}

    \ where :math:`n` is the number of periods considered,
    :math:`v_i = v^+_i - v^-_i` (with :math:`v^+_i, v^-_i \geq 0`),
    :math:`r_f` the finance rate, :math:`r_r` the reinvestment rate, and NPV
    the function :aimms:func:`InvestmentVariablePresentValue`.

.. note::

    -  This function can be used in an objective function or constraint and
       the input parameters *Value*, *FinanceRate* and *ReinvestRate* can be
       used as a variable.

    -  There should be at least one negative and one positive *Value*.

    -  The function :aimms:func:`InvestmentVariableInternalRateReturnModified` is
       similar to the Excel function `MIRR <https://support.microsoft.com/en-us/office/mirr-function-28b62fff-b057-47ee-9ff9-13ea2628a007>`_.


Example
-------

Often, internal rate of return is an investment first, (period 0, negative value),
and then return cashflows in following periods. 

.. code-block:: aimms

    _s_periods := ElementRange(0,4);
    _p_val('0') := -100 ;
    _p_val('1') := 50 ;
    _p_val(_i_per | _i_per > '1') := _p_val(_i_per-1) * 1.5 ;
    _p_irr := InvestmentVariableInternalRateReturnModified(
        value        :  _p_val, 
        FinanceRate  :  0.07, 
        ReinvestRate :  0.04 );
    block where single_column_display := 1, listing_number_precision := 6 ;
        display _p_val, _p_irr ;
    endblock ;

This results in the following IRR:

.. code-block:: aimms

    _p_val := data 
    { 0 : -100.000000,
      1 :   50.000000,
      2 :   75.000000,
      3 :  112.500000,
      4 :  168.750000 } ;

    _p_irr := 0.434215 ;
      

.. seealso::
    
    *   The function :aimms:func:`InvestmentVariableInternalRateReturn`.
