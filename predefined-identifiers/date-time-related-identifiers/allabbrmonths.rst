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
    specification as specified in :doc:`advanced-language-components/time-based-modeling/format-of-time-slots-and-periods` Such date-time format
    specifications are required, for instance, in the ``TimeslotFormat``
    attribute of a ``Calendar``.

.. seealso::

    The sets :aimms:set:`AllMonths`, :aimms:set:`LocaleAllAbbrMonths`, :aimms:set:`LocaleAllMonths`. Calendars are discussed in
    full detail in :doc:`advanced-language-components/time-based-modeling/calendars` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__, date-time formats
    in :doc:`advanced-language-components/time-based-modeling/format-of-time-slots-and-periods`
