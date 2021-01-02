.. _.LargestShadowPrice:

.LargestShadowPrice
===================

Definition
----------

    When the property ``LargestShadowPrice`` of a contraint is set and when
    the option ``Calculate_Sensitivity_Ranges`` is set to ``on``, the
    ``.LargestShadowPrice`` suffix contains the largest shadow price of the
    constraint while holding the objective value constant.

Datatype
--------

    The value of the ``.LargestShadowPrice`` suffix is numeric.

Dimension
---------

    The ``.LargestShadowPrice`` suffix has the same dimension and domain as
    that of the constraint at hand.

.. note::

    -  When a variable ``X`` has a definition the suffix can also be applied
       to ``X`` but this is not encouraged by the syntax highlighting. The
       preferred usage is ``X_definition.LargestShadowPrice``.

    -  The default of the option ``Calculate_Sensitivity_Ranges`` is ``on``.

    -  See also :doc:`optimization-modeling-components/variable-and-constraint-declaration/constraint-declaration-and-attributes` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
