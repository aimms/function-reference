.. aimms:procedure:: LicenseNumber(license)

.. _LicenseNumber:

LicenseNumber
=============

The procedure :aimms:func:`LicenseNumber` returns the license number of the
current AIMMS license.

.. code-block:: aimms

    LicenseNumber(
                 license    ! (output) a scalar string parameter
                 )

Arguments
---------

    *license*
        A scalar string parameter that, on return, contains the current license
        number.

Return Value
------------

    The procedure returns 1 on success, and 0 on failure.

.. note::

    The procedure will return the license number as a string of the form
    ``015.090.010.007`` if you are using an AIMMS 3 license, or as a
    string of the form ``1234.56`` if you are using an AIMMS 2 license.

.. seealso::

    The procedure :aimms:func:`LicenseType`.
