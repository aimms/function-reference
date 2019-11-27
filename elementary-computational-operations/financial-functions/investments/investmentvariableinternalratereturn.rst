.. aimms:function:: InvestmentVariableInternalRateReturn(Value, LowerBound, UpperBound, Error)

.. _InvestmentVariableInternalRateReturn:

InvestmentVariableInternalRateReturn
====================================

The function :aimms:func:`InvestmentVariableInternalRateReturn` returns the
internal rate of return for an investment based on a series of periodic
cash flows. The internal rate of return is the rate received for an
investment. This function uses the procedure
*InvestmentVariableInternalRateReturnAll* to determine all possible
internal rates and returns the internal rate that is within the
specified bounds.

.. code-block:: aimms

    InvestmentVariableInternalRateReturn(
        Value,                   ! (input) one-dimensional numerical expression
        [LowerBound,]            ! (optional) numerical expression
        [UpperBound,]            ! (optional) numerical expression
        [Error]                  ! (optional) numerical expression
        )

Arguments
---------

    *Value*
        The periodic payments (positive or negative), which must be equally
        spaced in time. The order of the payments in *Value* must be the same as
        the order in which the cash flows occur. *Value* is an one dimensional
        parameter of real numbers. *Value* given by positive numbers represent
        incoming amounts and *Value* given by negative numbers represent
        outgoing amounts. em Value must contain at least one positive and at
        least one negative number.

    *LowerBound*
        Indicates a minimum for the internal rate to be accepted by this
        function. The default is :math:`-1`.

    *UpperBound*
        Indicates a maximum for the internal rate to be accepted by this
        function. The default is :math:`5`.

    *Error*
        Indicates whether AIMMS should give an error if multiple solutions are
        found that satisfy the bounds. :math:`Error = 0`: if multiple solutions
        are found, return the solution with the smallest absolute value.
        :math:`Error = 1`: if multiple solutions are found, return an error
        message. The default is :math:`0`.

Return Value
------------

    The function :aimms:func:`InvestmentVariableInternalRateReturn` returns the
    internal rate of return for an investment based on a series of periodic
    cash flows. The internal rate of return is the rate received for an
    investment.

.. note::

    -  The function :aimms:func:`InvestmentVariableInternalRateReturn` can be used in
       an objective function or constraint. The input parameter *Value* can
       be used as a variable.

    -  The function :aimms:func:`InvestmentVariableInternalRateReturn` is similar to
       the Excel function ``IRR``.

.. seealso::

    The functions :aimms:func:`InvestmentVariableInternalRateReturnAll`, :aimms:func:`InvestmentVariableInternalRateReturnInPeriodic`.
