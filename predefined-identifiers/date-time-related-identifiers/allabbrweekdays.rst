.. aimms:set:: AllAbbrWeekdays

.. _AllAbbrWeekdays:

AllAbbrWeekdays
===============

The predefined set :aimms:set:`AllAbbrWeekdays` contains the abbreviated English
names of all weekdays.

.. code-block:: aimms

        Set AllAbbrWeekdays {
            Index      :  IndexAbbrWeekdays;
            Definition :  data { Mon, Tue, Wed, Thu, Fri, Sat, Sun };
        }

Definition
----------

    The set :aimms:set:`AllAbbrWeekdays` contains the abbreviated English names of
    all weekdays.

Updatability
------------

    The contents of the set cannot be modified.

.. note::

    The set :aimms:set:`AllAbbrWeekdays` can be used to construct a date-time format
    specification as specified in Section 33.7. Such date-time format
    specifications are required, for instance, in the ``TimeslotFormat``
    attribute of a ``Calendar``.

.. seealso::

    The sets :aimms:set:`AllWeekdays`, :aimms:set:`LocaleAllAbbrWeekdays`, :aimms:set:`LocaleAllWeekdays`. Calendars are discussed in
    full detail in Section 33.2 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__, date-time formats
    in Section 33.7.
