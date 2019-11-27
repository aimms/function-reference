.. aimms:set:: LocaleAllMonths

.. _LocaleAllMonths:

LocaleAllMonths
===============

The predefined set :aimms:set:`LocaleAllMonths` contains the unabbreviated names
of all months according the current system locale.

.. code-block:: aimms

        Set LocaleAllMonths {
            Index      :  LocaleIndexMonths;
        }

Definition
----------

    The set :aimms:set:`LocaleAllMonths` contains the unabbreviated names of all
    months according to the current system locale.

Updatability
------------

    During system startup, the set :aimms:set:`LocaleAllMonths` is filled with the
    set of unabbreviated month names according to the current system locale.
    The contents of the set cannot be modified.

.. note::

    The set :aimms:set:`LocaleAllMonths` can be used to construct a date-time format
    specification as specified in Section 33.7. Such date-time format
    specifications are required, for instance, in the ``TimeslotFormat``
    attribute of a ``Calendar``. The current system locale can be modified
    through the **Regional Settings** dialog box in the Windows **Control
    Panel**.

.. seealso::

    The sets :aimms:set:`AllAbbrMonths`, :aimms:set:`AllMonths`, :aimms:set:`LocaleAllAbbrMonths`. Calendars are discussed in
    full detail in Section 33.2 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__, date-time formats
    in Section 33.7.
