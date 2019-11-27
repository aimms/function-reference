.. aimms:function:: SecurityPeriodicYieldAll(SettlementDate, MaturityDate, ParValue, Price, Redemption, Frequency, CouponRate, Yield, Yield, NumberSolutions, Basis, Mode)

.. _SecurityPeriodicYieldAll:

SecurityPeriodicYieldAll
========================

The procedure :aimms:func:`SecurityPeriodicYieldAll` returns the yield(s) of a
security that pays interest at the end of each coupon period.

.. code-block:: aimms

    SecurityPeriodicYieldAll(
        SettlementDate,           ! (input) scalar string expression
        MaturityDate,             ! (input) scalar string expression
        ParValue,                 ! (input) numerical expression
        Price,                    ! (input) numerical expression
        Redemption,               ! (input) numerical expression
        Frequency,                ! (input) numerical expression
        CouponRate,               ! (input) numerical expression
        Yield,                    ! (output) one-dimensional numerical expression
        NumberSolutions,          ! (output) numerical expression
        [Basis,]                  ! (optional) numerical expression
        [Mode]                    ! (optional) numerical expression
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

    *Yield*
        The yield of the security. *Yield* must be a nonnegative real number.

    *Yield*
        There is not always a unique solution for yield. Dependent on *Mode* one
        solution or all the solutions will be given.

    *NumberSolutions*
        The number of solutions found. If :math:`Mode = 0` *NumberSolutions*
        will always be :math:`1`.

    *Basis*
        The day-count basis method to be used. The default is 1.

    *Mode*
        Indicates whether all the solutions need to be found or just one.
        :math:`Mode = 0`: the search for solutions stops after one solution is
        found. :math:`Mode = 1`: the search for solutions continues till all
        solutions are found.

.. note::

    -  When you want to use this procedure in an objective function or
       constraint you have to use ``SecurityPeriodicYield``.

    -  The function :aimms:func:`SecurityPeriodicYieldAll` is similar to the Excel
       function ``YIELD``.

.. seealso::

    Day count basis :ref:`methods<ff.dcb>`. General :ref:`equations<ff.sec.coupn>` for securities with multiple coupons.
