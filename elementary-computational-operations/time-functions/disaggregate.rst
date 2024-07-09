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


Example
-----------


Given the `timetable declarations in the example of CreateTimeTable   <https://documentation.aimms.com/functionreference/elementary-computational-operations/time-functions/createtimetable.html>`_ and the following declarations:

.. code-block:: aimms

	Parameter p_datCal {
		IndexDomain: i_day;
	}
	Parameter p_datHor {
		IndexDomain: i_hor;
		Definition: {
			data 
			{ p0 : 20,  
			  p1 : 30,
			  p2 : 40,
			  p3 : 50,
			  p4 : 60
			 }
		}
	}

The code

.. code-block:: aimms

	DisAggregate(
		PeriodData   :  p_datHor, 
		TimeSlotData :  p_datCal, 
		TimeTable    :  s_timetable, 
		Type         :  'summation' );

Produces:

.. code-block:: aimms

    p_datCal(i_day) := data 
    { 2024-01-01 : 20.000,
      2024-01-02 : 15.000,
      2024-01-03 : 15.000,
      2024-01-04 : 13.333,
      2024-01-05 : 13.333,
      2024-01-06 : 13.333,
      2024-01-07 : 12.500,
      2024-01-08 : 12.500,
      2024-01-09 : 12.500,
      2024-01-10 : 12.500,
      2024-01-11 : 15.000,
      2024-01-12 : 15.000,
      2024-01-13 : 15.000,
      2024-01-14 : 15.000 } ;



.. seealso::

    The procedure :aimms:procedure:`Aggregate`. Time-dependent aggregation and disaggregation
    is discussed in full detail in :doc:`advanced-language-components/time-based-modeling/data-conversion-of-time-dependent-identifiers` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
