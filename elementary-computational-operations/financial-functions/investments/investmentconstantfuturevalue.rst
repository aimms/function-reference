.. aimms:function:: InvestmentConstantFutureValue(PresentValue, Payment, NumberPeriods, InterestRate, Type)

.. _InvestmentConstantFutureValue:

InvestmentConstantFutureValue
=============================

The function :aimms:func:`InvestmentConstantFutureValue` returns the future value
of an investment based on periodic, constant payments and a constant
interest rate.

.. code-block:: aimms

    InvestmentConstantFutureValue(
        PresentValue,            ! (input) numerical expression
        Payment,                 ! (input) numerical expression
        NumberPeriods,           ! (input) numerical expression
        InterestRate,            ! (input) numerical expression
        Type                     ! (input) numerical expression
        )

Arguments
---------

    *PresentValue*
        The total amount that a series of future payments is worth at this
        moment. *PresentValue* must be a real number.

    *Payment*
        The periodic payment for the investment. *Payment* must be a real
        number.

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

    The function :aimms:func:`InvestmentConstantFutureValue` returns the cash balance
    you want to attain after the last payment is made.

.. note::

    -  This function can be used in an objective function or constraint and
       the input parameters *PresentValue*, *Payment* and *InterestRate* can
       be used as a variable.

    -  The function :aimms:func:`InvestmentConstantFutureValue` is similar to the
       Excel function `FV <https://support.microsoft.com/en-us/office/fv-function-2eef9f44-a084-4c61-bdd8-4fe4bb1b71b3>`_.


Example
-------

Receiving regularly money over time, leads to a debt:

.. code-block:: aimms

    ! Receiving 10 per period, 
    ! for 10 periods, and 
    ! an interest of 4%, 
    ! results in a debt of 120.06
    _p_constFutureValue := InvestmentConstantFutureValue(
        PresentValue  :  0,
        Payment       :  10,
        NumberPeriods :  10,
        InterestRate  :  0.04,
        type          :  0);
    block where single_column_display := 1, listing_number_precision := 6 ;
        display _p_constFutureValue;
    endblock ;

The future value computed is negative, indicating a debt:

.. code-block:: aimms

    _p_constFutureValue := -120.061071 ;

.. seealso::

    *   General :ref:`equations<FF.inveq>` for investments with constant, periodic payments.

