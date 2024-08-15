.. aimms:function:: SecurityDiscountedYield(SettlementDate, MaturityDate, Price, Redemption, Basis)

.. _SecurityDiscountedYield:

SecurityDiscountedYield
=======================

The function :aimms:func:`SecurityDiscountedYield` returns the yield of a
discounted security at maturity date.

.. code-block:: aimms

    SecurityDiscountedYield(
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

    The function :aimms:func:`SecurityDiscountedYield` returns the annual rate the
    security's value increases as a fraction of the price.

.. note::

    -  This function can be used in an objective function or constraint and
       the input parameters *Price* and *Redemption* can be used as a
       variable.

    -  The function :aimms:func:`SecurityDiscountedYield` is similar to the Excel
       function `YIELDDISC <https://support.microsoft.com/en-us/office/yielddisc-function-a9dbdbae-7dae-46de-b995-615faffaaed7>`_.


Example
-------

Knowing price, redemption, and length period; what was the interest (with respect to price)?

.. code-block:: aimms

    _p_sdf := SecurityDiscountedYield(
        SettlementDate :  "2024-01-01", 
        MaturityDate   :  "2025-01-01", 
        Price          :  90, 
        Redemption     :  100, 
        Basis          :  1);
    block where single_column_display := 1, listing_number_precision := 6 ;
        display _p_sdf ;
    endblock ;

This results in the following interest:

.. code-block:: aimms

    _p_sdf := 0.111111 ;

References
-----------

    *   Day count basis :ref:`methods<ff.dcb>`. 
    
    *   General :ref:`equations<ff.sec.disc>` for discounted securities.
