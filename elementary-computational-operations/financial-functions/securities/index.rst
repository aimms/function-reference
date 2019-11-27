.. _chap:finance-securities:

.. _FF.sec:

Securities
==========

There are several types of securities, each with its own features and
scheduled cash flows. Cash flows can be scheduled at the end of every
coupon period or just at the end of the security’s life. If we see a
security as an investment, its yield can be viewed as the internal rate
of return. The cash flows of a security can consists of periodic
payments (equal to a certain percentage of the par value), the coupons,
and the future value of the security. In general, the general cash flow
equation

.. math:: v_p(1+r)^N + p\sum_{i=1}^N (1+r)^{i-1} + v_f = 0

where :math:`v_p` is the present value, :math:`v_f` is the future value,
:math:`N` the number of periods, :math:`p` is a constant periodic
payment and :math:`r` is the constant interest rate, holds. AIMMS
provides functions the most common types of securities like treasury
bills and bonds. However, the present value, future value, periodic
payments, number of periods and interest rate are different for each
specify security type.

Security Types
^^^^^^^^^^^^^^

We distinguish three main types of securities:

-  securities with zero coupon periods (discounted securities),
-  securities with one coupon period (at maturity), and
-  securities with multiple coupon periods

.. _ff.sec.disc:

Discounted Securities
^^^^^^^^^^^^^^^^^^^^^

In the case of discounted (or zero coupon) securities such as treasury
bills, there are no periodical payments. The only positive cash flow is
a fixed redemption at the end of the security’s life. Therefore, only
the value of this redemption and the investment made for the security
determine its yield. In this case, the present value is equal to the
price :math:`-P`, the price at which the security is bought at the
settlement date, there 0 periods (so no periodic payments), and the
future value at the maturity date is equal to the redemption :math:`R`.
Thus the general cash flow equation reduces to

.. math:: -P(1+r_yf_{SM}) + R = 0

where :math:`r_y` is the annual yield of the security, and
:math:`f_{SM}` is the difference (in fractions of years) between the
settlement and maturity date, computed with respect to the specified day
count basis :ref:`method<ff.dcb>`.

Discount Rate
^^^^^^^^^^^^^

Commonly with discounted securities, the yield is not expressed in terms
of the price, but in terms of the fixed redemption. The discount rate is
the increase in value per year as a percentage of the redemption. The
relationship between the yield :math:`r_y` and the discount rate
:math:`r_d` is given by

.. math:: 1 + r_yf_{SM} = \frac{1}{1-r_df_{SM}}

which leads to the following equivalent relation between price and
redemption

.. math:: -P + R(1-r_df_{SM}) = 0

Treasury Bills
^^^^^^^^^^^^^^

A treasury bill is a discounted security with less than one year from
settlement until maturity, the number of days in one year is fixed at
360 and redemption is fixed at 100.

Functions for Discounted Securities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

AIMMS supports the following functions for securities with zero coupon
periods:

-  :aimms:func:`SecurityDiscountedPrice`
-  :aimms:func:`SecurityDiscountedRedemption`
-  :aimms:func:`SecurityDiscountedYield`
-  :aimms:func:`SecurityDiscountedRate`
-  :aimms:func:`TreasuryBillPrice`
-  :aimms:func:`TreasuryBillYield`
-  :aimms:func:`TreasuryBillBondEquivalent`

.. _ff.sec.coup1:

One-Coupon Securities
^^^^^^^^^^^^^^^^^^^^^

Securities that only pay interest at maturity can be seen as securities
with only one coupon period, where the accrued interest increases
linearly in time until it is paid (when the security expires), and the
redemption equals the par value of the security. In the general cash
flow equation,

-  the present value

   .. math:: v_p=-P - v_{\textit{par}}r_cf_{IS},

   \ where :math:`P` is the price of the account at settlement and
   :math:`f_{IS}` is the difference between the issue and settlement
   date (in fraction of years) with respect to the specified day count
   basis :ref:`method<ff.dcb>`, to account for the accrued interest from the issue
   date until settlement,

-  the periodic payment

   .. math:: p =v_{\textit{par}}r_yf_{IM},

   \ where :math:`r_y` is the annual yield and :math:`f_{IM}` is the
   difference between the issue and maturity date (in fraction of years)
   with respect to the specified day count basis :ref:`method<ff.dcb>`, and

-  the interest rate

   .. math:: r=r_yf_{SM},

   \ where :math:`f_{SM}` is the difference between the settlement and
   maturity date (in fraction of years) with respect to the specified
   day count basis :ref:`method<ff.dcb>`.

This results in the following equation for securities with one coupon
period:

.. math:: (-P - v_{\textit{par}}r_cf_{IS})(1+r_yf_{SM}) + v_{\textit{par}}r_yf_{IM} + v_{\textit{par}} = 0

Functions for One-Coupon Securities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

AIMMS supports the following functions for securities with one coupon
period:

-  :aimms:func:`SecurityMaturityPrice`
-  :aimms:func:`SecurityMaturityCouponRate`
-  :aimms:func:`SecurityMaturityYield`
-  :aimms:func:`SecurityMaturityAccruedInterest`

.. _ff.sec.coupn:

Multi-Coupon Securities
^^^^^^^^^^^^^^^^^^^^^^^

For securities with multiple coupon periods, interest will be accrued
linearly during and paid at the end of each coupon period (i.e. at the
coupon date). In the general cash flow equation

-  the number of periods

   .. math:: N=\lceil ff_{SM}\rceil,

   \ where :math:`f` is the coupon frequency (number of coupon periods
   per year), and :math:`f_{SM}` the difference between settlement and
   maturity date (in fraction of years) with respect to the specified
   day count basis :ref:`method<ff.dcb>`,

-  the present value

   .. math:: v_p = -P -v_{\textit{par}}\frac{r_c}{f}\frac{f_{PS}}{f_{PN}},

   \ where :math:`P` is the price of the security at settlement,
   :math:`v_{\textit{par}}` the par value of the security, :math:`r_c`
   the annual coupon rate, :math:`f_{PS}` the difference (in fraction of
   years) between the previous coupon and settlement date, and
   :math:`f_{PN}` the difference between the previous and next coupon
   date, both with respect to the specified day count basis :ref:`method<ff.dcb>`,

-  the periodic payment

   .. math:: p=v_{\textit{par}}\frac{r_c}{f}

-  the interest rate

   .. math:: r=\frac{r_y}{f},

   \ where :math:`r_y` is the annual yield.

This results in the following equation for securities with multiple
coupon periods:

.. math::

   \left(-P -v_{\textit{par}}\frac{r_c}{f}\frac{f_{PS}}{f_{PN}}\right)^{N-1+\frac{f_{SN}}{f_{PN}}} +
       \sum_{i=1}^{N}v_{\textit{par}}\frac{r_c}{f}\left(1+\frac{r_y}{f}\right)^{N-i} + R = 0

Functions for Multi-Coupon Securities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

AIMMS supports the following functions for securities with multiple
coupon periods:

-  :aimms:func:`SecurityCouponNumber`
-  :aimms:func:`SecurityCouponPreviousDate`
-  :aimms:func:`SecurityCouponNextDate`
-  :aimms:func:`SecurityCouponDays`
-  :aimms:func:`SecurityCouponDaysPreSettlement`
-  :aimms:func:`SecurityCouponDaysPostSettlement`
-  :aimms:func:`SecurityPeriodicPrice`
-  :aimms:func:`SecurityPeriodicRedemption`
-  :aimms:func:`SecurityPeriodicCouponRate`
-  :aimms:func:`SecurityPeriodicYieldAll`
-  :aimms:func:`SecurityPeriodicYield`
-  :aimms:func:`SecurityPeriodicAccruedInterest`
-  :aimms:func:`SecurityPeriodicDuration`
-  :aimms:func:`SecurityPeriodicDurationModified`

.. toctree::
   :hidden:

   securitydiscountedprice
   securitydiscountedredemption
   securitydiscountedyield
   securitydiscountedrate
   treasurybillprice
   securitymaturityprice
   treasurybillbondequivalent
   treasurybillyield
   securitymaturitycouponrate
   securitymaturityyield
   securitycouponnumber
   securitycouponpreviousdate
   securitymaturityaccruedinterest
   securitycoupondays
   securitycouponnextdate
   securitycoupondayspostsettlement
   securitycoupondayspresettlement
   securityperiodicprice
   securityperiodiccouponrate
   securityperiodicredemption
   securityperiodicaccruedinterest
   securityperiodicyield
   securityperiodicyieldall
   securityperiodicduration
   securityperiodicdurationmodified
