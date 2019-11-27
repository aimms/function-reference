.. aimms:set:: LocaleTimeZoneNameDST

.. _LocaleTimeZoneNameDST:

LocaleTimeZoneNameDST
=====================

The predefined string parameter :aimms:set:`LocaleTimeZoneNameDST` contains the
local name of all daylight saving time zones.

.. code-block:: aimms

        StringParameter LocaleTimeZoneNameDST {
            IndexDomain  :  IndexTimeZones;
        }

.. seealso::

    The predeclared identifier :aimms:set:`LocaleTimeZoneName` contains the local name of all
    standard time zones.
