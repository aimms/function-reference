.. aimms:procedure:: LicenseType(type, size)

.. _LicenseType:

LicenseType
===========

The procedure :aimms:func:`LicenseType` returns the type and size of the current
AIMMS license.

.. code-block:: aimms

    LicenseType(
               type,    ! (output) a scalar string parameter
               size     ! (output) a scalar string parameter
               )

Arguments
---------

    *type*
        A scalar string parameter that, on return, contains the type of the
        current license.

    *size*
        A scalar string parameter that, on return, contains the size of the
        current license.

Return Value
------------

    The procedure returns 1 on success, and 0 on failure.

.. note::

    Upon success, the *type* argument contains the license type description
    (e.g. ``"Economy"``) and the *size* argument contains a description of
    the license size (e.g. ``"Large"``).

.. seealso::

    The procedure :aimms:func:`LicenseNumber`.
