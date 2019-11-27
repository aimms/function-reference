.. _.nw:

.nw
===

Definition
----------

    The ``.nw`` suffix controls numeric field width. When specified it
    overrides the option ``put_number_width``.

Datatype
--------

    The value of the ``.nw`` suffix is an integer in the range
    {0..``option listing_page_width``} and the default is -1.

.. note::

    -  The suffix ``.nw`` is initialized to ``-1``. AIMMS considers it
       specified when its value is not equal to ``-1``.

    -  The suffix ``.nw`` is a legacy from GAMS and AIMMS 2.
