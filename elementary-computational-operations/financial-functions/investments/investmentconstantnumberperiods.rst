.. aimms:function:: InvestmentConstantNumberPeriods(PresentValue, FutureValue, Payment, InterestRate, Type)

.. _InvestmentConstantNumberPeriods:

InvestmentConstantNumberPeriods
===============================

The function :aimms:func:`InvestmentConstantNumberPeriods` returns the number of
periods for an investment based on periodic, constant payments and a
constant interest rate.

.. code-block:: aimms

    InvestmentConstantNumberPeriods(
        PresentValue,            ! (input) numerical expression
        FutureValue,             ! (input) numerical expression
        Payment,                 ! (input) numerical expression
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

    *Payment*
        The value of the periodic payment for the investment. Payment must be a
        real number. *Payment* and *InterestRate* cannot both be :math:`0`.

    *InterestRate*
        The interest rate per period for the investment. *InterestRate* must be
        a numerical expression in the range :math:`(-1, 1)`.

    *Type*
        Indicates when payments are due. :math:`Type = 0`: Payments are due at
        the end of each period. :math:`Type = 1`: Payments are due at the
        beginning of each period.

Return Value
------------

    The function :aimms:func:`InvestmentConstantNumberPeriods` returns the number of
    periods for an investment based on periodic, constant payments and a
    constant interest rate. 

.. note::

    -   The value returned may be fractional.

    -   The function :aimms:func:`InvestmentConstantNumberPeriods` is similar to the Excel
        function `NPER <https://support.microsoft.com/en-us/office/nper-function-240535b5-6653-4d2d-bfcf-b6a38151d815>`_.

Example
-------

``InvestmentConstantNumberPeriods`` is used here to determine 
how long it takes to save up for an investment, or pay back on a loan, 
given a certain amount of money that can be reserved per period.

.. code-block:: aimms

    ! How long does it take to save up 100 
    ! when paying 10 each period and an interest rate of 4%?
    _p_nperSavingUp := 
        InvestmentConstantNumberPeriods(
            PresentValue :  0, 
            FutureValue  :  -100, 
            Payment      :  10, 
            InterestRate :  0.04, 
            type         :  0);

    ! How long does it take to reimburse 100
    ! when paying 10 each period and an interest rate of 4%?
    _p_nperReimbursing := 
        InvestmentConstantNumberPeriods(
            PresentValue :  -100, 
            FutureValue  :  0, 
            Payment      :  10, 
            InterestRate :  0.04, 
            type         :  0);
    block where single_column_display := 1, listing_number_precision := 6 ;
        display { _p_nperSavingUp, _p_nperReimbursing};
    endblock ;

The results in the listing file state that saving up requires less time than paying back.

.. code-block:: aimms

    _p_nperSavingUp     :=  8.578942 ;
    _p_nperReimbursing  := 13.024384 ;
      

.. seealso::

    *   General :ref:`equations<FF.inveq>` for investments with constant, periodic payments.
