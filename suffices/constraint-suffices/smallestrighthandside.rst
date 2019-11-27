.. _.SmallestRightHandSide:

.SmallestRightHandSide
======================

Definition
----------

    When the property ``RightHandSideRange`` of a contraint is set and the
    option ``Calculate_Sensitivity_Ranges`` is not set to ``off`` the
    ``.SmallestRightHandSide`` suffix contains the smallest right hand side
    such that the basis remains constant.

Datatype
--------

    The value of the ``.SmallestRightHandSide`` suffix is numeric.

Dimension
---------

    The ``.SmallestRightHandSide`` suffix has the same dimension and domain
    as that of the constraint at hand.

.. note::

    -  When a variable ``X`` has a definition the suffix can also be applied
       to ``X`` but this is not encouraged by the syntax highlighting. The
       preferred usage is ``X_definition.SmallestRightHandSide``.

    -  The default of the option ``Calculate_Sensitivity_Ranges`` is ``on``.

    -  See also Section 14.2 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
