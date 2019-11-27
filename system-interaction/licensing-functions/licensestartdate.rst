.. aimms:procedure:: LicenseStartDate(date)

.. _LicenseStartDate:

LicenseStartDate
================

The procedure :aimms:func:`LicenseStartDate` returns the start date of the current
AIMMS license.

.. code-block:: aimms

    LicenseStartDate(
                    date    ! (output) a scalar string parameter
                    )

Arguments
---------

    *date*
        A scalar string parameter that, on return, contains the start date of
        the current AIMMS license.

Return Value
------------

    The procedure returns 1 on success, and 0 on failure.

.. note::

    The date returned by the procedure has the standard date format
    ``"YYYY-MM-DD"``, or holds the text ``"No start date"`` if the current
    AIMMS license has no start date.

.. seealso::

    The procedures :aimms:func:`LicenseExpirationDate`, :aimms:func:`LicenseMaintenanceExpirationDate`.
