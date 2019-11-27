.. _.SmallestShadowPrice:

.SmallestShadowPrice
====================

Definition
----------

    When the property ``SmallestShadowPrice`` of a contraint is set and when
    the option ``Calculate_Sensitivity_Ranges`` is set to ``on``, the
    ``.SmallestShadowPrice`` suffix contains the smallest shadow price of
    the constraint while holding the objective value constant.

Datatype
--------

    The value of the ``.SmallestShadowPrice`` suffix is numeric.

Dimension
---------

    The ``.SmallestShadowPrice`` suffix has the same dimension and domain as
    that of the constraint at hand.

.. note::

    -  When a variable ``X`` has a definition the suffix can also be applied
       to ``X`` but this is not encouraged by the syntax highlighting. The
       preferred usage is ``X_definition.SmallestShadowPrice``.

    -  The default of the option ``Calculate_Sensitivity_Ranges`` is ``on``.

    -  See also Section 14.2 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
