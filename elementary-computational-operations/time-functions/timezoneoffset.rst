.. aimms:function:: TimeZoneOffSet(FromTZ, ToTZ[, UseDST])

.. _TimeZoneOffSet:

TimeZoneOffSet
==============

The function :aimms:func:`TimeZoneOffSet` computes, in minutes, the offset between
two time zones.

.. code-block:: aimms

    TimeZoneOffSet(
         FromTZ,     ! (input) an element expression
         ToTZ        ! (input) an element expression
         [UseDST]    ! (optional) 0 or 1
         )

Arguments
---------

    *FromTZ*
        An element from the set ``AllTimeZones``.

    *ToTZ*
        An element from the set ``AllTimeZones``.

    *UseDST (optional)*
        A scalar expression specifying whether or not the current setting for
        daylight saving time (DST) in both time zones should be taken into
        account. The default is 0, indicating DST is not used.

Return Value
------------

    The result of :aimms:func:`TimeZoneOffSet` is the offset, in minutes, between
    *FromTZ* and *ToTZ*.

.. note::

    The result of the function has an associated unit, namely minutes. If
    *FromTZ* is UTC, the offset of *ToTZ* is the usual offset with respect
    to UTC (or GMT).

.. seealso::

    AIMMS support for time zones is discussed in full detail in :ref:`sec:time.format.dst` 
    and :doc:`advanced-language-components/time-based-modeling/working-in-multiple-time-zones` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
