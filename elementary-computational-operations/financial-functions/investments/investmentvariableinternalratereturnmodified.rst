.. aimms:function:: InvestmentVariableInternalRateReturnModified(Value, FinanceRate, ReinvestRate)

.. _InvestmentVariableInternalRateReturnModified:

InvestmentVariableInternalRateReturnModified
============================================

The function :aimms:func:`InvestmentVariableInternalRateReturnModified` returns
the modified internal rate of return for an investment based on a series
of periodic cash flows. It considers both the cost made for the
investment and the interest received on the reinvestment of cash flows.

.. code-block:: aimms

    InvestmentVariableInternalRateReturnModified(
        Value,                   ! (input) one-dimensional numerical expression
        FinanceRate,             ! (input) numerical expression
        ReinvestRate             ! (input) numerical expression
        )

Arguments
---------

    *Value*
        The periodic payments (positive or negative), which must be equally
        spaced in time. The order of the payments in *Value* must be the same as
        the order in which the cash flows occur. *Value* is an one dimensional
        parameter of real numbers. *Value* given by positive numbers represent
        incoming amounts and *Value* given by negative numbers represent
        outgoing amounts. *Value* must contain at least one positive and at
        least one negative number.

    *FinanceRate*
        Interest rate you pay on money used in negative cash flows.
        *FinanceRate* must be a numerical expression in the range
        :math:`[-1, \infty)`.

    *ReinvestRate*
        Interest rate you receive on the positive cash flows as you reinvest
        them. *ReinvestRate* must be a numerical expression in the range
        :math:`[-1, \infty)`.

Return Value
------------

    The function :aimms:func:`InvestmentVariableInternalRateReturnModified` returns
    the modified internal rate of return for the investment.

Equation
--------

    The internal rate of return :math:`r` is the solution of the equation

    .. math:: (1+r)^{n-1} = -\frac{\mbox{NPV}(v^+,r_r)(1+r_r)^n}{\mbox{NPV}(v^-,r_f)(1+r_f)}

    \ where :math:`n` is the number of periods considered,
    :math:`v_i = v^+_i - v^-_i` (with :math:`v^+_i, v^-_i \geq 0`),
    :math:`r_f` the finance rate, :math:`r_r` the reinvestment rate, and NPV
    the function :aimms:func:`InvestmentVariablePresentValue`.

.. note::

    -  This function can be used in an objective function or constraint and
       the input parameters *Value*, *FinanceRate* and *ReinvestRate* can be
       used as a variable.

    -  There should be at least one negative and one negative *Value*.

    -  The function :aimms:func:`InvestmentVariableInternalRateReturnModified` is
       similar to the Excel function ``MIRR``.

.. seealso::

    The function :aimms:func:`InvestmentVariableInternalRateReturn`.
