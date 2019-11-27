.. aimms:procedure:: AimmsRevisionString(Version, NumberOfFields)

.. _AimmsRevisionString:

AimmsRevisionString
===================

The procedure :aimms:func:`AimmsRevisionString` returns the revision number of the
current AIMMS executable.

.. code-block:: aimms

    AimmsRevisionString(
                       Version        ! (output) a scalar string parameter
                       NumberOfFields ! (optional) a scalar numerical expression)

Arguments
---------

    *Version*
        A scalar string parameter that, on return, contains the current revision
        number.

    *NumberOfFields*
        A scalar integer expression indicating the number of fields displayed in
        the revision string.

Return Value
------------

    The procedure returns 1 on success, and 0 on failure.

.. note::

    The revision string returned by the procedure has the format
    "``x.y.b.r``" where *x* represents the major AIMMS version number
    (e.g. 3), *y* represents the minor AIMMS version number (e.g. 0), where
    *b* represents the build number (e.g. 476) of the current executable,
    and where *r* represents the internal revision number.
