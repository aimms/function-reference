.. _.Objective:

.Objective
==========

Definition
----------

    The mathematical program suffix ``.Objective`` suffix contains the value
    of the objective at the end of the solve.

Datatype
--------

    The value of the ``.Objective`` suffix is numeric. When the solve is not
    successful or infeasible the value of the ``.Objective`` is ``NA``.

.. note::

    -  For multi-objective models, the ``.Objective`` suffix refers to the (blended) objective
       with the highest priority.

    -  The equivalent GAMS and AIMMS 2 name is ``.objval``.

    -  The ``.Objective`` suffix is also mentioned in Table :ref:`table:mp.suffix-mp.Solver`
       of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
