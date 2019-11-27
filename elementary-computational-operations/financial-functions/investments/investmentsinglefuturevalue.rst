.. aimms:function:: InvestmentSingleFutureValue(PresentValue, PeriodicRate)

.. _InvestmentSingleFutureValue:

InvestmentSingleFutureValue
===========================

The function :aimms:func:`InvestmentSingleFutureValue` returns the future value,
the cash balance, of a payment made at this moment, present value, with
periodic interest rates.

.. code-block:: aimms

    InvestmentSingleFutureValue(
        PresentValue,            ! (input) numerical expression
        PeriodicRate             ! (input) one-dimensional numerical expression
        )

Arguments
---------

    *PresentValue*
        Payment made at the start of the first period. *PresentValue* must be a
        real number. If *PresentValue* is a negative number it represents an
        outgoing amount and when it is a positive number it represents an
        incoming amount.

    *PeriodicRate*
        Interest rates which differ per period. *PeriodicRate* is a
        one-dimensional parameter, which should contain at least one nonzero
        number. The periods must be equally spaced in time and the interest
        rates must be ordered.

Return Value
------------

    The function :aimms:func:`InvestmentSingleFutureValue` returns the future value of
    the present value, using the periodic interest rates.

Equation
--------

    The future value :math:`v_f` is computed through the equation

    .. math:: v_f = v_p\prod_{i=1}^n(1+r_i)

    \ where :math:`v_p` is the present value, and :math:`r_i` the variable,
    periodic interest rates.

.. note::

    -  This function can be used in an objective function or constraint and
       the input parameters *PresentValue* and *PeriodicRate* can be used as
       a variable.

    -  The function :aimms:func:`InvestmentSingleFutureValue` is similar to the Excel
       function ``FVSCHEDULE``.
