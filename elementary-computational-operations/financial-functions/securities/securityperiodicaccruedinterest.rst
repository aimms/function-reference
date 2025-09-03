.. aimms:function:: SecurityPeriodicAccruedInterest(SettlementDate, MaturityDate, ParValue, Frequency, CouponRate, Basis)

.. _SecurityPeriodicAccruedInterest:

SecurityPeriodicAccruedInterest
===============================

The function :aimms:func:`SecurityPeriodicAccruedInterest` returns the accrued
interest from the begin of the coupon period until the settlement date
for a security that pays interest at the end of each coupon period.

.. code-block:: aimms

    SecurityPeriodicAccruedInterest(
        SettlementDate, ! (input) scalar string expression
        MaturityDate,   ! (input) scalar string expression
        ParValue,       ! (input) numerical expression
        Frequency,      ! (input) numerical expression
        CouponRate,     ! (input) numerical expression
        [Basis]         ! (optional) numerical expression
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

    *Frequency*
        The number of coupon payments in one year. *Frequency* must be 1
        (annual), 2 (semi-annual) or 4 (quarterly).

    *CouponRate*
        The annual interest rate of the security as a percentage of the par
        value. *CouponRate* must be a nonnegative real number.

    *Basis*
        The day-count basis method to be used. The default is 1.

Return Value
------------

    The function :aimms:func:`SecurityPeriodicAccruedInterest` returns the interest
    accrued from the begin of the coupon period until settlement date.

.. note::

    This function can be used in an objective function or constraint and the
    input parameters *ParValue* and *CouponRate* can be used as a variable.


Example
-------

Security owned for half a year since last coupon date, against 4%, and value 100.

.. code-block:: aimms

    _p_spai := SecurityPeriodicAccruedInterest(
        SettlementDate :  "2024-07-01", 
        MaturityDate   :  "2025-01-01", 
        ParValue       :  100, 
        Frequency      :  1, 
        CouponRate     :  0.04, 
        Basis          :  1);
    block where single_column_display := 1, listing_number_precision := 6 ;
        display _p_spai ;
    endblock ;

Results in an accrued interest of 2:

.. code-block:: aimms

    _p_spai := 2 ;

.. seealso::

    *  Day count basis :ref:`methods<ff.dcb>`. 
    *  General :ref:`equations<ff.sec.coupn>` for securities with multiple coupons.
