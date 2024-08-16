.. aimms:function:: SecurityMaturityCouponRate(IssueDate, SettlementDate, MaturityDate, ParValue, Price, Yield, Basis)

.. _SecurityMaturityCouponRate:

SecurityMaturityCouponRate
==========================

The function :aimms:func:`SecurityMaturityCouponRate` returns the coupon rate of a
security that pays interest at maturity.

.. code-block:: aimms

    SecurityMaturityCouponRate(
        IssueDate,                ! (input) scalar string expression
        SettlementDate,           ! (input) scalar string expression
        MaturityDate,             ! (input) scalar string expression
        ParValue,                 ! (input) numerical expression
        Price,                    ! (input) numerical expression
        Yield,                    ! (input) numerical expression
        [Basis]                   ! (optional) numerical expression
        )

Arguments
---------

    *IssueDate*
        The date of issue of the security. *IssueDate* must be given in date
        format.

    *SettlementDate*
        The date of settlement of the security. *SettlementDate* must also be in
        date format and must be a date after *IssueDate*.

    *MaturityDate*
        The date of maturity of the security. *MaturityDate* must also be in
        date format and must be a date after *SettlementDate*.

    *ParValue*
        The starting value of the security at issue date. *ParValue* must be a
        positive real number.

    *Price*
        The price of the security at settlement date. *Price* must be a positive
        real number.

    *Yield*
        The yield of the security. *Yield* must be a nonnegative real number.

    *Basis*
        The day-count basis method to be used. The default is 1.

Return Value
------------

    The function :aimms:func:`SecurityMaturityCouponRate` returns the annual interest
    rate of the security as a percentage of the par value.

.. note::

    This function can be used in an objective function or constraint and the
    input parameters *ParValue*, *Price*, and *Yield* can be used as a
    variable.


Example
-------

The code:

.. code-block:: aimms

	_p_smcr := SecurityMaturityCouponRate(
		IssueDate      :  "2020-01-01", 
		SettlementDate :  "2024-01-01", 
		MaturityDate   :  "2025-01-01", 
		ParValue       :  100, 
		Price          :  99, 
		Yield          :  0.02, 
		Basis          :  1);
	block where single_column_display := 1, listing_number_precision := 6 ;
		display _p_smcr ;
	endblock ;

Produces in the listing file:

.. code-block:: aimms

    _p_smcr := 0.010652 ;

References
-----------

    *   Day count basis :ref:`methods<ff.dcb>`. 
	
	*   General :ref:`equations<ff.sec.coup1>` for securities with one coupon.
