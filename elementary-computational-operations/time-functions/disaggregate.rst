.. aimms:procedure:: DisAggregate(PeriodData, TimeslotData, Timetable, Type[, Locus])

.. _DisAggregate:

DisAggregate
============

With the procedure :aimms:procedure:`DisAggregate` you can disaggregate time-dependent
data from a horizon time scale (periods) to a calendar time scale (time
slots).

.. code-block:: aimms

    DisAggregate(
         PeriodData,         ! (input) an indexed identifier over a horizon
         TimeslotData,       ! (output) an indexed identifier over a calendar
         Timetable,          ! (input) an AIMMS time table
         Type,               ! (input) an element in the set AggregationTypes
         [Locus]             ! (optional) a value between 0 and 1
         )

Arguments
---------

    *PeriodData*
        An identifier (slice) containing the data to be disaggregated. The
        domain sets in the index domain of this identifier should at least
        contain a horizon set, and all other sets should coincide with the
        domain of *TimeslotData*.

    *TimeslotData*
        An identifier (slice) that on returns will contain the disaggregated
        data. The domain sets in the index domain of this identifier should at
        least contain a calendar set, and all other sets should coincide with
        the domain of *PeriodData*.

    *Timetable*
        An indexed set in a calendar and defined over a horizon. This horizon
        and calendar should match with the index domains of ``TimeslotData`` and
        ``PeriodData``.

    *Type*
        An element of the pre-defined set :aimms:set:`AggregationTypes` (``summation``, ``average``,
        ``maximum``, ``minimum``, or ``interpolation``).

    *Locus (only for ``interpolation`` type)*
        A number between 0 and 1, that
        indicates at which moment in a period the quantity is to be measured.

.. seealso::

    The procedure :aimms:procedure:`Aggregate`. Time-dependent aggregation and disaggregation
    is discussed in full detail in Section 33.5 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
