.. aimms:set:: TimeSlotCharacteristics

.. _TimeSlotCharacteristics:

TimeSlotCharacteristics
=======================

The predefined set :aimms:set:`TimeSlotCharacteristics` contains the collection
of timeslot characteristic which can be used in conjunction with the
function :aimms:func:`TimeSlotCharacteristic`.

.. code-block:: aimms

        Set TimeSlotCharacteristics {
            Index      :  IndexTimeSlotCharacteristics;
            Definition :  {
                data { century, year, quarter, month
                weekday, yearday, monthday
                week, weekyear, weekcentury
                hour, minute, second, tick }
            }
        }

Definition
----------

    The set :aimms:set:`TimeSlotCharacteristics` contains the collection of timeslot
    characteristic which can be used in conjunction with the function
    :aimms:func:`TimeSlotCharacteristic`.

Updatability
------------

    The contents of the set cannot be modified.

.. note::

    Element parameters into :aimms:set:`TimeSlotCharacteristics` can be used as the
    *characteristic* argument of the :aimms:func:`TimeSlotCharacteristic` function.

.. seealso::

    The function :aimms:func:`TimeSlotCharacteristic`. The use of the function
    ``TimeSlotCharacteristic`` is explained in more detail in :doc:`advanced-language-components/time-based-modeling/creating-timetables`
    of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
