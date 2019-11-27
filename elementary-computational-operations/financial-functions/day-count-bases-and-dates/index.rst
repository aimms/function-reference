.. _chap:finance-datedifference:

Day Count Bases and Dates
=========================

.. _FF.date:

Many financial functions require date arguments, and depend on
differences between two dates, either as a number of days or as a
fraction of a year. This chapter discusses the date format expected by
AIMMS’s financial functions and the different methods to compute date
differences used from which you can choose in many functions.

Format of Date Arguments
------------------------

All date arguments in AIMMS’s financial functions should be provided in
the fixed string date format ``"ccyy-mm-dd"``. So, 15 August, 2000
should be passed to a financial function as the string ``"2000-08-15"``.
If you want to pass an element from a daily calendar as a date argument,
you should convert it to the fixed string date format using the function :aimms:func:`TimeSlotToString`

.. _ff.dcb:

Day Count Bases
---------------

The result of many financial functions depends on the way with which
differences between two dates are dealt with. Such functions have a *day
count basis* argument, which determines how the difference between two
dates is calculated, either in days or as a fraction of a year. AIMMS
supports 5 different day count basis methods, each of which is commonly
used in the financial markets. Each of these methods is specified by a
way to count days and a way to determine how many days are in a year.

Method 1 - NASD Method / 360 Days
   Calculating with day count basis method 1 means that a year is
   assumed to consist of 12 periods of 30 days. A year consists of 360
   days. The difference between this method and method 5 is the way the
   last day of a month is handled.

Method 2 - Actual / Actual
   Calculating with day count basis method 2 means that both the number
   of days between two dates and the number of dates in a year are
   actual.

Method 3 - Actual / 360 Days
   Calculating with day count basis method 3 means that the number of
   days between two dates is actual and that the number of days in a
   year is 360. When using this method, you should note that the year
   fraction of two dates that are one year apart is larger than 1
   (365/360) and that this may lead to unwanted results.

Method 4 - Actual / 365 Days
   Calculating with day count basis method 4 means that the number of
   days between two dates is actual and that the number of days in a
   year is 365.

Method 5 - European Method / 360 Days
   Calculating with day count basis method 5 means that a year is
   assumed to consist of 12 periods of 30 days. A year consists of 360
   days. The difference between this method and method 1 is the way the
   last day of a month is handled.

When the day count basis argument is optional, AIMMS assumes the NASD
method 1 by default.

Date Differences
----------------

AIMMS supports the following functions for computing differences between
two dates:

-  :aimms:func:`DateDifferenceDays`
-  :aimms:func:`DateDifferenceYearFraction`

.. toctree::
   :hidden:

   datedifferencedays
   datedifferenceyearfraction
