.. aimms:function:: MomentToString(Format, unit, ReferenceDate, Elapsed)

.. _MomentToString:

MomentToString
==============

The function :aimms:func:`MomentToString` creates a string representation of a
moment, that is calculated from a given amount of elapsed time since a
specific reference date.

.. code-block:: aimms

    MomentToString(
         Format,                 ! (input) a string expression
         unit,                   ! (input) a time unit
         ReferenceDate,          ! (input) a string expression
         Elapsed                 ! (input) a numerical expression
         )

Arguments
---------

    *Format*
        A string that holds the date and time format used in the returned
        string. Valid format strings are described in Section 33.7.

    *unit*
        The time unit that is used in the argument *Elapsed*.

    *ReferenceDate*
        A string that holds the begin date using the fixed format for date and
        time, see paragraph *Reference date format* on page 544 of the Language
        Reference.

    *Elapsed*
        A numerical value of the time elapsed since *ReferenceDate*.

Return Value
------------

    The result of :aimms:func:`MomentToString` is a string describing the
    corresponding moment according to *Format*.

.. seealso::

    The function :aimms:func:`StringToMoment`.
