.. _.nz:

.nz
===

Definition
----------

    The ``.nz`` suffix controls the nonzero tolerance. When specified it
    overrides the option ``put_number_tolerance``.

Datatype
--------

    The value of the ``.nz`` suffix is a floating point number in the range
    [0,1] and the default is -1.0.

.. note::

    -  The suffix ``.nz`` is initialized to ``-1.0``. AIMMS considers it
       specified when its value is not equal to ``-1.0``.

    -  The suffix ``.nz`` is a legacy from GAMS and AIMMS 2.
