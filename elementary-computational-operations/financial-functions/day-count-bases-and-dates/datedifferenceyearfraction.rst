.. aimms:function:: DateDifferenceYearFraction(FirstDate, SecondDate, Basis)

.. _DateDifferenceYearFraction:

DateDifferenceYearFraction
==========================

The function :aimms:func:`DateDifferenceYearFraction` calculates the year fraction
between two dates based on the specified day count basis.

.. code-block:: aimms

    DateDifferenceYearFraction(
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

    The function :aimms:func:`DateDifferenceYearFraction` returns the difference
    between *FirstDate* and *SecondDate* in fractions of a year.

.. note::

    The function :aimms:func:`DateDifferenceYearFraction` is similar to the Excel
    function ``YEARFRAC``.

.. seealso::

    Day count basis :ref:`methods<ff.dcb>`.
