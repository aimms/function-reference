.. _.blank_zeros:

.blank_zeros
============

Definition
----------

    The ``.blank_zeros`` suffix controls whether or not numbers (almost)
    equal to 0.0 should be printed as blanks or as 0.0's according to the
    current format.

Datatype
--------

    The value of the ``.blank_zeros`` suffix is an integer in the range
    {0..2} and the default is 0. The possible values are:

    0
       Do not print numbers equal or within AIMMS tolerances equal to 0.0 as
       blanks.

    1
       Print numbers equal or within AIMMS tolerances equal to 0.0 as
       blanks.

    2
       Print numbers after formatting equal to 0.0 as blanks.
