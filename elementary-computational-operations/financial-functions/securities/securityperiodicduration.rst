.. aimms:function:: SecurityPeriodicDuration(SettlementDate, MaturityDate, ParValue, Redemption, Frequency, CouponRate, Yield, Basis)

.. _SecurityPeriodicDuration:

SecurityPeriodicDuration
========================

The function :aimms:func:`SecurityPeriodicDuration` returns the Macauley duration
of a security that pays interest at the end of each coupon period.
Duration is defined as the weighted average of time it takes to receive
a positive cash flow. The present values of the cash flows are used as
weights. The duration can be used as a measure of a bond price's
response to changes in yield.

.. code-block:: aimms

    SecurityPeriodicDuration(
        SettlementDate,           ! (input) scalar string expression
        MaturityDate,             ! (input) scalar string expression
        ParValue,                 ! (input) numerical expression
        Redemption,               ! (input) numerical expression
        Frequency,                ! (input) numerical expression
        CouponRate,               ! (input) numerical expression
        Yield,                    ! (input) numerical expression
        [Basis]                   ! (optional) numerical expression
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

    *Basis*
        The day-count basis method to be used. The default is 1.

Return Value
------------

    The function :aimms:func:`SecurityPeriodicDuration` returns the Macauley duration
    of a security that pays interest at the end of each coupon period.
    Duration is defined as the weighted average of the time it takes to
    receive a positive cash flow.

Equation
--------

    The Macauley duration :math:`D` is computed through the equation

    .. math:: D = \frac{ \displaystyle \left(N-1+ \frac{f_{SN}}{f_{PN}}\right) \frac{R}{\left(1 + \frac{r_y}{f}\right)^{N-1+\frac{f_{SN}}{f_{PN}}}} + \sum_{i=1}^N \left(i-1+ \frac{f_{SN}}{f_{PN}}\right) \frac{v_{\textit{par}}\frac{r_c}{f}}{\left(1 + \frac{r_y}{f}\right)^{i-1+\frac{f_{SN}}{f_{PN}}}} } { \displaystyle \frac{R}{\left(1 + \frac{r_y}{f}\right)^{N-1+\frac{f_{SN}}{f_{PN}}}} + \sum_{i=1}^N \frac{v_{\textit{par}}\frac{r_c}{f}}{\left(1 + \frac{r_y}{f}\right)^{i-1+\frac{f_{SN}}{f_{PN}}}} }

    \ where all other variables have the same interpretation as in the
    general :ref:`equations<ff.sec.coupn>` for securities with multiple coupons.

.. note::

    -  This function can be used in an objective function or constraint and
       the input parameters *ParValue*, *Redemption*, *CouponRate*, and
       *Yield* can be used as a variable.

    -  The function :aimms:func:`SecurityPeriodicDuration` is similar to the Excel
       function ``DURATION``.

.. seealso::

    Day count basis :ref:`methods<ff.dcb>`. General :ref:`equations<ff.sec.coupn>` for securities with multiple coupons.
