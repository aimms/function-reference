.. aimms:function:: SecurityPeriodicCouponRate(SettlementDate, MaturityDate, ParValue, Price, Redemption, Frequency, Yield, Basis)

.. _SecurityPeriodicCouponRate:

SecurityPeriodicCouponRate
==========================

The function :aimms:func:`SecurityPeriodicCouponRate` returns the coupon rate of a
security that pays interest at the end of each coupon period.

.. code-block:: aimms

    SecurityPeriodicCouponRate(
        SettlementDate,           ! (input) scalar string expression
        MaturityDate,             ! (input) scalar string expression
        ParValue,                 ! (input) numerical expression
        Price,                    ! (input) numerical expression
        Redemption,               ! (input) numerical expression
        Frequency,                ! (input) numerical expression
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

    *Redemption*
        The amount repaid for the security at the maturity date. *Redemption*
        must be a positive real number.

    *Frequency*
        The number of coupon payments in one year. *Frequency* must be 1
        (annual), 2 (semi-annual) or 4 (quarterly).

    *Yield*
        The yield of the security. *Yield* must be a nonnegative real number.

    *Basis*
        The day-count basis method to be used. The default is 1.

Return Value
------------

    The function :aimms:func:`SecurityPeriodicCouponRate` returns the interest rate
    per year of the security as a percentage of the par value.

.. note::

    This function can be used in an objective function or constraint and the
    input parameters *ParValue*, *Price*, *Redemption*, and *Yield* can be
    used as a variable.



Example
-------

The code:

.. code-block:: aimms

	_p_spcr := SecurityPeriodicCouponRate(
		SettlementDate :  "2024-01-01", 
		MaturityDate   :  "2030-01-01", 
		ParValue       :  100, 
		Price          :  100, 
		Redemption     :  100, 
		Frequency      :  4, 
		Yield          :  0.04, 
		Basis          :  1);
	block where single_column_display := 1, listing_number_precision := 6 ;
		display _p_spcr ;
	endblock ;

Produces:

.. code-block:: aimms

    _p_spcr := 0.040000 ;

References
-----------


    *   Day count basis :ref:`methods<ff.dcb>`. 
	
	*   General :ref:`equations<ff.sec.coupn>` for securities with multiple coupons.
