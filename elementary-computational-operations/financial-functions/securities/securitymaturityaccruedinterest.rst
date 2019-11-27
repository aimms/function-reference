.. aimms:function:: SecurityMaturityAccruedInterest(IssueDate, SettlementDate, ParValue, CouponRate, Basis)

.. _SecurityMaturityAccruedInterest:

SecurityMaturityAccruedInterest
===============================

The function :aimms:func:`SecurityMaturityAccruedInterest` returns the accrued
interest for a security that pays interest at maturity.

.. code-block:: aimms

    SecurityMaturityAccruedInterest(
        IssueDate,                ! (input) scalar string expression
        SettlementDate,           ! (input) scalar string expression
        ParValue,                 ! (input) numerical expression
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

    *ParValue*
        The starting value of the security at issue date. *ParValue* must be a
        positive real number.

    *CouponRate*
        The annual interest rate of the security as a percentage of the par
        value. *CouponRate* must be a nonnegative real number.

    *Basis*
        The day-count basis method to be used. The default is 1.

Return Value
------------

    The function :aimms:func:`SecurityMaturityAccruedInterest` returns the interest
    accrued from issue date until settlement date.

.. note::

    -  This function can be used in an objective function or constraint and
       the input parameters *CouponRate* and *ParValue* can be used as a
       variable.

    -  The function :aimms:func:`SecurityMaturityAccruedInterest` is similar to the
       Excel function ``ACCRINTM``.

.. seealso::

    Day count basis :ref:`methods<ff.dcb>`. General :ref:`equations<ff.sec.coup1>` for securities with one coupon.
