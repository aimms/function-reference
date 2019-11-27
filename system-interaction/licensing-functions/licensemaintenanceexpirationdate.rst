.. aimms:procedure:: LicenseMaintenanceExpirationDate(date)

.. _LicenseMaintenanceExpirationDate:

LicenseMaintenanceExpirationDate
================================

The procedure :aimms:func:`LicenseMaintenanceExpirationDate` returns the
maintenance expiration date of the current AIMMS license.

.. code-block:: aimms

    LicenseMaintenanceExpirationDate(
                                    date    ! (output) a scalar string parameter
                                    )

Arguments
---------

    *date*
        A scalar string parameter that, on return, contains the maintenance
        expiration date of the current AIMMS license.

Return Value
------------

    The procedure returns 1 on success, and 0 on failure.

.. note::

    The date returned by the procedure has the standard date format
    ``"YYYY-MM-DD"``, or holds the text ``"No maintenance expiration date"``
    if the current AIMMS license has no maintenance expiration date.

.. seealso::

    The procedures :aimms:func:`LicenseStartDate`, :aimms:func:`LicenseExpirationDate`.
