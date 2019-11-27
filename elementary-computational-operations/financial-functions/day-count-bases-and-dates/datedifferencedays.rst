.. aimms:function:: DateDifferenceDays(FirstDate, SecondDate, Basis)

.. _DateDifferenceDays:

DateDifferenceDays
==================

The function :aimms:func:`DateDifferenceDays` calculates the number of days
between two dates based on the specified day count basis.

.. code-block:: aimms

    DateDifferenceDays(
        FirstDate,             ! (input) scalar string expression
        SecondDate,            ! (input) scalar string expression
        [Basis]                ! (optional) numerical expression
        )

Arguments
---------

    *FirstDate*
        The first date must be in date format.

    *SecondDate*
        The second date must be in date format, and later than *FirstDate*.

    *Basis*
        The day-count basis method to be used. The default is 1.

Return Value
------------

    The function :aimms:func:`DateDifferenceDays` returns the number of days between
    the two dates.

.. note::

    The function :aimms:func:`DateDifferenceDays` is similar to the Excel function
    ``DAYS300``.

.. seealso::

    Day count basis :ref:`methods<ff.dcb>`.
