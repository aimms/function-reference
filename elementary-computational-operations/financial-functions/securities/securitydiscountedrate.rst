.. aimms:function:: SecurityDiscountedRate(SettlementDate, MaturityDate, Price, Redemption, Basis)

.. _SecurityDiscountedRate:

SecurityDiscountedRate
======================

The function :aimms:func:`SecurityDiscountedRate` returns the discount rate of a
discounted security.

.. code-block:: aimms

    SecurityDiscountedRate(
        SettlementDate,           ! (input) scalar string expression
        MaturityDate,             ! (input) scalar string expression
        Price,                    ! (input) numerical expression
        Redemption,               ! (input) numerical expression
        [Basis]                   ! (optional) numerical expression
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
    security's value increases as a percentage of the redemption value.

.. note::

    -  This function can be used in an objective function or constraint and
       the input parameters *Price* and *Redemption* can be used as a
       variable.

    -  The function :aimms:func:`SecurityDiscountedRate` is similar to the Excel
       function ``DISC``.

.. seealso::

    Day count basis :ref:`methods<ff.dcb>`. General :ref:`equations<ff.sec.disc>` for discounted securities.
