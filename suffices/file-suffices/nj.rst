.. _.nj:

.nj
===

Definition
----------

    The ``.nj`` suffix controls numeric justification. When specified it
    overrides the option ``put_number_justification``.

Datatype
--------

    The value of the ``.nj`` suffix is integer in the range {1..3} and the
    default is ``-1``. The possible values are:

    1
       Right

    2
       Left

    3
       Center

.. note::

    -  The suffix ``.nj`` is initialized to ``-1``. AIMMS considers it
       specified when its value is not equal to ``-1``.

    -  The suffix ``.nj`` is a legacy from GAMS and AIMMS 2.
