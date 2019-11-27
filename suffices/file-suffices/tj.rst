.. _.tj:

.tj
===

Definition
----------

    The ``.tj`` suffix controls the justification when putting the text
    associated with identifiers. When specified it overrides the option
    ``put_string_justification``.

Datatype
--------

    The value of the ``.tj`` suffix is integer in the range {1..3} and the
    default is ``-1``. The possible values are:

    1
       Right

    2
       Left

    3
       Center

.. note::

    -  The suffix ``.tj`` is initialized to ``-1``. AIMMS considers it
       specified when its value is not equal to ``-1``.

    -  The suffix ``.tj`` is a legacy from GAMS and AIMMS 2.
