.. _.SmallestCoefficient:

.SmallestCoefficient
====================

Definition
----------

    When the property ``CoefficientRange`` of a variable is set and the
    option ``Calculate_Sensitivity_Ranges`` is not set to ``off`` a
    coefficient range sensitivity analysis is conducted such that the
    optimal basis remains constant. As a result of this analysis the
    variable suffix ``.SmallestCoefficient`` contains the smallest objective
    coefficient value.

Datatype
--------

    The value of the ``.SmallestCoefficient`` suffix is numeric.

Dimension
---------

    The ``.SmallestCoefficient`` suffix has the same dimension and domain as
    that of the variable at hand.

.. note::

    -  The default of the option ``Calculate_Sensitivity_Ranges`` is ``on``.

    -  See also Section 14.1 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
