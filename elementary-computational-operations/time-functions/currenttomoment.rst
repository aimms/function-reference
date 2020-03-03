.. aimms:function:: CurrentToMoment(Unit, ReferenceDate)

.. _CurrentToMoment:

CurrentToMoment
===============

The function :aimms:func:`CurrentToMoment` converts the current time to the
elapsed time with respect to a specific reference date.

.. code-block:: aimms

    CurrentToMoment(
         Unit,                    ! (input) a time unit
         ReferenceDate            ! (input) a string expression
         )

Arguments
---------

    *Unit*
        The time unit that is used to return the elapsed time.

    *ReferenceDate*
        A string that holds the begin date using the fixed format for date and
        time, see paragraph *Reference date format* on page 544 of the Language
        Reference.

Return Value
------------

    The result of :aimms:func:`CurrentToMoment` is the elapsed time in *Unit* since
    *ReferenceDate*.

.. seealso::

    -  The function :aimms:func:`StringToMoment`.

    -  :any:`Articles/144/144-Stopwatch`
       illustrates the use of some time functions. The purpose of
       :aimms:func:`CurrentToMoment` in that post is to compute the time since a
       starting point.
