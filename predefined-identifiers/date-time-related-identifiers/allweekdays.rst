.. aimms:set:: AllWeekdays

.. _AllWeekdays:

AllWeekdays
===========

The predefined set :aimms:set:`AllWeekdays` contains the unabbreviated English
names of all weekdays.

.. code-block:: aimms

        Set AllWeekdays {
            Index      :  IndexWeekdays;
            Definition :  {
                data { Monday, Tuesday, Wednesday, Thursday,
                       Friday, Saturday, Sunday }
            }
        }

Definition
----------

    The set :aimms:set:`AllWeekdays` contains the unabbreviated English names of all
    weekdays.

Updatability
------------

    The contents of the set cannot be modified.

.. note::

    The set :aimms:set:`AllWeekdays` can be used to construct a date-time format
    specification as specified in :doc:`advanced-language-components/time-based-modeling/format-of-time-slots-and-periods` Such date-time format
    specifications are required, for instance, in the ``TimeslotFormat``
    attribute of a ``Calendar``.

.. seealso::

    The sets :aimms:set:`AllAbbrWeekdays`, :aimms:set:`LocaleAllWeekdays`, :aimms:set:`LocaleAllWeekdays`. Calendars are discussed in
    full detail in :doc:`advanced-language-components/time-based-modeling/calendars` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__, date-time formats
    in :doc:`advanced-language-components/time-based-modeling/format-of-time-slots-and-periods`
