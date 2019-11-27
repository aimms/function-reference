.. _.nr:

.nr
===

Definition
----------

    The ``.nr`` suffix controls the numeric formatting method. When
    specified it overrides the option ``put_number_style``.

Datatype
--------

    The value of the ``.nr`` suffix is an integer in the range {0..3} and
    the default is ``-1``. The possible values are:

    0
       Fit field or e format

    1
       Fit field width

    2
       Always e format

    3
       Fit field or e format or 0

.. note::

    -  The suffix ``.nr`` is initialized to ``-1``. AIMMS considers it
       specified when its value is not equal to ``-1``.

    -  The suffix ``.nr`` is a legacy from GAMS and AIMMS 2.
