.. aimms:set:: AllAbbrMonths

.. _AllAbbrMonths:

AllAbbrMonths
=============

The predefined set :aimms:set:`AllAbbrMonths` contains the abbreviated English
names of all months.

.. code-block:: aimms

        Set AllAbbrMonths {
            Index      :  IndexAbbrMonths;
            Definition :  {
                data { Jan, Feb, Mar, Apr, May, Jun,
                       Jul, Aug, Sep, Oct, Nov, Dec }
            }
        }

Definition
----------

    The set :aimms:set:`AllAbbrMonths` contains the abbreviated English names of all
    months.

Updatability
------------

    The contents of the set cannot be modified.

.. note::

    The set :aimms:set:`AllAbbrMonths` can be used to construct a date-time format
    specification as specified in Section 33.7. Such date-time format
    specifications are required, for instance, in the ``TimeslotFormat``
    attribute of a ``Calendar``.

.. seealso::

    The sets :aimms:set:`AllMonths`, :aimms:set:`LocaleAllAbbrMonths`, :aimms:set:`LocaleAllMonths`. Calendars are discussed in
    full detail in Section 33.2 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__, date-time formats
    in Section 33.7.
