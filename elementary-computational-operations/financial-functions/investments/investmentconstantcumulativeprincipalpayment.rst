.. aimms:function:: InvestmentConstantCumulativePrincipalPayment(PresentValue, FutureValue, NumberPeriods, StartPeriod, EndPeriod, InterestRate, Type)

.. _InvestmentConstantCumulativePrincipalPayment:

InvestmentConstantCumulativePrincipalPayment
============================================

The function :aimms:func:`InvestmentConstantCumulativePrincipalPayment` returns
the cumulative principal payment for the specified interval for an
investment based on periodic, constant payments and a constant interest
rate. Every periodic payment can be divided in two parts: an interest
payment and a principal payment.

.. code-block:: aimms

    InvestmentConstantCumulativePrincipalPayment(
        PresentValue,            ! (input) numerical expression
        FutureValue,             ! (input) numerical expression
        NumberPeriods,           ! (input) numerical expression
        StartPeriod,             ! (input) numerical expression
        EndPeriod,               ! (input) numerical expression
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

    *StartPeriod*
        The starting period of the interval for which you want to compute the
        cumulative interest payment. *StartPeriod* must be an integer in the
        range :math:`\{ 1, NumberPeriods \}`.

    *EndPeriod*
        The ending period of the interval for which you want to compute the
        cumulative interest payment. *EndPeriod* must be an integer in the range
        :math:`\{ StartPeriod, NumberPeriods\}`.

    *InterestRate*
        The interest rate per period for the investment. *InterestRate* must be
        a numerical expression in the range :math:`(-1, 1)`.

    *Type*
        Indicates when payments are due. :math:`Type = 0`: Payments are due at
        the end of each period. :math:`Type = 1`: Payments are due at the
        beginning of each period.

Return Value
------------

    The function :aimms:func:`InvestmentConstantCumulativePrincipalPayment` returns
    the sum of the principal payments for the periods in the specified
    interval.

.. note::

    -  This function can be used in an objective function or constraint and
       the input parameters *PresentValue*, *FutureValue* and *InterestRate*
       can be used as a variable.

    -  The function :aimms:func:`InvestmentConstantCumulativePrincipalPayment` is
       similar to the Excel function ``CUMPRINC``.

.. seealso::

    General :ref:`equations<FF.inveq>` for investments with constant, periodic payments.
