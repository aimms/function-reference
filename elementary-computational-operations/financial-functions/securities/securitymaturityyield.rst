.. aimms:function:: SecurityMaturityYield(IssueDate, SettlementDate, MaturityDate, ParValue, Price, CouponRate, Basis)

.. _SecurityMaturityYield:

SecurityMaturityYield
=====================

The function :aimms:func:`SecurityMaturityYield` returns the yield of a security
that pays interest at maturity.

.. code-block:: aimms

    SecurityMaturityYield(
        IssueDate,                ! (input) scalar string expression
        SettlementDate,           ! (input) scalar string expression
        MaturityDate,             ! (input) scalar string expression
        ParValue,                 ! (input) numerical expression
        Price,                    ! (input) numerical expression
        CouponRate,               ! (input) numerical expression
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

    *CouponRate*
        The annual interest rate of the security as a percentage of the par
        value. *CouponRate* must be a nonnegative real number.

    *Basis*
        The day-count basis method to be used. The default is 1.

Return Value
------------

    The function :aimms:func:`SecurityMaturityYield` returns the annual rate the
    security's value increases as a percentage of the price.

.. note::

    -  This function can be used in an objective function or constraint and
       the input parameters *ParValue*, *Price*, and *CouponRate* can be
       used as a variable.

    -  The function :aimms:func:`SecurityMaturityYield` is similar to the Excel
       function ``YIELDMAT``.

.. seealso::

    Day count basis :ref:`methods<ff.dcb>`. General :ref:`equations<ff.sec.coup1>` for securities with one coupon.
