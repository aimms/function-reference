.. _.sw:

.sw
===

Definition
----------

    The ``.sw`` suffix controls the field width of the texts associated with
    elements in a *GAMS* model. In an AIMMS model a string parameter is used
    instead of associating texts with elements. A value of 0 implies
    variable length. When specified it overrides the option
    ``put_string_width``.

Datatype
--------

    The value of the ``.sw`` suffix is an integer in the range
    {0..``option listing_page_width``} and the default is -1.

.. note::

    -  The suffix ``.sw`` is initialized to ``-1``. AIMMS considers it
       specified when its value is not equal to ``-1``.

    -  The suffix ``.sw`` is a legacy from GAMS and AIMMS 2.
