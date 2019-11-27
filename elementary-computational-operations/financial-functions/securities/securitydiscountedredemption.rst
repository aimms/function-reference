.. aimms:function:: SecurityDiscountedRedemption(SettlementDate, MaturityDate, Price, DiscountRate, Basis)

.. _SecurityDiscountedRedemption:

SecurityDiscountedRedemption
============================

The function :aimms:func:`SecurityDiscountedRedemption` returns the repayment at
maturity date of a discounted security.

.. code-block:: aimms

    SecurityDiscountedRedemption(
        SettlementDate,           ! (input) scalar string expression
        MaturityDate,             ! (input) scalar string expression
        Price,                    ! (input) numerical expression
        DiscountRate,             ! (input) numerical expression
        [Basis]                   ! (optional) numerical expression
        )

Arguments
---------

    *SettlementDate*
        The date of settlement of the security. *SettlementDate* must be given
        in a date format.

    *MaturityDate*
        The date of maturity of the security. *MaturityDate* must also be in
        date format and must be a date after *SettlementDate*.

    *Price*
        The price of the security at settlement date. *Price* must be a positive
        real number.

    *DiscountRate*
        The rate the security's value increases per year as a percentage of the
        redemption value. *DiscountRate* must be a positive real number.

    *Basis*
        The day-count basis method to be used. The default is 1.

Return Value
------------

    The function :aimms:func:`SecurityDiscountedRedemption` returns the amount paid at
    maturity date.

.. note::

    -  This function can be used in an objective function or constraint and
       the input parameters *Price* and *DiscountRate* can be used as a
       variable.

    -  The function :aimms:func:`SecurityDiscountedRedemption` is similar to the Excel
       function ``RECEIVED``.

.. seealso::

    Day count basis :ref:`methods<ff.dcb>`. General :ref:`equations<ff.sec.disc>` for discounted securities.
