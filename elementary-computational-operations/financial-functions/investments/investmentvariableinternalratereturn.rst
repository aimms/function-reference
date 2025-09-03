.. aimms:function:: InvestmentVariableInternalRateReturn(Value, LowerBound, UpperBound, Error)

.. _InvestmentVariableInternalRateReturn:

InvestmentVariableInternalRateReturn
====================================

The function :aimms:func:`InvestmentVariableInternalRateReturn` returns the
internal rate of return for an investment based on a series of periodic
cash flows. The internal rate of return is the rate received for an
investment. This function uses the procedure
*InvestmentVariableInternalRateReturnAll* to determine all possible
internal rates and returns the internal rate that is within the
specified bounds.

.. code-block:: aimms

    InvestmentVariableInternalRateReturn(
        Value,                   ! (input) one-dimensional numerical expression
        [LowerBound,]            ! (optional) numerical expression
        [UpperBound,]            ! (optional) numerical expression
        [Error]                  ! (optional) numerical expression
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

    *LowerBound*
        Indicates a minimum for the internal rate to be accepted by this
        function. The default is :math:`-1`.

    *UpperBound*
        Indicates a maximum for the internal rate to be accepted by this
        function. The default is :math:`5`.

    *Error*
        Indicates whether AIMMS should give an error if multiple solutions are
        found that satisfy the bounds. :math:`Error = 0`: if multiple solutions
        are found, return the solution with the smallest absolute value.
        :math:`Error = 1`: if multiple solutions are found, return an error
        message. The default is :math:`0`.

Return Value
------------

    The function :aimms:func:`InvestmentVariableInternalRateReturn` returns the
    internal rate of return for an investment based on a series of periodic
    cash flows. The internal rate of return is the rate received for an
    investment.

.. note::

    -  The function :aimms:func:`InvestmentVariableInternalRateReturn` can be used in
       an objective function or constraint. The input parameter *Value* can
       be used as a variable.

    -  The function :aimms:func:`InvestmentVariableInternalRateReturn` is similar to
       the Excel function `IRR <https://support.microsoft.com/en-us/office/irr-function-64925eaa-9988-495b-b290-3ad0c163c1bc>`_.


Example
-------

Often, internal rate of return is an investment first, (period 0, negative value),
and then return cashflows in following periods. 

.. code-block:: aimms

	_s_periods := ElementRange(0,4);
	_p_val('0') := -100 ;
	_p_val('1') := 50 ;
	_p_val(_i_per | _i_per > '1') := _p_val(_i_per-1) * 1.5 ;
	_p_irr := InvestmentVariableInternalRateReturn(
		value      :  _p_val, 
		LowerBound :  -1, 
		UpperBound :  5, 
		Error      :  1);
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

    _p_irr := 0.688847 ;
      

.. seealso::

    * The functions :aimms:func:`InvestmentVariableInternalRateReturnAll`.	
	* :aimms:func:`InvestmentVariableInternalRateReturnInPeriodic`.
