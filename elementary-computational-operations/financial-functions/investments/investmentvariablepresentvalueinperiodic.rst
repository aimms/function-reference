.. aimms:function:: InvestmentVariablePresentValueInPeriodic(Value, Date, InterestRate, Basis)

.. _InvestmentVariablePresentValueInPeriodic:

InvestmentVariablePresentValueInPeriodic
========================================

The function :aimms:func:`InvestmentVariablePresentValueInPeriodic` returns the
net present value on the date of the first cash flow for an investment
based on a series of in-periodic cash flows and a constant interest
rate.

.. code-block:: aimms

    InvestmentVariablePresentValueInPeriodic(
        Value,                   ! (input) one-dimensional numerical expression
        Date,                    ! (input) one-dimensional string expression
        InterestRate,            ! (input) numerical expression
        [Basis]                  ! (optional) numerical expression
        )

Arguments
---------

    *Value*
        The payments (positive or negative). *Value* is an one-dimensional
        parameter of real numbers. *Value* given by positive numbers represent
        incoming amounts and *Value* given by negative numbers represent
        outgoing amounts. *Value* must contain at least one positive and at
        least one negative number.

    *Date*
        The dates on which the payments occur. *Date* and *Value* must have the
        same order. *Date* is an one-dimensional parameter of dates given in a
        date format. The first payment date indicates the beginning of the
        schedule of payments. All other dates must be later than this date, but
        they may occur in any order. *Date* should contain as many dates as the
        number of values given by *Value*.

    *InterestRate*
        The interest rate per period for the investment. *InterestRate* must be
        a numerical expression in the range :math:`(-1, 1)`.

    *Basis*
        The day-count basis method to be used. The default is 1.

Return Value
------------

    The function :aimms:func:`InvestmentVariablePresentValueInPeriodic` returns the
    net present value of an investment, which is the total value of all the
    future cash flows at this moment.

Equation
--------

    The net present value :math:`v_p` is computed through the equation

    .. math:: v_p = \sum_{i=1}^n \frac{p_i}{(1+r)^{f_i}}

    \ where :math:`p_i` are the periodic payments, :math:`r` is the
    (constant) interest rate, and :math:`f_i` is the difference between date
    :math:`i` and the first date (so, :math:`f_1 = 0`), according to the
    selected day-count basis method.

.. note::

    -  This function can be used in an objective function or constraint and
       the input parameters *Value* and *InterestRate* can be used as a
       variable.

    -  The function :aimms:func:`InvestmentVariablePresentValueInPeriodic` is similar
       to the Excel function ``XNPV``.

.. seealso::

    Day count basis :ref:`methods<ff.dcb>`.
