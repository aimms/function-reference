.. aimms:function:: GMP::Solution::GetBestBound(GMP, solution)

.. _GMP::Solution::GetBestBound:

GMP::Solution::GetBestBound
===========================

The function :aimms:func:`GMP::Solution::GetBestBound` returns the the best known
bound on a solution.

.. code-block:: aimms

    GMP::Solution::GetBestBound(
         GMP,            ! (input) a generated mathematical program
         solution        ! (input) a solution
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *solution*
        An integer scalar reference to a solution.

Return Value
------------

    In case of success, the best known bound. Otherwise it returns ``UNDF``.

.. note::

    -  This function can be used for GMPs with model type MIP, MIQP or MIQCP.

    -  This function can also be used for GMPs solved with BARON,
       regardless of the model type.

    -  This function can also be used for GMPs with model type QP that are
       solved with CPLEX, if the CPLEX option *Solution Target* is set to
       'Search for global optimum'.

    -  This function can also be used for GMPs with model type QP or QCP that are
       solved with GUROBI, if the GUROBI option *Nonconvex Strategy*
       is set to 'Translate'.

    -  For multi-objective models, the best bound refers to the (blended) objective
       with the highest priority.

.. seealso::

    - The procedure :aimms:func:`GMP::Solution::GetObjective`.
