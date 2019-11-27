.. aimms:function:: InvestmentConstantPrincipalPayment(PresentValue, FutureValue, NumberPeriods, Period, InterestRate, Type)

.. _InvestmentConstantPrincipalPayment:

InvestmentConstantPrincipalPayment
==================================

The function :aimms:func:`InvestmentConstantPrincipalPayment` returns the
principal payment of the specified period for an investment based on
periodic, constant payments and a constant interest rate. Every periodic
payment can be divided in two parts: an interest payment and a principal
payment.

.. code-block:: aimms

    InvestmentConstantPrincipalPayment(
        PresentValue,            ! (input) numerical expression
        FutureValue,             ! (input) numerical expression
        NumberPeriods,           ! (input) numerical expression
        Period                   ! (input) numerical expression
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

    *Period*
        The period for which you want to compute the interest payment. *Period*
        must be an integer in the range :math:`\{1, NumberPeriods + Type \}`.
        When :math:`Type = 1`, the extra period is to account the interest over
        the former period.

    *InterestRate*
        The interest rate per period for the investment. *InterestRate* must be
        a numerical expression in the range :math:`(-1, 1)`.

    *Type*
        Indicates when payments are due. :math:`Type = 0`: Payments are due at
        the end of each period. :math:`Type = 1`: Payments are due at the
        beginning of each period.

Return Value
------------

    The function :aimms:func:`InvestmentConstantPrincipalPayment` returns the
    principal payment for the specified period.

Equation
--------

    The principal payment :math:`p_i` in period :math:`i` follows from the
    relation

    .. math:: p_i = p - i_i

    \ where :math:`i_i` is the interest payment in period :math:`i`.

.. note::

    -  This function can be used in an objective function or constraint and
       the input parameters *PresentValue*, *FutureValue* and *InterestRate*
       can be used as a variable.

    -  The function :aimms:func:`InvestmentConstantPrincipalPayment` is similar to the
       Excel function ``PPMT``.

.. seealso::

    General :ref:`equations<FF.inveq>` for investments with constant, periodic payments.
