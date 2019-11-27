.. aimms:set:: LocaleTimeZoneName

.. _LocaleTimeZoneName:

LocaleTimeZoneName
==================

The predefined string parameter :aimms:set:`LocaleTimeZoneName` contains the
local name of all standard time zones.

.. code-block:: aimms

        StringParameter LocaleTimeZoneName {
             IndexDomain :  IndexTimeZones;
        }

.. seealso::

    The predeclared identifier :aimms:set:`LocaleTimeZoneNameDST` contains the local name of all
    daylight saving time zones.
