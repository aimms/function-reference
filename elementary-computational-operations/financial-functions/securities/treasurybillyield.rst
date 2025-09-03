.. aimms:function:: TreasuryBillYield(SettlementDate, MaturityDate, Price)

.. _TreasuryBillYield:

TreasuryBillYield
=================

The function :aimms:func:`TreasuryBillYield` returns the yield of a Treasury bill
at settlement date. A Treasury bill is a discounted security with less
than one year from settlement until maturity, the number of days in one
year is fixed at 360 and redemption is fixed at 100.

.. code-block:: aimms

    TreasuryBillYield(
        SettlementDate,           ! (input) scalar string expression
        MaturityDate,             ! (input) scalar string expression
        Price                     ! (input) numerical expression
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
        The price the security is worth at this moment. *Price* must be a
        positive real number.

Return Value
------------

    The function :aimms:func:`TreasuryBillYield` returns the annual rate the Treasury
    bill's value increases as a percentage of the price.

.. note::

    -  This function can be used in an objective function or constraint and
       the input parameter *Price* can be used as a variable.

    -  The function :aimms:func:`TreasuryBillYield` is similar to the Excel function
       `TBILLYIELD <https://support.microsoft.com/en-us/office/tbillyield-function-6d381232-f4b0-4cd5-8e97-45b9c03468ba>`_.


Example
-------

What is the yield if a bond of 100 is bought for 95 and matures in half a year?

.. code-block:: aimms

	_p_tby := TreasuryBillYield(
		SettlementDate :  "2024-07-01", 
		MaturityDate   :  "2025-01-01", 
		Price          :  95);
	block where single_column_display := 1, listing_number_precision := 6 ;
		display _p_tby ;
	endblock ;

Well:

.. code-block:: aimms

    _p_tby := 0.102975 ;

.. seealso::

    *   General :ref:`equations<ff.sec.disc>` for discounted securities.
