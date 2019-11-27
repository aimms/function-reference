.. aimms:function:: GMP::Solution::IsPrimalDegenerated(GMP, solution)

.. _GMP::Solution::IsPrimalDegenerated:

GMP::Solution::IsPrimalDegenerated
==================================

The function :aimms:func:`GMP::Solution::IsPrimalDegenerated` checks whether the
solution for a generated mathematical program, with model type LP, RMIP
or QP, is primal degenerated.

.. code-block:: aimms

    GMP::Solution::IsPrimalDegenerated(
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

    The function returns 1 if the solution is primal degenerated, and 0
    otherwise.

.. note::

    -  A solution is primal degenerated if a basic variable is at a bound,
       or if a non-equality constraint is basic and at a bound. In that case
       the dual solution is not unique.

    -  This function will always return 0 if the barrier algorithm (without
       crossover) of CPLEX was used to solve the problem because the barrier
       algorithm (without crossover) of CPLEX does not provide a basic
       solution.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Solution::IsDualDegenerated` and :aimms:func:`GMP::Solution::RetrieveFromSolverSession`.
