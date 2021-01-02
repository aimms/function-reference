.. _.Relax:

.Relax
======

Definition
----------

    The variable suffix ``.Relax`` controls whether the integer variable at
    hand is relaxed to a continuous range or not. This suffix can take on
    two values:

    ``0``
       This variable is not relaxed and its restriction to take on only
       integral values is passed on to the solver.

    ``1``
       This variable is relaxed to the continuous range directly
       encompassing its original integral range.

Datatype
--------

    The value of the ``.Relax`` suffix is an integer in the range
    :math:`\{ 0, 1 \}` and the default is 0.

Dimension
---------

    The ``.Relax`` suffix has the same dimension and domain as that of the
    constraint or variable at hand.

.. note::

    -  See also :doc:`optimization-modeling-components/variable-and-constraint-declaration/variable-declaration-and-attributes` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
