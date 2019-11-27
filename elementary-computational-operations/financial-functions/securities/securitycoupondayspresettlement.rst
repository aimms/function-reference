.. aimms:function:: SecurityCouponDaysPreSettlement(SettlementDate, MaturityDate, Frequency, Basis)

.. _SecurityCouponDaysPreSettlement:

SecurityCouponDaysPreSettlement
===============================

The function :aimms:func:`SecurityCouponDaysPreSettlement` returns the number of
days from the last coupon-date previous to settlement date until
settlement date of a security that pays interest at the end of each
coupon period.

.. code-block:: aimms

    SecurityCouponDaysPreSettlement(
        SettlementDate,           ! (input) scalar string expression
        MaturityDate,             ! (input) scalar string expression
        Frequency,                ! (input) numerical expression
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

    *Frequency*
        The number of coupon payments in one year. *Frequency* must be 1
        (annual), 2 (semi-annual) or 4 (quarterly).

    *Basis*
        The day-count basis method to be used. The default is 1.

Return Value
------------

    The function :aimms:func:`SecurityCouponDaysPreSettlement` returns the number of
    days from the previous coupon-date until the settlement date, using the
    specified day-count basis.

.. note::

    The function :aimms:func:`SecurityCouponDaysPreSettlement` is similar to the Excel
    function ``COUPDAYBS``.

.. seealso::

    Day count basis :ref:`methods<ff.dcb>`. General :ref:`equations<ff.sec.coupn>` for securities with multiple coupons.
