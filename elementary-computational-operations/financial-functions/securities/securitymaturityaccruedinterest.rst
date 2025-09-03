.. aimms:function:: SecurityMaturityAccruedInterest(IssueDate, SettlementDate, ParValue, CouponRate, Basis)

.. _SecurityMaturityAccruedInterest:

SecurityMaturityAccruedInterest
===============================

The function :aimms:func:`SecurityMaturityAccruedInterest` returns the accrued
interest for a security that pays interest at maturity.

.. code-block:: aimms

    SecurityMaturityAccruedInterest(
        IssueDate,       ! (input) scalar string expression
        SettlementDate,  ! (input) scalar string expression
        ParValue,        ! (input) numerical expression
        CouponRate,      ! (input) numerical expression
        [Basis]          ! (optional) numerical expression
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
        The annual interest rate of the security as a fraction of the par
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
       Excel function `ACCRINTM <https://support.microsoft.com/en-us/office/accrintm-function-f62f01f9-5754-4cc4-805b-0e70199328a7>`_.


Example
-------

How much interest was paid for a security 

* over a period of five years, 

* with an interest rate of 7%, 

* and bought for a 100 at the time?

.. code-block:: aimms

    _p_smai := SecurityMaturityAccruedInterest(
        IssueDate      :  "2020-01-01", 
        SettlementDate :  "2025-01-01", 
        ParValue       :  100, 
        CouponRate     :  0.07, 
        Basis          :  1);
    block where single_column_display := 1, listing_number_precision := 6 ;
        display _p_smai ;
    endblock ;

No interest on interest, so:

.. code-block:: aimms

    _p_smai := 35 ;

.. seealso::

    *   Day count basis :ref:`methods<ff.dcb>`. 
    *   General :ref:`equations<ff.sec.coup1>` for securities with one coupon.
