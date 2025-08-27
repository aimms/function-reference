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



Example
-----------

Given the `timetable declarations in the example of CreateTimeTable   <https://documentation.aimms.com/functionreference/elementary-computational-operations/time-functions/createtimetable.html>`_ and the following declarations:

.. code-block:: aimms

	Parameter p_datCal {
		IndexDomain: i_day;
		Definition: {
			data 
			{ 2024-01-01 : 3,  
			  2024-01-02 : 4,  
			  2024-01-03 : 5,  
			  2024-01-04 : 3,  
			  2024-01-05 : 4,  
			  2024-01-06 : 5,  
			  2024-01-07 : 3,
			  2024-01-08 : 4,  
			  2024-01-09 : 5,  
			  2024-01-10 : 3,  
			  2024-01-11 : 4,  
			  2024-01-12 : 5,  
			  2024-01-13 : 3,  
			  2024-01-14 : 4 }
		}
	}
	Parameter p_datHor {
		IndexDomain: i_hor;
	}

The code

.. code-block:: aimms

	Aggregate(
		TimeSlotData :  p_datCal, 
		PeriodData   :  p_datHor, 
		TimeTable    :  s_timetable, 
		Type         :  'summation' );

produces:


.. code-block:: aimms

	p_datHor := data { 
		p0 :  3,  
		p1 :  9,  
		p2 : 12,  
		p3 : 15,  
		p4 : 16 } ;


.. seealso::

    - The procedure :aimms:procedure:`DisAggregate`. 
	- Time-dependent aggregation and disaggregation is discussed in full detail in :doc:`advanced-language-components/time-based-modeling/data-conversion-of-time-dependent-identifiers` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
