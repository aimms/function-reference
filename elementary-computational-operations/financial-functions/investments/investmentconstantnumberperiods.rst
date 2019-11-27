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

    The function :aimms:func:`InvestmentConstantNumberPeriods` is similar to the Excel
    function ``NPER``.

.. seealso::

    General :ref:`equations<FF.inveq>` for investments with constant, periodic payments.
