.. aimms:function:: SecurityDiscountedRate(SettlementDate, MaturityDate, Price, Redemption, Basis)

.. _SecurityDiscountedRate:

SecurityDiscountedRate
======================

The function :aimms:func:`SecurityDiscountedRate` returns the discount rate of a
discounted security.

.. code-block:: aimms

    SecurityDiscountedRate(
        SettlementDate,  ! (input) scalar string expression
        MaturityDate,    ! (input) scalar string expression
        Price,           ! (input) numerical expression
        Redemption,      ! (input) numerical expression
        [Basis]          ! (optional) numerical expression
        )

Arguments
---------

    *SettlementDate*
        The date of settlement of the security. *SettlementDate* must be given
        in a date format.

    *MaturityDate*
        The date of maturity of the security. *MaturityDate* must also be in
        date format and must be a date after *SettlementDate*.

    *Price*
        The price of the security at settlement date. *Price* must be a positive
        real number.

    *Redemption*
        The amount repaid at maturity date. *Redemption* must be a positive real
        number.

    *Basis*
        The day-count basis method to be used. The default is 1.

Return Value
------------

    The function :aimms:func:`SecurityDiscountedRate` returns the annual rate the
    security's value increases as a fraction of the redemption value.

.. note::

    -  This function can be used in an objective function or constraint and
       the input parameters *Price* and *Redemption* can be used as a
       variable.

    -  The function :aimms:func:`SecurityDiscountedRate` is similar to the Excel
       function `DISC <https://support.microsoft.com/en-us/office/disc-function-71fce9f3-3f05-4acf-a5a3-eac6ef4daa53>`_.

Example
-------

Knowing price, redemption, and length period; what was the interest (with respect to redemption)?

.. code-block:: aimms

	_p_sdr := SecurityDiscountedRate(
		SettlementDate :  "2024-01-01", 
		MaturityDate   :  "2025-01-01", 
		Price          :  90, 
		Redemption     :  100, 
		Basis          :  1);
	block where single_column_display := 1, listing_number_precision := 6 ;
		display _p_sdr ;
	endblock ;

This results in the following interest:

.. code-block:: aimms

    _p_sdr := 0.100000 ;

References
-----------

    *   Day count basis :ref:`methods<ff.dcb>`. 
	
	*   General :ref:`equations<ff.sec.disc>` for discounted securities.
