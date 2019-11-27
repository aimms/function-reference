.. aimms:function:: InvestmentVariableInternalRateReturnAll(Value, Mode, NumberSolutions, IRR)

.. _InvestmentVariableInternalRateReturnAll:

InvestmentVariableInternalRateReturnAll
=======================================

The procedure :aimms:func:`InvestmentVariableInternalRateReturnAll` returns the
internal rate of return for an investment based on a series of periodic
cash flows. The internal rate of return is the rate received for an
investment consisting of payments (negative values) and income (positive
values).

.. code-block:: aimms

    InvestmentVariableInternalRateReturnAll(
        Value,                   ! (input) one-dimensional numerical expression
        Mode,                    ! (input) numerical expression
        NumberSolutions,         ! (output) numerical expression
        IRR                      ! (output) one-dimensional numerical expression
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

    *Mode*
        Indicates whether all the solutions need to be found or just one.
        :math:`Mode = 0`: the search for solutions stops after one solution is
        found. :math:`Mode = 1`: the search for solutions continues till all
        solutions are found.

    *NumberSolutions*
        The number of solutions found. When :math:`Mode = 0` the
        *NumberSolutions* will be 1.

    *IRR*
        The internal rate of return for the investment. There is not always a
        unique solution for *IRR*. Dependent on *Mode* one solution or all the
        solutions will be given. Solutions smaller than -1 are not supposed to
        be relevant, so the search for solutions is limited to the area greater
        than -1.

Equation
--------

    The internal rate of return :math:`r` is a solution of the equation

    .. math:: \sum_{i=1}^n \frac{p_i}{(1+r)^i} = 0

    \ where :math:`p_i` are the periodic payments.

.. note::

    -  The internal rate of return is the interest rate at which the
       investment has a zero net present value.

    -  When you want to use this procedure in an objective function or
       constraint you have to use *InvestmentVariableInternalRateReturn*.

    -  The function :aimms:func:`InvestmentVariableInternalRateReturnAll` is similar
       to the Excel function ``IRR``.

.. seealso::

    The functions :aimms:func:`InvestmentVariableInternalRateReturn`, :aimms:func:`InvestmentVariableInternalRateReturnInPeriodic`.
