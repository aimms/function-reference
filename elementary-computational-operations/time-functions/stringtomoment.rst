.. aimms:function:: StringToMoment(Format, Unit, ReferenceDate, Timeslot)

.. _StringToMoment:

StringToMoment
==============

The function :aimms:func:`StringToMoment` converts a given time string (in a free
time format) to the elapsed time with a respect to a specific reference
date.

.. code-block:: aimms

    StringToMoment(
         Format,             ! (input) a string expression
         Unit,               ! (input) a time unit
         ReferenceDate,      ! (input) a string expression
         Timeslot            ! (input) a string expression
         )

Arguments
---------

    *Format*
        A string that holds the date and time format used in the fourth argument
        *Timeslot*. Valid format strings are described in :doc:`advanced-language-components/time-based-modeling/format-of-time-slots-and-periods`.

    *Unit*
        The time unit that is used to return the elapsed time.

    *ReferenceDate*
        A string that holds the begin date using the fixed format for date and
        time, see paragraph :ref:`calendar.reference_date_format` of the Language
        Reference.
        
    .. note::
        Depending on the option ``use UTC forCaseAndStartEndDate``, reference dates
        are with respect to 
        
        * value ``on`` : timezone ``'UTC'`` or 
        * value ``off``: timezone ``'local'``.


    *Timeslot*
        A string representing a specific date and time moment using the format
        specified in the first argument *Format*.

Return Value
------------

    The result of :aimms:func:`StringToMoment` is the elapsed time in *unit* between
    *reference-date* and *date*.


Example
-----------

The code

.. code-block:: aimms

    block where use_UTC_forCaseAndStartEndDate := 'on' ;
        _p_noSec1 := StringToMoment(
            Format        :  "%c%y-%m-%d %H:%M:%S%TZ('UTC')", 
            Unit          :  [s], 
            ReferenceDate :  "2020-01-01 09:30:30", 
            Timeslot      :  "2020-01-01 09:30:58");
        display _p_noSec1 ;
    endblock ;
    block where use_UTC_forCaseAndStartEndDate := 'off' ;
        _p_noSec2 := StringToMoment(
            Format        :  "%c%y-%m-%d %H:%M:%S%TZ('local')", 
            Unit          :  [s], 
            ReferenceDate :  "2020-01-01 09:30:30", 
            Timeslot      :  "2020-01-01 09:30:58");
        display _p_noSec2 ;
    endblock ;


will result in:

.. code-block:: aimms

    _p_noSec1 := 28 [s] ;

    _p_noSec2 := 28 [s] ;




.. seealso::

    - The functions :aimms:func:`MomentToString`, :aimms:func:`CurrentToMoment`.
