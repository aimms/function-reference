.. aimms:set:: LocaleShortDateFormat

.. _LocaleShortDateFormat:

LocaleShortDateFormat
=====================

The predefined string parameter :aimms:set:`LocaleShortDateFormat` contains the
AIMMS date-time format equivalent with the short date format as
specified in the current system locale.

.. code-block:: aimms

        StringParameter LocaleShortDateFormat;

Definition
----------

    The string parameter :aimms:set:`LocaleShortDateFormat` contains the AIMMS
    date-time format equivalent with the short date format as specified in
    the current system locale.

Updatability
------------

    During system startup, the string parameter :aimms:set:`LocaleShortDateFormat` is
    computed on the basis of the information in the current system locale.
    The contents of the string parameter cannot be modified.

.. note::

    The string parameter :aimms:set:`LocaleShortDateFormat` can be used, for
    instance, in the ``TimeslotFormat`` attribute of a ``Calendar``. The
    current system locale can be modified through the **Regional Settings**
    dialog box in the Windows **Control Panel**.

.. seealso::

    The string parameters :aimms:set:`LocaleLongDateFormat`, :aimms:set:`LocaleTimeFormat`. Calendars are discussed in
    full detail in Section 33.2 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__, date-time formats
    in Section 33.7.
