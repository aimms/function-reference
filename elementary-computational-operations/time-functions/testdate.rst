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
        string. Valid format strings are described in Section 33.7.

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

        ok := TestDate( "\%c\%y-\%m-\%d", "2015-xx-xx" ); ! ok becomes 0; Not numeric.
        ok := TestDate( "\%c\%y-\%m-\%d", "2015-02-29" ); ! ok becomes 0; Feb 2015 has only 28 days.
        ok := TestDate( "\%c\%y-\%m-\%d", "2016-02-29" ); ! ok becomes 1; Feb 29, 2016 exists.
        ok := TestDate( "\%c\%y-\%m-\%d", "2015-04-31" ); ! ok becomes 0; April 31 does not exist.
        ok := TestDate( "\%c\%y-\%m-\%d", "2015-04-01" ); ! ok becomes 1; April 01 does exist (-;
        ok := TestDate( "\%m-\%d", "03-03", requireUnique:1 ); ! Not unique, ok becomes 0.
        ok := TestDate( "\%m-\%d", "03-03", requireUnique:0 ); ! Uniqueness not required; ok becomes 1.

.. seealso::

    The function :aimms:func:`CurrentToString`.
