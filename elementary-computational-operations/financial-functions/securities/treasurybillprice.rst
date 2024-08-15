.. aimms:function:: TreasuryBillPrice(SettlementDate, MaturityDate, DiscountRate)

.. _TreasuryBillPrice:

TreasuryBillPrice
=================

The function :aimms:func:`TreasuryBillPrice` returns the price of a Treasury bill
at settlement date. A Treasury bill is a discounted security with less
than one year from settlement until maturity, the number of days in one
year is fixed at 360 and redemption is fixed at 100.

.. code-block:: aimms

    TreasuryBillPrice(
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
        The discount rate of the security as a fraction of the redemption.
        *DiscountRate* must be a positive real number.

Return Value
------------

    The function :aimms:func:`TreasuryBillPrice` returns the price of a Treasury bill
    at settlement date.

.. note::

    -  This function can be used in an objective function or constraint and
       the input parameter *DiscountRate* can be used as a variable.

    -  The function :aimms:func:`TreasuryBillPrice` is similar to the Excel function
       `TBILLPRICE <https://support.microsoft.com/en-us/office/tbillprice-function-eacca992-c29d-425a-9eb8-0513fe6035a2>`_.


Example
-------

Half a year, 10%, what does this do?

.. code-block:: aimms

	_p_tbp := TreasuryBillPrice(
		SettlementDate :  "2024-07-01", 
		MaturityDate   :  "2025-01-01", 
		DiscountRate   :  0.1);
	block where single_column_display := 1, listing_number_precision := 6 ;
		display _p_tbp ;
	endblock ;

Well:

.. code-block:: aimms

    _p_tbp := 94.888889 ;

References
-----------

    *   General :ref:`equations<ff.sec.disc>` for discounted securities.
