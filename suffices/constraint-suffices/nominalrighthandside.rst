.. _.NominalRightHandSide:

.NominalRightHandSide
=====================

Definition
----------

    When the property ``RightHandSideRange`` of a contraint is set and the
    option ``Calculate_Sensitivity_Ranges`` is not set to ``off`` the
    ``.NominalRightHandSide`` suffix contains the right hand side value of
    the constraint. In case of a ranged constraint it contains the largest
    of the two constraint bounds.

Datatype
--------

    The value of the ``.NominalRightHandSide`` suffix is numeric.

Dimension
---------

    The ``.NominalRightHandSide`` suffix has the same dimension and domain
    as that of the constraint at hand.

.. note::

    -  When a variable ``X`` has a definition the suffix can also be applied
       to ``X`` but this is not encouraged by the syntax highlighting. The
       preferred usage is ``X_definition.NominalRightHandSide``.

    -  The default of the option ``Calculate_Sensitivity_Ranges`` is ``on``.

    -  See also Section 14.2 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
