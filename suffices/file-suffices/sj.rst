.. _.sj:

.sj
===

Definition
----------

    The ``.sj`` suffix controls the justification of the texts associated
    with elements in a *GAMS* model. In an AIMMS model a string parameter is
    used instead of associating texts with elements. When specified it
    overrides the option ``put_string_justification``.

Datatype
--------

    The value of the ``.sj`` suffix is integer in the range {1..3} and the
    default is ``-1``. The possible values are:

    1
       Right

    2
       Left

    3
       Center

.. note::

    -  The suffix ``.sj`` is initialized to ``-1``. AIMMS considers it
       specified when its value is not equal to ``-1``.

    -  The suffix ``.sj`` is a legacy from GAMS and AIMMS 2.
