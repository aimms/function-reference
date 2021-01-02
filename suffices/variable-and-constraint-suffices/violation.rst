.. _.Violation:

.Violation
==========

Definition
----------

    The ``.Violation`` suffix of a variable contains the amount by which one
    of the bounds of that variable is violated. The ``.Violation`` suffix of
    a constraint contains the amount by which the definition of that
    constraint is violated.

Datatype
--------

    The value of the ``.Violation`` suffix is numeric.

Dimension
---------

    The ``.Violation`` suffix has the same dimension and domain as that of
    the constraint or variable at hand.

.. note::

    -  When a variable ``X`` has a definition the suffix
       ``.DefinitionViolation`` can be used to obtain the violation of the
       defining constraint of ``X``. An alternative is to use
       ``X_definition.Violation``.

    -  See also :ref:`sec:mp.infeas.inspect` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__ and :ref:`.DefinitionViolation`.
