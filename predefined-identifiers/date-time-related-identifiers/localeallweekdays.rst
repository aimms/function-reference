.. aimms:set:: LocaleAllWeekdays

.. _LocaleAllWeekdays:

LocaleAllWeekdays
=================

The predefined set :aimms:set:`LocaleAllWeekdays` contains the unabbreviated
names of all weekdays according the current system locale.

.. code-block:: aimms

        Set LocaleAllWeekdays {
            Index      :  LocaleIndexWeekdays;
        }

Definition
----------

    The set :aimms:set:`LocaleAllWeekdays` contains the unabbreviated names of all
    weekdays according to the current system locale.

Updatability
------------

    During system startup, the set :aimms:set:`LocaleAllWeekdays` is filled with the
    set of unabbreviated weekday names according to the current system
    locale. The contents of the set cannot be modified.

.. note::

    The set :aimms:set:`LocaleAllWeekdays` can be used to construct a date-time
    format specification as specified in :doc:`advanced-language-components/time-based-modeling/format-of-time-slots-and-periods` Such date-time format
    specifications are required, for instance, in the ``TimeslotFormat``
    attribute of a ``Calendar``. The current system locale can be modified
    through the **Regional Settings** dialog box in the Windows **Control
    Panel**.

.. seealso::

    The sets :aimms:set:`AllAbbrWeekdays`, :aimms:set:`AllWeekdays`, :aimms:set:`LocaleAllAbbrWeekdays`. Calendars are discussed in
    full detail in :doc:`advanced-language-components/time-based-modeling/calendars` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__, date-time formats
    in :doc:`advanced-language-components/time-based-modeling/format-of-time-slots-and-periods`
