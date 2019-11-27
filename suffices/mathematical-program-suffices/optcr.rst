.. _.optcr:

.optcr
======

Definition
----------

    When specified the solution procedure stops if the solver can guarantee
    that the current best solution is within suffix ``.optcr`` of the global
    optimum. This is only valid for mixed integer programming models
    including mixed integer quadratic problems. The ``.optcr`` suffix
    controls the append mode of the file. When specified the suffix
    ``.optcr`` overwrites the option ``MIP_Relative_Optimality_Tolerance``

Datatype
--------

    The value of the ``.optcr`` suffix is numeric.

.. note::

    -  The suffix ``.optcr`` is initialized to ``NA``. AIMMS considers it
       specified when its value is not equal to ``NA``.
