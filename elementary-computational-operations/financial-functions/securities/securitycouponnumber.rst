.. aimms:function:: SecurityCouponNumber(SettlementDate, MaturityDate, Frequency)

.. _SecurityCouponNumber:

SecurityCouponNumber
====================

The function :aimms:func:`SecurityCouponNumber` returns the number of coupons from
settlement date and maturity date of a security that pays interest at
the end of each coupon period.

.. code-block:: aimms

    SecurityCouponNumber(
        SettlementDate,           ! (input) scalar string expression
        MaturityDate,             ! (input) scalar string expression
        Frequency,                ! (input) numerical expression
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

Return Value
------------

    The function :aimms:func:`SecurityCouponNumber` returns the number of coupon
    payments from the settlement date until the maturity date.

.. note::

    The function :aimms:func:`SecurityCouponNumber` is similar to the Excel function
    `COUPNUM <https://support.microsoft.com/en-us/office/coupnum-function-a90af57b-de53-4969-9c99-dd6139db2522>_`.


Example
-------

How many quarterly coupons are paid out over a period of five years?

.. code-block:: aimms

	_p_scn := SecurityCouponNumber(
		SettlementDate :  "2025-01-01", 
		MaturityDate   :  "2030-01-01", 
		Frequency      :  4);
	block where single_column_display := 1, listing_number_precision := 6 ;
		display _p_scn ;
	endblock ;

Twenty:

.. code-block:: aimms

    _p_scn := 20 ;

References
-----------


    *   Day count basis :ref:`methods<ff.dcb>`. 
	
	*   General :ref:`equations<ff.sec.coupn>` for securities with multiple coupons.
