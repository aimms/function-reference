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
    specification as specified in :doc:`advanced-language-components/time-based-modeling/format-of-time-slots-and-periods` Such date-time format
    specifications are required, for instance, in the ``TimeslotFormat``
    attribute of a ``Calendar``.

.. seealso::

    The sets :aimms:set:`AllWeekdays`, :aimms:set:`LocaleAllAbbrWeekdays`, :aimms:set:`LocaleAllWeekdays`. Calendars are discussed in
    full detail in :doc:`advanced-language-components/time-based-modeling/calendars` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__, date-time formats
    in :doc:`advanced-language-components/time-based-modeling/format-of-time-slots-and-periods`
