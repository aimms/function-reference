.. aimms:function:: GMP::Solution::IsDualDegenerated(GMP, solution)

.. _GMP::Solution::IsDualDegenerated:

GMP::Solution::IsDualDegenerated
================================

The function :aimms:func:`GMP::Solution::IsDualDegenerated` checks whether the
solution for a generated mathematical program, with model type LP, RMIP
or QP, is dual degenerated.

.. code-block:: aimms

    GMP::Solution::IsDualDegenerated(
         GMP,            ! (input) a generated mathematical program
         solution        ! (input) a solution
         )

Arguments
---------

    *GMP*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

    *solution*
        An integer scalar reference to a solution.

Return Value
------------

    The function returns 1 if the solution is dual degenerated, and 0
    otherwise.

.. note::

    -  A solution is dual degenerated if a non-basic variable has a zero
       marginal, or if a non-equality constraint is non-basic and has a zero
       marginal. In that case the primal solution is not unique.

    -  This function will always return 0 if the barrier algorithm (without
       crossover) of CPLEX was used to solve the problem because the barrier
       algorithm (without crossover) of CPLEX does not provide a basic
       solution.

.. seealso::

    - The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Solution::IsPrimalDegenerated` and :aimms:func:`GMP::Solution::RetrieveFromSolverSession`.
