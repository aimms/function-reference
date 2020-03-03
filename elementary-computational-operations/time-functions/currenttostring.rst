.. aimms:function:: CurrentToString(Format)

.. _CurrentToString:

CurrentToString
===============

The function :aimms:func:`CurrentToString` creates a string representation of the
current time in the a specified format.

.. code-block:: aimms

    CurrentToString(
         Format           ! (input) a string expression
         )

Arguments
---------

    *Format*
        A string that holds the date and time format used in the returned
        string. Valid format strings are described in Section 33.7.

Return Value
------------

    The result of :aimms:func:`CurrentToString` is a description of the current time
    according to *Format*.

.. note::

    There is an option ``Current_Time_in_LocalDST`` that specifies whether
    this function takes into account the effects of daylight savings time.

.. seealso::

    -  The functions :aimms:func:`MomentToString`, :aimms:func:`CurrentToMoment`.

    -  :any:`Articles/144/144-Stopwatch`
       illustrates the use of some time functions. The purpose of
       :aimms:func:`CurrentToString` in that post is to mark the starting point.
