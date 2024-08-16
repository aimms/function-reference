.. aimms:function:: TreasuryBillBondEquivalent(SettlementDate, MaturityDate, DiscountRate)

.. _TreasuryBillBondEquivalent:

TreasuryBillBondEquivalent
==========================

The function :aimms:func:`TreasuryBillBondEquivalent` returns the bond equivalent
yield of a treasury bill. A Treasury bill is a discounted security with
less than one year from settlement until maturity, the number of days in
one year is fixed at 360 and redemption is fixed at 100.

.. code-block:: aimms

    TreasuryBillBondEquivalent(
        SettlementDate,           ! (input) scalar string expression
        MaturityDate,             ! (input) scalar string expression
        DiscountRate              ! (input) numerical expression
        )

Arguments
---------

    *SettlementDate*
        The date of settlement of the security. *SettlementDate* must be given
        in a date format.

    *MaturityDate*
        The date of maturity of the security. *MaturityDate* must also be in
        date format and must be a date after *SettlementDate*.

    *DiscountRate*
        The discount rate of the security as a percentage of the redemption.
        *DiscountRate* must be a positive real number.

Return Value
------------

    The function :aimms:func:`TreasuryBillBondEquivalent` returns the bond equivalent
    yield of a Treasury bill.

.. note::

    -  This function can be used in an objective function or constraint and
       the input parameter *DiscountRate* can be used as a variable.

    -  The function :aimms:func:`TreasuryBillBondEquivalent` is similar to the Excel
       function `TBILLEQ <https://support.microsoft.com/en-us/office/tbilleq-function-2ab72d90-9b4d-4efe-9fc2-0f81f2c19c8c>`.

Example
-------

Bond equivalent yield for a treasury bill, half a year out, 10%:

.. code-block:: aimms

	_p_tbbe := TreasuryBillBondEquivalent(
		SettlementDate :  "2024-07-01", 
		MaturityDate   :  "2025-01-01", 
		DiscountRate   :  0.1);
	block where single_column_display := 1, listing_number_precision := 6 ;
		display _p_tbbe ;
	endblock ;

Well:

.. code-block:: aimms

    _p_tbbe := 0.106850 ;

References
-----------

    *   General :ref:`equations<ff.sec.disc>` for discounted securities.

