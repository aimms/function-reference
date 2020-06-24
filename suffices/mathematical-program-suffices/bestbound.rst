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

    -  The ``.BestBound`` suffix suffix also contains the current best bound during the solve of a nonconvex
       QP or QCP problem with GUROBI, if the GUROBI option *Nonconvex Strategy* is set to 'Translate'.

    -  The ``.BestBound`` suffix is also mentioned in Table 15.3 of the
       `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
