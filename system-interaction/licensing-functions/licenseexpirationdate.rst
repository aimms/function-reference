.. aimms:procedure:: LicenseExpirationDate(date)

.. _LicenseExpirationDate:

LicenseExpirationDate
=====================

The procedure :aimms:func:`LicenseExpirationDate` returns the expiration date of
the current AIMMS license.

.. code-block:: aimms

    LicenseExpirationDate(
                         date    ! (output) a scalar string parameter
                         )

Arguments
---------

    *date*
        A scalar string parameter that, on return, contains the expiration date
        of the current AIMMS license.

Return Value
------------

    The procedure returns 1 on success, and 0 on failure.

.. note::

    The date returned by the procedure has the standard date format
    ``"YYYY-MM-DD"``, or holds the text ``"No expiration date"`` if the
    current AIMMS license has no expiration date.

.. seealso::

    The procedures :aimms:func:`LicenseStartDate`, :aimms:func:`LicenseMaintenanceExpirationDate`.
