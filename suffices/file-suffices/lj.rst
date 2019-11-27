.. _.lj:

.lj
===

Definition
----------

    The ``.lj`` suffix controls the element justification. When specified it
    overrides the option ``put_element_justification``.

Datatype
--------

    The value of the ``.lj`` suffix is integer in the range {1..3} and the
    default is ``-1``. The possible values are:

    1
       Right

    2
       Left

    3
       Center

.. note::

    -  The suffix ``.lj`` is initialized to ``-1``. AIMMS considers it
       specified when its value is not equal to ``-1``.

    -  The suffix ``.lj`` is a legacy from GAMS and AIMMS 2.
