.. aimms:function:: SecurityPeriodicYield(SettlementDate, MaturityDate, ParValue, Price, Redemption, Frequency, CouponRate, Basis, LowerBound, UpperBound, Error)

.. _SecurityPeriodicYield:

SecurityPeriodicYield
=====================

The function :aimms:func:`SecurityPeriodicYield` returns the yield of a security
that pays interest at the end of each coupon period. This function uses
the procedure ``SecurityPeriodicYieldAll`` to determine all possible
yields and returns the yield that is within the specified bounds.

.. code-block:: aimms

    SecurityPeriodicYield(
        SettlementDate,  ! (input) scalar string expression
        MaturityDate,    ! (input) scalar string expression
        ParValue,        ! (input) numerical expression
        Price,           ! (input) numerical expression
        Redemption,      ! (input) numerical expression
        Frequency,       ! (input) numerical expression
        CouponRate,      ! (input) numerical expression
        [Basis,]         ! (optional) numerical expression
        [LowerBound,]    ! (optional) numerical expression
        [UpperBound,]    ! (optional) numerical expression
        [Error]          ! (optional) numerical expression
        )

Arguments
---------

    *SettlementDate*
        The date of settlement of the security. *SettlementDate* must be in date
        format.

    *MaturityDate*
        The date of maturity of the security. *MaturityDate* must also be in
        date format and must be a date after *SettlementDate*.

    *ParValue*
        The starting value of the security at issue date. *ParValue* must be a
        positive real number.

    *Price*
        The price of the security at settlement date. *Price* must be a positive
        real number.

    *Redemption*
        The amount repaid for the security at the maturity date. *Redemption*
        must be a positive real number.

    *Frequency*
        The number of coupon payments in one year. *Frequency* must be 1
        (annual), 2 (semi-annual) or 4 (quarterly).

    *CouponRate*
        The annual interest rate of the security as a percentage of the par
        value. *CouponRate* must be a nonnegative real number.

    *Basis*
        The day-count basis method to be used. The default is 1.

    *LowerBound*
        Indicates a minimum for the yield to be accepted by this function. The
        default is :math:`-1`.

    *UpperBound*
        Indicates a maximum for the yield to be accepted by this function. The
        default is :math:`5`.

    *Error*
        Indicates whether AIMMS should give an error if multiple solutions are
        found that satisfy the bounds. :math:`Error = 0`: if multiple solutions
        are found, return the solution with the smallest absolute value.
        :math:`Error = 1`: if multiple solutions are found, return an error
        message. The default is :math:`0`.

Return Value
------------

    The function :aimms:func:`SecurityPeriodicYield` returns the yield of a security
    that pays interest at the end of each coupon period.

.. note::

    -  This function can be used in an objective function or constraint and
       the input parameters *ParValue*, *Price*, *Redemption*, and
       *CouponRate* can be used as a variable.

    -  The function :aimms:func:`SecurityPeriodicYield` is similar to the Excel
       function `YIELD <https://support.microsoft.com/en-us/office/yield-function-f5f5ca43-c4bd-434f-8bd2-ed3c9727a4fe>`_.

Example
-------

The code:

.. code-block:: aimms

    _p_spy := SecurityPeriodicYield(
        SettlementDate :  "2024-01-01",
        MaturityDate   :  "2025-01-01",
        ParValue       :  100,
        Price          :  95,
        Redemption     :  100,
        Frequency      :  4,
        CouponRate     :  0.06,
        Basis          :  1,
        LowerBound     :  -1,
        UpperBound     :  5,
        Error          :  0);
    block where single_column_display := 1, listing_number_precision := 6 ;
        display _p_spy ;
    endblock ;

Produces:

.. code-block:: aimms

    _p_spy := 0.113600 ;

.. seealso::

    *   Day count basis :ref:`methods<ff.dcb>`. 
    *   General :ref:`equations<ff.sec.coupn>` for securities with multiple coupons.
