.. _.PageWidth:

.PageWidth
==========

Definition
----------

    The file suffix ``.PageWidth`` controls the maximum number of characters
    per line. When specified it overrides the option ``listing_page_width``.

Datatype
--------

    The value of the ``.PageWidth`` suffix is an integer in the range
    {30..32767}.

.. note::

    -  The suffix ``.PageWidth`` is initialized to ``-1``. AIMMS considers
       it specified when its value is not equal to ``-1``.

    -  The equivalent GAMS and AIMMS 2 name is ``.pw``.

    -  See also Section 31.4 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
