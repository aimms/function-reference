.. _.BestBound:

.BestBound
==========

Definition
----------

    The ``.BestBound`` suffix contains the current best bound during the
    branch-and-bound solution process of ``MIP``, ``MIQP`` and ``MIQCP``
    problems.

Datatype
--------

    The value of the ``.BestBound`` suffix is numeric.

.. note::

    -  The ``.BestBound`` suffix also contains the current best bound during a solve with BARON.

    -  The ``.BestBound`` suffix also contains the current best bound during the solve of a nonconvex
       QP problem with CPLEX, if the CPLEX option *Solution Target* is set to 'Search for global optimum'.

    -  The ``.BestBound`` suffix suffix also contains the current best bound during the solve of a
       QP, QCP, NLP or MINLP problem with GUROBI.

    -  For multi-objective models, the ``.BestBound`` suffix refers to the (blended) objective
       with the highest priority.

    -  The ``.BestBound`` suffix is also mentioned in Table :ref:`table:mp.suffix-mp.Solver` of the
       Language Reference.
