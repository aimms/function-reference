.. _.tw:

.tw
===

Definition
----------

    The ``.tw`` suffix controls field width when putting the text associated
    with identifiers. When specified it overrides the option
    ``put_string_width``.

Datatype
--------

    The value of the ``.tw`` suffix is an integer in the range
    {0..``option listing_page_width``} and the default is -1.

.. note::

    -  The suffix ``.tw`` is initialized to ``-1``. When its value is not
       equal to ``-1`` AIMMS considers it specified.

    -  The suffix ``.tw`` is a legacy from GAMS and AIMMS 2.
