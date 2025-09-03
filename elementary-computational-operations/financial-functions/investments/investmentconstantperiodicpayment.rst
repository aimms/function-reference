.. aimms:function:: InvestmentConstantPeriodicPayment(PresentValue, FutureValue, NumberPeriods, InterestRate, Type)

.. _InvestmentConstantPeriodicPayment:

InvestmentConstantPeriodicPayment
=================================

The function :aimms:func:`InvestmentConstantPeriodicPayment` returns the periodic
payment for an investment based on periodic, constant payments and a
constant interest rate.

.. code-block:: aimms

    InvestmentConstantPeriodicPayment(
        PresentValue,            ! (input) numerical expression
        FutureValue,             ! (input) numerical expression
        NumberPeriods,           ! (input) numerical expression
        InterestRate,            ! (input) numerical expression
        Type                     ! (input) numerical expression
        )

Arguments
---------

    *PresentValue*
        The total amount that a series of future payments is worth at this
        moment. *PresentValue* must be a real number.

    *FutureValue*
        The cash balance you want to attain after the last payment is made.
        *FutureValue* must be a real number.

    *NumberPeriods*
        The total number of payment periods for the investment. *NumberPeriods*
        must be a positive integer.

    *InterestRate*
        The interest rate per period for the investment. *InterestRate* must be
        a numerical expression in the range :math:`(-1, 1)`.

    *Type*
        Indicates when payments are due. :math:`Type = 0`: Payments are due at
        the end of each period. :math:`Type = 1`: Payments are due at the
        beginning of each period.

Return Value
------------

    The function :aimms:func:`InvestmentConstantPeriodicPayment` returns the periodic
    payment for the investment.

.. note::

    -  This function can be used in an objective function or constraint and
       the input parameters *PresentValue*, *FutureValue* and *InterestRate*
       can be used as a variable.

    -  The function :aimms:func:`InvestmentConstantPeriodicPayment` is similar to the
       Excel function ``PMT``.



Example
-------

Perhaps the following will encourage you to save up first:

.. code-block:: aimms

    ! How much needs to be paid per period, 
    ! for 10 periods, and an interest rate of 4% 
    ! to attain a capital of 100 in the end?
    _p_constPeriodicPaymentSavingup := InvestmentConstantPeriodicPayment(
        PresentValue  :  0,
        FutureValue   :  100, 
        NumberPeriods :  10,
        InterestRate  :  0.04,
        type          :  0);

    ! Spending a 100 now, how much do I have to 
    ! reimburse/compensate over each of the 10 periods, 
    ! whereby the interest rate is 4%
    _p_constPeriodicPaymentReimbursing := InvestmentConstantPeriodicPayment(
        PresentValue  :  100,
        FutureValue   :  0, 
        NumberPeriods :  10,
        InterestRate  :  0.04,
        type          :  0);

    block where single_column_display := 1, listing_number_precision := 6 ;
        display { _p_constPeriodicPaymentSavingup, _p_constPeriodicPaymentReimbursing } ;
    endblock ;

The result of this example shows there is a 50% difference 
in amount to be saved per period, if you spent it 
at the beginning or at the end:

.. code-block:: aimms

    _p_constPeriodicPaymentSavingup    :=  -8.329094 ;
    _p_constPeriodicPaymentReimbursing := -12.329094 ;

.. seealso::

    *   General :ref:`equations<FF.inveq>` for investments with constant, periodic payments.
