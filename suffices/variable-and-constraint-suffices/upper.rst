.. _.Upper:

.Upper
======

Definition
----------

    The ``.Upper`` suffix contains the upper bound of a variable. When the
    property ``Bounds`` of a constraint is set, the ``.Upper`` suffix
    contains the maximum value the left hand side of the constraint may
    attain. Note that for a ``>=`` constraint this value is ``INF``. This
    value is set at the end of the generation step by AIMMS.

Datatype
--------

    The value of the ``.Upper`` suffix is numeric.

Dimension
---------

    The ``.Upper`` suffix has the same dimension and domain as that of the
    constraint or variable at hand.

.. note::

    -  When the ``.Lower`` suffix (see :ref:`.Lower`) of a variable is equal to
       the ``.Upper`` suffix of that variable this variable is treated as a
       frozen variable and subsequently removed from the generated
       mathematical program independently from the setting of the
       ``.nonvar`` suffix (see :doc:`optimization-modeling-components/variable-and-constraint-declaration/variable-declaration-and-attributes`).

    -  In order to access the upper bound of the definition of a variable
       ``X`` use the notation ``X_definition.Upper``.

    -  See also Sections :doc:`optimization-modeling-components/variable-and-constraint-declaration/variable-declaration-and-attributes` and :ref:`sec:constr.values` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.

    -  The ``GAMS`` and ``AIMMS 2`` equivalent suffix name is ``.up``.
