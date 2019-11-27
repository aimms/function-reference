.. _.tolinfrep:

.tolinfrep
==========

Definition
----------

    When specified, the suffix ``.tolinfrep`` is the tolerance on row
    feasibility when computing the values of the suffixes
    ``.NumberOfInfeasibilities`` and ``.SumOfInfeasibilities``. When
    specified the option ``.tolinfrep`` overrides the option
    ``bound_tolerance``.

Datatype
--------

    The value of the ``.tolinfrep`` suffix is numeric.

.. note::

    -  The suffix ``.tolinfrep`` is initialized to ``NA``. AIMMS considers
       it specified when its value is not equal to ``NA``.
