.. aimms:function:: InvestmentConstantPresentValue(FutureValue, Payment, NumberPeriods, InterestRate, Type)

.. _InvestmentConstantPresentValue:

InvestmentConstantPresentValue
==============================

The function :aimms:func:`InvestmentConstantPresentValue` returns the present
value of an investment based on periodic, constant payments and a
constant interest rate.

.. code-block:: aimms

    InvestmentConstantPresentValue(
        FutureValue,             ! (input) numerical expression
        Payment,                 ! (input) numerical expression
        NumberPeriods,           ! (input) numerical expression
        InterestRate,            ! (input) numerical expression
        Type                     ! (input) numerical expression
        )

Arguments
---------

    *FutureValue*
        The cash balance you want to attain after the last payment is made.
        *FutureValue* must be a real number.

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

    The function :aimms:func:`InvestmentConstantPresentValue` returns the total amount
    that a series of future payments is worth at this moment.

.. note::

    -  This function can be used in an objective function or constraint and
       the input parameters *FutureValue*, *Payment* and *InterestRate* can
       be used as a variable.

    -  The function :aimms:func:`InvestmentConstantPresentValue` is similar to the
       Excel function ``PV``.

.. seealso::

    General :ref:`equations<FF.inveq>` for investments with constant, periodic payments.
