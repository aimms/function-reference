.. aimms:function:: InvestmentConstantInterestPayment(PresentValue, FutureValue, NumberPeriods, Period, InterestRate, Type)

.. _InvestmentConstantInterestPayment:

InvestmentConstantInterestPayment
=================================

The function :aimms:func:`InvestmentConstantInterestPayment` returns the interest
payment of the specified period for an investment based on periodic,
constant payments and a constant interest rate. Every periodic payment
can be divided in two parts: an interest payment and a principal
repayment.

.. code-block:: aimms

    InvestmentConstantInterestPayment(
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

    The function :aimms:func:`InvestmentConstantInterestPayment` returns the interest
    payment for the specified period.

Equation
--------

    The interest payment :math:`i_i` in period :math:`i` is computed through
    the equation

    .. math:: i_i = -v_pr(1+r)^{i-1-T} - p\left(\left((1+r)^{i-1-T}-1\right)(1+r)^T+rT\right)

.. note::

    -  This function can be used in an objective function or constraint and
       the input parameters *PresentValue*, *FutureValue* and *InterestRate*
       can be used as a variable.

    -  The function :aimms:func:`InvestmentConstantInterestPayment` is similar to the
       Excel function ``IPMT``.

Example
-------

How much interest is paid for a loan of ten years and an interest of 4% in each period:

.. code-block:: aimms

    _p_life := 10 ;
    _bp_type := 1;
    _s_periods := ElementRange(1, _p_life + _bp_type);
    _p_InterestPayment(_i_per) :=
        InvestmentConstantInterestPayment(
            PresentValue  :  100, 
            FutureValue   :  0, 
            NumberPeriods :  10, 
            Period        :  _i_per, 
            InterestRate  :  0.04, 
            type          :  _bp_type);
    block where single_column_display := 1, listing_number_precision := 6 ;
        display _p_InterestPayment;
    endblock ;

The following table shows that the interest portion of each anuity becomes less:

.. code-block:: aimms

    _p_InterestPayment := data 
    {  2 : -3.525804e+00,
       3 : -3.192640e+00,
       4 : -2.846150e+00,
       5 : -2.485800e+00,
       6 : -2.111036e+00,
       7 : -1.721282e+00,
       8 : -1.315937e+00,
       9 : -8.943784e-01,
      10 : -4.559576e-01,
      11 :  4.440892e-15 } ;

.. seealso::

    *   General :ref:`equations<FF.inveq>` for investments with constant, periodic payments.
