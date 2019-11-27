.. _.lw:

.lw
===

Definition
----------

    The ``.lw`` suffix controls the element field width. When specified it
    overrides the option ``put_element_width``.

Datatype
--------

    The value of the ``.lw`` suffix is an integer in the range
    {0..``option listing_page_width``} and the default is -1.

.. note::

    -  The suffix ``.lw`` is initialized to ``-1``. AIMMS considers it
       specified when its value is not equal to ``-1``.

    -  The suffix ``.lw`` is a legacy from GAMS and AIMMS 2.
