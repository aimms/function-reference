.. aimms:function:: RateNominal(EffectiveRate, NumberPeriods)

.. _RateNominal:

RateNominal
===========

The function :aimms:func:`RateNominal` returns the nominal annual interest rate,
expressed as a fraction, on the basis of an effective annual interest
rate plus the number of compounding periods per year.

.. code-block:: aimms

    RateNominal(
        EffectiveRate,             ! (input) numerical expression
        NumberPeriods              ! (input) numerical expression
        )

Arguments
---------

    *EffectiveRate*
        The effective annual interest rate expressed as a fraction.
        *EffectiveRate* must be a nonnegative decimal number.

    *NumberPeriods*
        The number of compounding periods per year. *NumberPeriods* must be a
        positive integer.

Return Value
------------

    The function :aimms:func:`RateNominal` returns the nominal annual interest rate
    expressed as a fraction.

.. note::

    -  The equation on which the conversion between nominal and effective
       rates is based, is explained for the function :aimms:func:`RateEffective` (the inverse
       of :aimms:func:`RateNominal`).

    -  This function can be used in an objective function or constraint, and
       the input parameter *EffectiveRate* can be used as a variable.

    -  The function :aimms:func:`RateNominal` is similar to the Excel function
       ``NOMINAL``.

.. seealso::

    The function :aimms:func:`RateEffective`.
