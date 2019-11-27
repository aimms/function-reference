.. aimms:function:: SecurityCouponNextDate(SettlementDate, MaturityDate, Frequency, NextDate)

.. _SecurityCouponNextDate:

SecurityCouponNextDate
======================

The function :aimms:func:`SecurityCouponNextDate` returns the first coupon-date
next to settlement date of a security that pays interest at the end of
each coupon period.

.. code-block:: aimms

    SecurityCouponNextDate(
        SettlementDate,           ! (input) scalar string expression
        MaturityDate,             ! (input) scalar string expression
        Frequency                 ! (input) numerical expression
        NextDate                  ! (output) string parameter
        )

Arguments
---------

    *SettlementDate*
        The date of settlement of the security. *SettlementDate* must be in date
        format.

    *MaturityDate*
        The date of maturity of the security. *MaturityDate* must also be in
        date format and must be a date after *SettlementDate*.

    *Frequency*
        The number of coupon payments in one year. *Frequency* must be 1
        (annual), 2 (semi-annual) or 4 (quarterly).

    *NextDate*
        The date on which the coupon period ends and on which the next coupon
        period starts.

.. note::

    The function :aimms:func:`SecurityCouponNextDate` is similar to the Excel function
    ``COUPNCD``.

.. seealso::

    General :ref:`equations<ff.sec.coupn>` for securities with multiple coupons.
