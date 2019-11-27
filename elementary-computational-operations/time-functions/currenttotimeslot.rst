.. aimms:function:: CurrentToTimeSlot(Calendar)

.. _CurrentToTimeSlot:

CurrentToTimeSlot
=================

The function :aimms:func:`CurrentToTimeSlot` determines the time slot in a
calendar that corresponds with the current time.

.. code-block:: aimms

    CurrentToTimeSlot(
         Calendar           ! (input) a calendar
         )

Arguments
---------

    *Calendar*
        An identifier of type calendar.

Return Value
------------

    The function :aimms:func:`CurrentToTimeSlot` returns the time slot in the calendar
    that contains the current moment.

.. note::

    There is an option ``Current_Time_in_LocalDST`` that specifies whether
    this function takes into account the effects of daylight savings time.

.. seealso::

    The functions :aimms:func:`StringToTimeSlot`, :aimms:func:`MomentToTimeSlot`.
