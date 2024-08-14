.. aimms:function:: SecurityDiscountedPrice(SettlementDate, MaturityDate, Redemption, DiscountRate, Basis)

.. _SecurityDiscountedPrice:

SecurityDiscountedPrice
=======================

The function :aimms:func:`SecurityDiscountedPrice` returns the price of a
discounted security at settlement date.

.. code-block:: aimms

    SecurityDiscountedPrice(
        SettlementDate,  ! (input) scalar string expression
        MaturityDate,    ! (input) scalar string expression
        Redemption,      ! (input) numerical expression
        DiscountRate,    ! (input) numerical expression
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

    *Redemption*
        The amount repaid at maturity date. *Redemption* must be a positive real
        number.

    *DiscountRate*
        The rate the security's value increases per year as a fraction of the
        redemption value. *DiscountRate* must be a positive real number.

    *Basis*
        The day-count basis method to be used. The default is 1.

Return Value
------------

    The function :aimms:func:`SecurityDiscountedPrice` returns the price of the
    security at settlement date.

.. note::

    -  This function can be used in an objective function or constraint and
       the input parameters *Redemption* and *DiscountRate* can be used as a
       variable.

    -  The function :aimms:func:`SecurityDiscountedPrice` is similar to the Excel
       function `PRICEDISC <https://support.microsoft.com/en-us/office/pricedisc-function-d06ad7c1-380e-4be7-9fd9-75e3079acfd3>_`.


Example
-------

Selling a security one year before maturity with a discount rate of 10%:

.. code-block:: aimms

    _p_sdp := SecurityDiscountedPrice(
        SettlementDate :  "2024-01-01", 
        MaturityDate   :  "2025-01-01", 
        Redemption     :  100, 
        DiscountRate   :  0.1, 
        Basis          :  1);
    block where single_column_display := 1, listing_number_precision := 6 ;
        display _p_sdp ;
    endblock ;

This results in the following discounted price:

.. code-block:: aimms

    _p_sdp := 90 ;

References
-----------

    *   Day count basis :ref:`methods<ff.dcb>`. 
    
    *   General :ref:`equations<ff.sec.disc>` for discounted securities.
