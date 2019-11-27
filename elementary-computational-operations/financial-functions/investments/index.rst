.. _chap:finance-investments:

.. _FF.inv:

Investments
===========

Investments and Loans
^^^^^^^^^^^^^^^^^^^^^

When dealing with investments or loans, several cash flows are scheduled
within a certain time frame, such as the

-  present value (the value at the beginning of the scheduled time
   frame),

-  future value (the value at the end of the scheduled time frame), and

-  periodic payments during the scheduled time frame.

AIMMS provides several functions to calculate each of these cash flows
(or the interest rate used) in the presence of all others.

Constant Payments
^^^^^^^^^^^^^^^^^

Investments and loans with constant, periodic payments and a constant
interest rate are special. When the payments are annual, such an
investment is called an annuity. The constant payments of these
investments consist of a principal and an interest payment. The
principal payment will generally increase in time whereas the interest
payment will decrease in time. Two different types of investments with
constant payments and interest rates can be distinguished:

-  The first type, also referred as type 0, has payments that are made
   at the end of each period.

-  The second type, type 1, has payments that are made at the beginning
   of each period. This type has no interest payment at the beginning of
   the first period, but does have an extra period, after the last
   periodic payment, with an interest payment over the last period and
   an inverse principal payment.

.. _FF.inveq:

Equations
^^^^^^^^^

Cash flows can be either positive or negative, where a positive payment
indicates that you are receiving this payment. Taking the interest into
account, the total value of an investment must be equal to zero after
all cash flows have occurred. For example, a positive present value and
positive payments will lead to a negative future value: your debt has
grown. The following equation expresses the relation between all the
cash flows that take place

.. math:: v_p(1+r)^N + p\sum_{i=1}^N (1+r)^{i-1+T} + v_f = 0

where :math:`v_p` is the present value, :math:`v_f` is the future value,
:math:`p` is the constant periodic payment, :math:`r` is the constant
interest rate and :math:`T` is the investment type as discussed above.

AIMMS supports the following investment functions with constant,
periodic payments:

-  :aimms:func:`InvestmentConstantPresentValue`
-  :aimms:func:`InvestmentConstantFutureValue`
-  :aimms:func:`InvestmentConstantPeriodicPayment`
-  :aimms:func:`InvestmentConstantInterestPayment`
-  :aimms:func:`InvestmentConstantPrincipalPayment`
-  :aimms:func:`InvestmentConstantCumulativeInterestPayment`
-  :aimms:func:`InvestmentConstantCumulativePrincipalPayment`
-  :aimms:func:`InvestmentConstantNumberPeriods`
-  :aimms:func:`InvestmentConstantRateAll`
-  :aimms:func:`InvestmentConstantRate`

Variable Payments
^^^^^^^^^^^^^^^^^

When the cash flows are variable (i.e. not constant), take place at
irregular intervals, or when the interest rate varies over time, it
still possible to compute present values, future values, and the
internal rate of return, i.e. the rate received for an investment
consisting of payments and income.

AIMMS supports the following investment functions for variable cash
flows:

-  :aimms:func:`InvestmentVariablePresentValue`
-  :aimms:func:`InvestmentVariablePresentValueInPeriodic`
-  :aimms:func:`InvestmentSingleFutureValue`
-  :aimms:func:`InvestmentVariableInternalRateReturnAll`
-  :aimms:func:`InvestmentVariableInternalRateReturn`
-  :aimms:func:`InvestmentVariableInternalRateReturnInPeriodicAll`
-  :aimms:func:`InvestmentVariableInternalRateReturnInPeriodic`
-  :aimms:func:`InvestmentVariableInternalRateReturnModified`

.. toctree::
   :hidden:

   investmentconstantfuturevalue
   investmentconstantperiodicpayment
   investmentconstantpresentvalue
   investmentconstantinterestpayment
   investmentconstantprincipalpayment
   investmentconstantcumulativeinterestpayment
   investmentconstantcumulativeprincipalpayment
   investmentconstantnumberperiods
   investmentconstantrate
   investmentconstantrateall
   investmentvariablepresentvalue
   investmentvariablepresentvalueinperiodic
   investmentsinglefuturevalue
   investmentvariableinternalratereturn
   investmentvariableinternalratereturnall
   investmentvariableinternalratereturninperiodic
   investmentvariableinternalratereturninperiodicall
   investmentvariableinternalratereturnmodified
