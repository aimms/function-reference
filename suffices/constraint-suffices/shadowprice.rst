.. _.ShadowPrice:

.ShadowPrice
============

Definition
----------

    When the property ``ShadowPrice`` of a contraint is set or when the
    option ``Always_store_marginals`` is set to ``on``, the ``.ShadowPrice``
    suffix contains the shadow price of the constraint as computed by the
    solver. The shadow price of a constraint is the marginal change in the
    objective value with respect to a change in the right-hand side of the
    constraint.

Datatype
--------

    The value of the ``.ShadowPrice`` suffix is numeric.

Dimension
---------

    The ``.ShadowPrice`` suffix has the same dimension and domain as that of
    the constraint at hand.

.. note::

    -  When a variable ``X`` has a definition the suffix can also be applied
       to ``X`` but this is not encouraged by the syntax highlighting. The
       preferred notation is ``X_definition.ShadowPrice``.

    -  The GAMS equivalent suffix name is ``.m``.

    -  The default of the option ``Always_store_basics`` is ``off``.

    -  See also Section 14.2 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
