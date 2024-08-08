.. aimms:function:: InvestmentConstantRate(PresentValue, FutureValue, Payment, NumberPeriods, Type, LowerBound, UpperBound, Error)

.. _InvestmentConstantRate:

InvestmentConstantRate
======================

The function :aimms:func:`InvestmentConstantRate` returns the interest rate for an
investment based on periodic, constant payments and a constant interest
rate. This function uses the procedure ``InvestmentConstantRateAll`` to
determine all possible interest rates and returns the interest rate that
is within the specified bounds.

.. code-block:: aimms

    InvestmentConstantRate(
        PresentValue,            ! (input) numerical expression
        FutureValue,             ! (input) numerical expression
        Payment,                 ! (input) numerical expression
        NumberPeriods,           ! (input) numerical expression
        Type,                    ! (input) numerical expression
        [LowerBound,]            ! (optional) numerical expression
        [UpperBound,]            ! (optional) numerical expression
        [Error]                  ! (optional) numerical expression
        )

Arguments
---------

    *PresentValue*
        The total amount that a series of future payments is worth at this
        moment. *PresentValue* must be a real number.

    *FutureValue*
        The cash balance you want to attain after the last payment is made.
        *FutureValue* must be a real number.

    *Payment*
        The periodic payment for the investment. *Payment* must be a real
        number.

    *NumberPeriods*
        The total number of payment periods for the investment. *NumberPeriods*
        must be a positive integer.

    *Type*
        Indicates when payments are due. :math:`Type = 0`: Payments are due at
        the end of each period. :math:`Type = 1`: Payments are due at the
        beginning of each period.

    *LowerBound*
        Indicates a minimum for the interest rate to be accepted by this
        function. The default is :math:`-1`.

    *UpperBound*
        Indicates a maximum for the interest rate to be accepted by this
        function. The default is :math:`5`.

    *Error*
        Indicates whether AIMMS should give an error if multiple solutions are
        found that satisfy the bounds. :math:`Error = 0`: if multiple solutions
        are found, return the solution with the smallest absolute value.
        :math:`Error = 1`: if multiple solutions are found, return an error
        message. The default is :math:`0`.

Return Value
------------

    The function :aimms:func:`InvestmentConstantRate` returns the interest rate for an
    investment based on periodic, constant payments and a constant interest
    rate.

.. note::

    -  The function :aimms:func:`InvestmentConstantRate` can be used in an objective
       function or constraint. The input parameters *PresentValue*,
       *FutureValue* and *Payment* can be used as variables.

    -  The function :aimms:func:`InvestmentConstantRate` is similar to the Excel
       function ``RATE``.


Example
-------

``InvestmentConstantRate`` is used when there is a fixed series of equal payments
to determine the interest percentage needed to make up for a loan or to save up for an investment.

.. code-block:: aimms

	! Which interest rate do I need to save up for a given investment
	! with a given series of fixed savings?
	_p_pctSavingUp := 
		InvestmentConstantRate(
			PresentValue  :  0, 
			FutureValue   :  -100, 
			Payment       :  10, 
			NumberPeriods :  8, 
			type          :  0, 
			LowerBound    :  -1, 
			UpperBound    :  5, 
			Error         :  1);

	! With which percentage can I pay off a loan,
	! given a fixed series of equal payments?
	_p_pctReimburse := 
		InvestmentConstantRate(
			PresentValue  :  -100, 
			FutureValue   :  0, 
			Payment       :  10, 
			NumberPeriods :  13, 
			type          :  0, 
			LowerBound    :  -1, 
			UpperBound    :  5, 
			Error         :  1);

	block where single_column_display := 1, listing_number_precision := 6 ;
		display { _p_pctSavingUp, _p_pctReimburse};
	endblock ;

As the number of periods used are not equal, it is hard to compare the results.

.. code-block:: aimms

    _p_pctSavingUp  := 0.062870 ;
    _p_pctReimburse := 0.039769 ;
      

References
-----------

    *   General :ref:`equations<FF.inveq>` for investments with constant, periodic payments.
