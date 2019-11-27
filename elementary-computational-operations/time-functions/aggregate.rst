.. aimms:procedure:: Aggregate(TimeslotData, PeriodData, TimeTable, Type[, Locus])

.. _Aggregate:

Aggregate
=========

With the procedure :aimms:procedure:`Aggregate` you can aggregate time-dependent data
from a calendar time scale (time slots) to a horizon time scale
(periods).

.. code-block:: aimms

    Aggregate(
         TimeslotData,        ! (input) an indexed identifier over a calendar
         PeriodData,          ! (output) an indexed identifier over a horizon
         TimeTable,           ! (input) an AIMMS time table
         Type,                ! (input) an element in the set AggregationTypes
         [Locus]              ! (optional) a value between 0 and 1
         )

Arguments
---------

    *TimeslotData*
        An identifier (slice) containing the data to be aggregated. The domain
        sets in the index domain of this identifier should at least contain a
        calendar set, and all other sets should coincide with the domain of
        *PeriodData*.

    *PeriodData*
        An identifier (slice) that on return will contain the aggregated data.
        The domain sets in the index domain of this identifier should at least
        contain a horizon set, and all other sets should coincide with the
        domain of *TimeslotData*.

    *TimeTable*
        An indexed set in a calendar and defined over a horizon. This horizon
        and calendar should match with the index domains of *TimeslotData* and
        *PeriodData*.

    *Type*
        An element of the pre-defined set :aimms:set:`AggregationTypes` (``summation``, ``average``,
        ``maximum``, ``minimum``, or ``interpolation``).

    *Locus (only for* ``interpolation`` *type)*
        A number between 0 and 1, that
        indicates at which moment in a period the quantity is to be measured.

.. seealso::

    The procedure :aimms:procedure:`DisAggregate`. Time-dependent aggregation and disaggregation
    is discussed in full detail in Section 33.5 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
