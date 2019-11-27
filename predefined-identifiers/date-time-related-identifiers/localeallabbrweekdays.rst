.. aimms:set:: LocaleAllAbbrWeekdays

.. _LocaleAllAbbrWeekdays:

LocaleAllAbbrWeekdays
=====================

The predefined set :aimms:set:`LocaleAllAbbrWeekdays` contains the abbreviated
names of all weekdays according the current system locale.

.. code-block:: aimms

        Set LocaleAllAbbrWeekdays {
            Index      :  LocaleIndexAbbrWeekdays;
        }

Definition
----------

    The set :aimms:set:`LocaleAllAbbrWeekdays` contains the abbreviated names of all
    weekdays according to the current system locale.

Updatability
------------

    During system startup, the set :aimms:set:`LocaleAllAbbrWeekdays` is filled with
    the set of abbreviated weekday names according to the current system
    locale. The contents of the set cannot be modified.

.. note::

    The set :aimms:set:`LocaleAllAbbrWeekdays` can be used to construct a date-time
    format specification as specified in Section 33.7. Such date-time format
    specifications are required, for instance, in the ``TimeslotFormat``
    attribute of a ``Calendar``. The current system locale can be modified
    through the **Regional Settings** dialog box in the Windows **Control
    Panel**.

.. seealso::

    The sets :aimms:set:`AllAbbrWeekdays`, :aimms:set:`AllWeekdays`, :aimms:set:`LocaleAllWeekdays`. Calendars are discussed in
    full detail in Section 33.2 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__, date-time formats
    in Section 33.7.
