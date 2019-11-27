.. aimms:function:: SecurityPeriodicRedemption(SettlementDate, MaturityDate, ParValue, Price, Frequency, CouponRate, Yield, Basis)

.. _SecurityPeriodicRedemption:

SecurityPeriodicRedemption
==========================

The function :aimms:func:`SecurityPeriodicRedemption` returns the repayment at
maturity date of a security that pays interest at the end of each coupon
period.

.. code-block:: aimms

    SecurityPeriodicRedemption(
        SettlementDate,           ! (input) scalar string expression
        MaturityDate,             ! (input) scalar string expression
        ParValue,                 ! (input) numerical expression
        Price,                    ! (input) numerical expression
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

    *Price*
        The price of the security at settlement date. *Price* must be a positive
        real number.

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

    The function :aimms:func:`SecurityPeriodicRedemption` returns the amount repaid
    for the security at the maturity date.

.. note::

    This function can be used in an objective function or constraint and the
    input parameters *ParValue*, *Price*, *CouponRate*, and *Yield* can be
    used as a variable.

.. seealso::

    Day count basis :ref:`methods<ff.dcb>`. General :ref:`equations<ff.sec.coupn>` for securities with multiple coupons.
