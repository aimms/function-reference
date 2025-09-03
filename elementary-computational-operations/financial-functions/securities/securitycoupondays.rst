.. aimms:function:: SecurityCouponDays(SettlementDate, MaturityDate, Frequency, Basis)

.. _SecurityCouponDays:

SecurityCouponDays
==================

The function :aimms:func:`SecurityCouponDays` returns the number of days of the
coupon period in which settlement date falls. In other words the number
of days from the last coupon-date previous to settlement date until the
first coupon-date next to settlement date of a security that pays
interest at the end of each coupon period.

.. code-block:: aimms

    SecurityCouponDays(
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

    The function :aimms:func:`SecurityCouponDays` returns the number of days of the
    coupon period in which the settlement date falls.

.. note::

    The function :aimms:func:`SecurityCouponDays` is similar to the Excel function
    `COUPDAYS <https://support.microsoft.com/en-us/office/coupdays-function-cc64380b-315b-4e7b-950c-b30b0a76f671>`_.



Example
-------

The length of the coupon period in which settlement day is:

.. code-block:: aimms

    _p_scd := SecurityCouponDays(
        SettlementDate :  "2025-02-01", 
        MaturityDate   :  "2030-01-01", 
        Frequency      :  4,
        Basis          :  1);
    block where single_column_display := 1, listing_number_precision := 6 ;
        display _p_scd ;
    endblock ;

Day basis 1, just three months, each of 30 days:

.. code-block:: aimms

    _p_scd := 90 ;

.. seealso::

    *   Day count basis :ref:`methods<ff.dcb>`. 
    *   General :ref:`equations<ff.sec.coupn>` for securities with multiple coupons.
