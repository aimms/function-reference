.. _.NominalCoefficient:

.NominalCoefficient
===================

Definition
----------

    When the property ``CoefficientRange`` of a variable is set and the
    option ``Calculate_Sensitivity_Ranges`` is not set to ``off`` a
    coefficient range sensitivity analysis is conducted such that the
    optimal basis remains constant. As a result of this analysis the
    variable suffix ``.NominalCoefficient`` contains the nominal objective
    coefficient value.

Datatype
--------

    The value of the ``.NominalCoefficient`` suffix is numeric.

Dimension
---------

    The ``.NominalCoefficient`` suffix has the same dimension and domain as
    that of the variable at hand.

.. note::

    -  The default of the option ``Calculate_Sensitivity_Ranges`` is ``on``.

    -  See also :doc:`optimization-modeling-components/variable-and-constraint-declaration/variable-declaration-and-attributes` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
