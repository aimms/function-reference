.. _.Nonvar:

.Nonvar
=======

Definition
----------

    The ``.Nonvar`` suffix controls whether individual variables are frozen
    or not. This suffix can take on three values:

    #. This variable is not frozen and a value for the variable should be
       found in the next solve statement.

    #. This variable is frozen and it will retain its value during the SOLVE
       statement. The corresponding column will be removed from the
       generated mathematical program for the sake of efficiency.

    #. This variable is frozen and it will retain its value during the SOLVE
       statement. The corresponding column will *not* be removed from the
       generated mathematical program but can be manipulated during
       subsequent calls of the GMP function library.

Datatype
--------

    The value of the ``.Nonvar`` suffix is an integer in the range
    :math:`\{ -1, 0, 1 \}` and the default is 0.

Dimension
---------

    The ``.Nonvar`` suffix has the same dimension and domain as that of the
    constraint or variable at hand.

.. note::

    -  When the ``.lower`` suffix of a variable is equal to the ``.upper``
       suffix of the same variable that variable is treated as a frozen
       variable and subsequently removed from the generated mathematical
       program independently from the setting of the ``.nonvar`` suffix.

    -  See also Section 14.1 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.

    -  The AIMMS 2 equivalent suffix name is ``.freeze``.

    -  The ``.NonVar`` suffix should not be confused with the GAMS suffix
       ``.fx``. This latter suffix is a shorthand for the GAMS suffixes
       ``.l``, ``.lo`` and ``.up``.
