.. _.SolutionTime:

.SolutionTime
=============

Definition
----------

    The mathematical program suffix ``.SolutionTime`` contains the time
    required to solve the mathematical program.

Datatype
--------

    The value of the ``.SolutionTime`` suffix is numeric.

.. note::

    -  The suffix ``.SolutionTime`` has unit [second] iff (1) this unit has
       been declared, and (2) the option ``solution_time_has_unit_seconds``
       is kept to its default of ``on``. In all other cases the suffix has
       no unit.

    -  The GAMS and AIMMS 2 equivalent name is ``.resusd``.

    -  The ``.SolutionTime`` suffix is also mentioned in Table :ref:`table:mp.suffix-mp.Solver`
       of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
