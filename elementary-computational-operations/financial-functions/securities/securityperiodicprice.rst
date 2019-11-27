.. aimms:function:: SecurityPeriodicPrice(SettlementDate, MaturityDate, ParValue, Redemption, Frequency, CouponRate, Yield, Basis)

.. _SecurityPeriodicPrice:

SecurityPeriodicPrice
=====================

The function :aimms:func:`SecurityPeriodicPrice` returns the price at settlement
date of a security that pays interest at the end of each coupon period.

.. code-block:: aimms

    SecurityPeriodicPrice(
        SettlementDate,           ! (input) scalar string expression
        MaturityDate,             ! (input) scalar string expression
        ParValue,                 ! (input) numerical expression
        Redemption,               ! (input) numerical expression
        Frequency,                ! (input) numerical expression
        CouponRate,               ! (input) numerical expression
        Yield,                    ! (input) numerical expression
        [Basis]                   ! (optional) numerical expression
        )

Arguments
---------

    *SettlementDate*
        The date of settlement of the security. *SettlementDate* must be in date
        format.

    *MaturityDate*
        The date of maturity of the security. *MaturityDate* must also be in
        date format and must be a date after *SettlementDate*.

    *ParValue*
        The starting value of the security at issue date. *ParValue* must be a
        positive real number.

    *Redemption*
        The amount repaid for the security at the maturity date. *Redemption*
        must be a positive real number.

    *Frequency*
        The number of coupon payments in one year. *Frequency* must be 1
        (annual), 2 (semi-annual) or 4 (quarterly).

    *CouponRate*
        The annual interest rate of the security as a percentage of the par
        value. *CouponRate* must be a nonnegative real number.

    *Yield*
        The yield of the security. *Yield* must be a nonnegative real number.

    *Basis*
        The day-count basis method to be used. The default is 1.

Return Value
------------

    The function :aimms:func:`SecurityPeriodicPrice` returns the price of the security
    at settlement date.

.. note::

    -  This function can be used in an objective function or constraint and
       the input parameters *ParValue*, *Redemption*, *CouponRate*, and
       *Yield* can be used as a variable.

    -  The function :aimms:func:`SecurityPeriodicPrice` is similar to the Excel
       function ``PRICE``.

.. seealso::

    Day count basis :ref:`methods<ff.dcb>`. General :ref:`equations<ff.sec.coupn>` for securities with multiple coupons.
