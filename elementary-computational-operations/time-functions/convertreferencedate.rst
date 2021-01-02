.. aimms:function:: ConvertReferenceDate(ReferenceDate, FromTimezone, ToTimezone, IgnoreDST)

.. _ConvertReferenceDate:

ConvertReferenceDate
====================

The function :aimms:func:`ConvertReferenceDate` converts a reference date from one
timezone to the other.

.. code-block:: aimms

    ConvertReferenceDate(
         ReferenceDate,          ! (input) a string expression
         FromTimezone,           ! (input) an element expression
         ToTimezone,             ! (input) an element expression
         IgnoreDST               ! (optional) a numerical expression (default 0)
         )

Arguments
---------

    *ReferenceDate*
        A string that holds a reference date in *FromTimezone*.

    *FromTimezone*
        An element of :aimms:set:`AllTimeZones` with respect to which *ReferenceDate* is
        expressed.

    *ToTimezone*
        An element of :aimms:set:`AllTimeZones` with respect to which the resulting reference
        date must be expressed.

    *IgnoreDST*
        A numerical expression indicating whether daylight saving time must be
        ignored in the conversion.

Return Value
------------

    The result of :aimms:func:`ConvertReferenceDate` is a reference date in
    *ToTimezone* corresponding to the reference date *ReferenceDate* in
    *FromTimezone*.

.. seealso::

    AIMMS support for time zones is discussed in full detail in :ref:`sec:time.format.dst` 
    and :doc:`advanced-language-components/time-based-modeling/working-in-multiple-time-zones` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
