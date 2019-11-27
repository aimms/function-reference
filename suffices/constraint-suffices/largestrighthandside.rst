.. _.LargestRightHandSide:

.LargestRightHandSide
=====================

Definition
----------

    When the property ``RightHandSideRange`` of a contraint is set and the
    option ``Calculate_Sensitivity_Ranges`` is not set to ``off`` the
    ``.LargestRightHandSide`` suffix contains the largest right hand side
    such that the basis remains constant.

Datatype
--------

    The value of the ``.LargestRightHandSide`` suffix is numeric.

Dimension
---------

    The ``.LargestRightHandSide`` suffix has the same dimension and domain
    as that of the constraint at hand.

.. note::

    -  When a variable ``X`` has a definition the suffix can also be applied
       to ``X`` but this is not encouraged by the syntax highlighting. The
       preferred usage is ``X_definition.LargestRightHandSide``.

    -  The default of the option ``Calculate_Sensitivity_Ranges`` is ``on``.

    -  See also Section 14.2 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
