.. aimms:function:: SecurityCouponDaysPostSettlement(SettlementDate, MaturityDate, Frequency, Basis)

.. _SecurityCouponDaysPostSettlement:

SecurityCouponDaysPostSettlement
================================

The function :aimms:func:`SecurityCouponDaysPostSettlement` returns the number of
days from the first coupon-date next to settlement date until settlement
date of a security that pays interest at the end of each coupon period.

.. code-block:: aimms

    SecurityCouponDaysPostSettlement(
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

    The function :aimms:func:`SecurityCouponDaysPostSettlement` returns the number of
    days from the first coupon-date next to settlement date until settlement
    date.

.. note::

    The function :aimms:func:`SecurityCouponDaysPostSettlement` is similar to the
    Excel function `COUPDAYSNC <https://support.microsoft.com/en-us/office/coupdaysnc-function-5ab3f0b2-029f-4a8b-bb65-47d525eea547>`.



Example
-------

The number of days from the settlement date up to the next coupon date:

.. code-block:: aimms

    _p_scdps := SecurityCouponDaysPostSettlement(
        SettlementDate :  "2025-02-01", 
        MaturityDate   :  "2030-01-01", 
        Frequency      :  4,
        Basis          :  1);
    block where single_column_display := 1, listing_number_precision := 6 ;
        display _p_scdps ;
    endblock ;

Day basis 1, just two months, so that is 60 days:

.. code-block:: aimms

    _p_scdps := 60 ;

References
-----------


    *   Day count basis :ref:`methods<ff.dcb>`. 
    
    *   General :ref:`equations<ff.sec.coupn>` for securities with multiple coupons.
