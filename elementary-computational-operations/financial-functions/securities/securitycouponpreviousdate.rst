.. aimms:function:: SecurityCouponPreviousDate(SettlementDate, MaturityDate, Frequency, PreviousDate)

.. _SecurityCouponPreviousDate:

SecurityCouponPreviousDate
==========================

The function :aimms:func:`SecurityCouponPreviousDate` returns the last coupon-date
previous to settlement date of a security that pays interest at the end
of each coupon period.

.. code-block:: aimms

    SecurityCouponPreviousDate(
        SettlementDate,           ! (input) scalar string expression
        MaturityDate,             ! (input) scalar string expression
        Frequency                 ! (input) numerical expression
        PreviousDate              ! (output) string parameter
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

    *PreviousDate*
        The date on which the coupon period, in which the settlement date falls,
        starts and on which the previous coupon period ends.

.. note::

    The function :aimms:func:`SecurityCouponPreviousDate` is similar to the Excel
    function `COUPPCD <https://support.microsoft.com/en-us/office/couppcd-function-2eb50473-6ee9-4052-a206-77a9a385d5b3>`_.



Example
-------

When was the last coupon issued, when the settlement date is Feb 1, and the coupons are issued quarterly until Jan 1?

.. code-block:: aimms

	SecurityCouponPreviousDate(
		SettlementDate :  "2025-02-01", 
		MaturityDate   :  "2030-01-01", 
		Frequency      :  4,
		PreviousDate   :  _sp_tcpd);
	block where single_column_display := 1, listing_number_precision := 6 ;
		display _sp_tcpd ;
	endblock ;

Here it coincides with the start of every quarter, which is also Jan 1:

.. code-block:: aimms

    _sp_tcpd := "2025-01-01" ;

.. seealso::

    *  General :ref:`equations<ff.sec.coupn>` for securities with multiple coupons.
