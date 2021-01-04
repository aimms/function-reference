.. _.SmallestValue:

.SmallestValue
==============

Definition
----------

    When the property ``ValueRange`` of a variable is set and the option
    ``Calculate_Sensitivity_Ranges`` is not set to ``off`` a value range
    sensitivity analysis is conducted such that the objective value remains
    constant. As a result of this analysis the variable suffix
    ``.SmallestValue`` contains the smallest possible value of that
    variable.

Datatype
--------

    The value of the ``.SmallestValue`` suffix is numeric.

Dimension
---------

    The ``.SmallestValue`` suffix has the same dimension and domain as that
    of the variable at hand.

.. note::

    -  The default of the option ``Calculate_Sensitivity_Ranges`` is ``on``.

    -  See also :doc:`optimization-modeling-components/variable-and-constraint-declaration/variable-declaration-and-attributes` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
