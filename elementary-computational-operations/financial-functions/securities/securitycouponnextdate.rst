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
    `COUPNCD <https://support.microsoft.com/en-us/office/coupncd-function-fd962fef-506b-4d9d-8590-16df5393691f>_`.


Example
-------

When will the next coupon be issued, when the settlement date is Feb 1, and the coupons are issued quarterly until Jan 1?

.. code-block:: aimms

	SecurityCouponNextDate(
		SettlementDate :  "2025-02-01", 
		MaturityDate   :  "2030-01-01", 
		Frequency      :  4,
		NextDate       :  _sp_tcnd);
	block where single_column_display := 1, listing_number_precision := 6 ;
		display _sp_tcnd ;
	endblock ;

Here it coincides with the start of every quarter, which is also Jan 1:

.. code-block:: aimms

    _sp_tcnd := "2025-04-01" ;

References
-----------

    *   General :ref:`equations<ff.sec.coupn>` for securities with multiple coupons.
