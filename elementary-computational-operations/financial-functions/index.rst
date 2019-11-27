.. _chap:finance-intro:

Financial Functions
-------------------

Financial functions can be of great use in modeling financial
optimization models. They perform common business calculations, such as
determining

-  the depreciation of an asset,
-  the payments for a loan,
-  the future value or net present value of an investment, and
-  the values of bonds, coupons or other securities.

Having these functions available in AIMMS prevents you from having to
implement such functionality into your models yourself. Common arguments
for the financial functions include:

Values
   the value of an investment, security or cash flow at a specific time.
   For example, the amount paid periodically to an investment or loan.

Rates
   the interest rate or discount rate for an investment or security. For
   example, the desired internal return on investment could be 8
   percent.

Dates
   the date of measurements, payments or other events. For example, the
   date of settlement of a security. AIMMS's financial functions always
   expect dates to be provided in the format ``"ccyy-mm-dd"``.

Interval lengths (in time periods)
   the number of periods that has to be analyzed. For example, the
   useful life of an asset or the number of payments or periods of an
   investment

Type
   the time when payments are made during the period. For example, at
   the beginning of a month or the end of the month.

The financial functions supported by AIMMS can be divided into separate
categories. Each of these categories will be shortly introduced
(including the mathematical equations underlying the functions in a
category) and each of the available functions will be described in full
detail. The following categories can be distinguished:

.. toctree::
   :maxdepth: 1

   general-conversions/index
   day-count-bases-and-dates/index
   depreciations/index
   investments/index
   securities/index
