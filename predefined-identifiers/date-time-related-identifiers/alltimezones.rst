.. aimms:set:: AllTimeZones

.. _AllTimeZones:

AllTimeZones
============

The predefined set :aimms:set:`AllTimeZones` contains the set of all available
time zones.

.. code-block:: aimms

        Set AllTimeZones {
            Index      :  IndexTimeZones;
        }

Definition
----------

    The set :aimms:set:`AllTimeZones` contains the set of all time zones as defined
    by the operating system, plus a number of predefined time zones.

Updatability
------------

    The contents of the set cannot be modified.

.. note::

    The set :aimms:set:`AllTimeZones` can be used in the ``\%TZ`` specifier of a time
    slot or period format. Such time zone specifications can be used, for
    instance, in the ``TimeslotFormat`` attribute of a ``Calendar``.

.. seealso::

    Calendars are discussed in full detail in :doc:`advanced-language-components/time-based-modeling/calendars` of the Language
    Reference, the time zone specific part of a date-time format in :ref:`sec:time.format.dst`.
