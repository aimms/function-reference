.. _.nd:

.nd
===

Definition
----------

    The ``.nd`` suffix controls the number of decimals displayed. When
    specified it overrides the option ``put_number_decimals``.

Datatype
--------

    The value of the ``.nd`` suffix is an integer in the range
    {0..``option listing_page_width``} and the default is -1.

.. note::

    -  The suffix ``.nd`` is initialized to ``-1``. AIMMS considers it
       specified when its value is not equal to ``-1``.

    -  The suffix ``.nd`` is a legacy from GAMS and AIMMS 2.
