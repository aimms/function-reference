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
    format specification as specified in Section 33.7. Such date-time format
    specifications are required, for instance, in the ``TimeslotFormat``
    attribute of a ``Calendar``. The current system locale can be modified
    through the **Regional Settings** dialog box in the Windows **Control
    Panel**.

.. seealso::

    The sets :aimms:set:`AllAbbrWeekdays`, :aimms:set:`AllWeekdays`, :aimms:set:`LocaleAllAbbrWeekdays`. Calendars are discussed in
    full detail in Section 33.2 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__, date-time formats
    in Section 33.7.
