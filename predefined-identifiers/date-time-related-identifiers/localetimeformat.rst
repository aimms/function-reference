.. aimms:set:: LocaleTimeFormat

.. _LocaleTimeFormat:

LocaleTimeFormat
================

The predefined string parameter :aimms:set:`LocaleTimeFormat` contains the AIMMS
date-time format equivalent with the time format specified in the
current system locale.

.. code-block:: aimms

        StringParameter LocaleTimeFormat;

Definition
----------

    The string parameter :aimms:set:`LocaleTimeFormat` contains the AIMMS date-time
    format equivalent with the time format specified in the current system
    locale.

Updatability
------------

    During system startup, the string parameter :aimms:set:`LocaleTimeFormat` is
    computed on the basis of the information in the current system locale.
    The contents of the string parameter cannot be modified.

.. note::

    The string parameter :aimms:set:`LocaleTimeFormat` can be used, for instance, in
    the ``TimeslotFormat`` attribute of a ``Calendar``. The current system
    locale can be modified through the **Regional Settings** dialog box in
    the Windows **Control Panel**.

.. seealso::

    The string parameters :aimms:set:`LocaleLongDateFormat`, :aimms:set:`LocaleShortDateFormat`. Calendars are discussed in
    full detail in Section 33.2 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__, date-time formats
    in Section 33.7.
