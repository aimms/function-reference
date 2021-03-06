.. _.ReducedCost:

.ReducedCost
============

Definition
----------

    When the property ``ReducedCost`` of a variable is set or when the
    option ``Always_store_marginals`` is set to ``on``, the ``.ReducedCost``
    suffix contains the reduced cost of that variable.

Datatype
--------

    The value of the ``.ReducedCost`` suffix is numeric.

Dimension
---------

    The ``.ReducedCost`` suffix has the same dimension and domain as that of
    the constraint at hand.

.. note::

    -  The GAMS equivalent suffix name is ``.m``.

    -  The default of the option ``Always_store_marginals`` is ``off``.

    -  See also :doc:`optimization-modeling-components/variable-and-constraint-declaration/variable-declaration-and-attributes` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
