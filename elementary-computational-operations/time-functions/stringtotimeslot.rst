.. aimms:function:: StringToTimeSlot(Format, Calendar, MomentString)

.. _StringToTimeSlot:

StringToTimeSlot
================

The function :aimms:func:`StringToTimeSlot` determines the time slot in a calendar
that corresponds with the a moment that is specified using a free format
string.

.. code-block:: aimms

    StringToTimeSlot(
         Format,         ! (input) a string expression
         Calendar,       ! (input) a calendar
         MomentString    ! (input) a string expression
         )

Arguments
---------

    *Format*
        A string that holds the date and time format used in the third argument
        *MomentString*. Valid format strings are described in :doc:`advanced-language-components/time-based-modeling/format-of-time-slots-and-periods`

    *Calendar*
        An identifier of type calendar.

    *MomentString*
        A string expression of the moment (using the format given in ``Format``)
        that should be matched with the time slots in the calendar.

Return Value
------------

    The function :aimms:func:`StringToTimeSlot` returns the time slot in the calendar
    that contains the given moment.

.. seealso::

    The functions :aimms:func:`CurrentToTimeSlot`, :aimms:func:`MomentToTimeSlot`.
