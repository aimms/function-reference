.. _.optca:

.optca
======

Definition
----------

    When specified, the solution process stops if the solver can guarantee
    that the current best solution is within the value of suffix ``optca``
    of the global optimum. This is only valid for mixed integer programming
    models including mixed integer quadratic problems. When specified the
    suffix ``.optca`` overrides the option
    ``MIP_Absolute_Optimality_Tolerance``.

Datatype
--------

    The value of the ``.optca`` suffix is numeric.

.. note::

    -  The suffix ``.optca`` is initialized to ``NA``. AIMMS considers it
       specified when its value is not equal to ``NA``.
