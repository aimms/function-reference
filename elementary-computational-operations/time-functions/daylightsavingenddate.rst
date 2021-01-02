.. aimms:function:: DaylightSavingEndDate(Year, Timezone)

.. _DaylightSavingEndDate:

DaylightSavingEndDate
=====================

The function :aimms:func:`DaylightSavingEndDate` computes the end date of daylight
saving time for a particular year in a particular time zone.

.. code-block:: aimms

    DaylightSavingEndDate(
         Year,                    ! (input) an element expression
         Timezone                 ! (input) an element expression
         )

Arguments
---------

    *Year*
        An element of a yearly calendar for the end date of daylight saving time
        must be computed.

    *Timezone*
        An element in the predefined set :aimms:set:`AllTimeZones`.

Return Value
------------

    The result of :aimms:func:`DaylightSavingEndDate` is the end date of daylight
    saving time, as a reference date, for the time zone *Timezone* in the
    year *Year*.

.. seealso::

    AIMMS support for time zones is discussed in full detail in :ref:`sec:time.format.dst` 
    and :doc:`advanced-language-components/time-based-modeling/working-in-multiple-time-zones` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
