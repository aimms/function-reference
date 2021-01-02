.. aimms:set:: AllMonths

.. _AllMonths:

AllMonths
=========

The predefined set :aimms:set:`AllMonths` contains the unabbreviated English
names of all months.

.. code-block:: aimms

        Set AllMonths {
            Index      :  IndexMonths;
            Definition :  {
                data { January, February, March, April,
                       May, June, July, August,
                       September, October, November, December }
            }
        }

Definition
----------

    The set :aimms:set:`AllMonths` contains the unabbreviated English names of all
    months.

Updatability
------------

    The contents of the set cannot be modified.

.. note::

    The set :aimms:set:`AllMonths` can be used to construct a date-time format
    specification as specified in :doc:`advanced-language-components/time-based-modeling/format-of-time-slots-and-periods` Such date-time format
    specifications are required, for instance, in the ``TimeslotFormat``
    attribute of a ``Calendar``.

.. seealso::

    The sets :aimms:set:`AllAbbrMonths`, :aimms:set:`LocaleAllMonths`, :aimms:set:`LocaleAllMonths`. Calendars are discussed in
    full detail in :doc:`advanced-language-components/time-based-modeling/calendars` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__, date-time formats
    in :doc:`advanced-language-components/time-based-modeling/format-of-time-slots-and-periods`
