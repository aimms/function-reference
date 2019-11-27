.. aimms:function:: SecurityMaturityPrice(IssueDate, SettlementDate, MaturityDate, ParValue, CouponRate, Yield, Basis)

.. _SecurityMaturityPrice:

SecurityMaturityPrice
=====================

The function :aimms:func:`SecurityMaturityPrice` returns the price at settlement
date of a security that pays interest at maturity.

.. code-block:: aimms

    SecurityMaturityPrice(
        IssueDate,                ! (input) scalar string expression
        SettlementDate,           ! (input) scalar string expression
        MaturityDate,             ! (input) scalar string expression
        ParValue,                 ! (input) numerical expression
        CouponRate,               ! (input) numerical expression
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

    *CouponRate*
        The annual interest rate of the security as a percentage of the par
        value. *CouponRate* must be a nonnegative real number.

    *Yield*
        The yield of the security. *Yield* must be a nonnegative real number.

    *Basis*
        The day-count basis method to be used. The default is 1.

Return Value
------------

    The function :aimms:func:`SecurityMaturityPrice` returns the price of the security
    at settlement date.

.. note::

    -  This function can be used in an objective function or constraint and
       the input parameters *ParValue*, *CouponRate*, and *Yield* can be
       used as a variable.

    -  The function :aimms:func:`SecurityMaturityPrice` is similar to the Excel
       function ``PRICEMAT``.

.. seealso::

    Day count basis :ref:`methods<ff.dcb>`. General :ref:`equations<ff.sec.coup1>` for securities with one coupon.
