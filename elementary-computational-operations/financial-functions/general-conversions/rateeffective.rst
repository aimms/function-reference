.. aimms:function:: RateEffective(NominalRate, NumberPeriods)

.. _RateEffective:

RateEffective
=============

The function :aimms:func:`RateEffective` returns the effective annual interest
rate, expressed as a fraction, on the basis of a nominal interest rate
plus the number of compounding periods per year.

.. code-block:: aimms

    RateEffective(
        NominalRate,             ! (input) numerical expression
        NumberPeriods            ! (input) numerical expression
        )

Arguments
---------

    *NominalRate*
        The nominal annual interest rate expressed as a fraction. *NominalRate*
        must be a nonnegative decimal number.

    *NumberPeriods*
        The number of compounding periods per year. *NumberPeriods* must be a
        positive integer.

Return Value
------------

    The function :aimms:func:`RateEffective` returns the effective annual interest
    rate expressed as a fraction.

Equation
--------

    The conversion between nominal and effective rates is based on the
    equation

    .. math:: r_{\textit{eff}} = \left( 1 + \frac{r_{\textit{nom}}}{n} \right)^n - 1

    \ where :math:`r_{\textit{eff}}` is the effective annual rate,
    :math:`r_{\textit{nom}}` the nominal annual rate and :math:`n` the
    number of compounding periods.

.. note::

    -  This function can be used in an objective function or constraint, and
       the input parameter *NominalRate* can be used as a variable.

    -  The function :aimms:func:`RateEffective` is similar to the Excel function
       ``EFFECT``.

.. seealso::

    The function :aimms:func:`RateNominal`.
