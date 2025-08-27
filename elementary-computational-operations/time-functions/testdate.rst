.. aimms:function:: TestDate(Format, Date, requireUnique)

.. _TestDate:

TestDate
========

The function :aimms:func:`TestDate` tests whether or not a particular date is
according to given format.

.. code-block:: aimms

    TestDate(
         Format,        ! (input) a string expression
         Date,          ! (input) a string expression
         requireUnique  ! (optional) default 1.
         )

Arguments
---------

    *Format*
        A string that holds the date and time format used in the returned
        string. Valid format strings are described in :doc:`advanced-language-components/time-based-modeling/format-of-time-slots-and-periods`.

    *Date*
        It is tested whether or not this string is according to format *Format*.

    *requireUnique*
        When 1, it requires the year number to be present in the date.

Return Value
------------

    The result of :aimms:func:`TestDate` is 1 if *Date* is according to format
    *Format* and an existing data, and 0 otherwise. If the result is 0, the
    pre-defined identifier :aimms:set:`CurrentErrorMessage` will contain a proper error message.

Example
-------

.. code-block:: aimms

	_bp_ok1 := TestDate( "%c%y-%m-%d", "2015-xx-xx" ); ! ok becomes 0; Not numeric.
	_bp_ok2 := TestDate( "%c%y-%m-%d", "2015-02-29" ); ! ok becomes 0; Feb 2015 has only 28 days.
	_bp_ok3 := TestDate( "%c%y-%m-%d", "2016-02-29" ); ! ok becomes 1; Feb 29, 2016 exists.
	_bp_ok4 := TestDate( "%c%y-%m-%d", "2015-04-31" ); ! ok becomes 0; April 31 does not exist.
	_bp_ok5 := TestDate( "%c%y-%m-%d", "2015-04-01" ); ! ok becomes 1; April 01 does exist (-;
	_bp_ok6 := TestDate( "%m-%d", "03-03", requireUnique:1 ); ! Not unique, ok becomes 0.
	_bp_ok7 := TestDate( "%m-%d", "03-03", requireUnique:0 ); ! Uniqueness not required; ok becomes 1.
	_bp_ok8 := TestDate( "%Aw|AllAbbrWeekdays| %Am|AllAbbrMonths| %d, %c%y", "Mon Jul 22, 2024" ); ! ok becomes 1; Jul 24, 2024 is a Monday.
	_bp_ok9 := TestDate( "%Aw|AllAbbrWeekdays| %Am|AllAbbrMonths| %d, %c%y", "Tue Jul 22, 2024" ); ! ok becomes 0; Jul 24, 2024 is not a Tuesday.

.. seealso::

    - The function :aimms:func:`CurrentToString`.
