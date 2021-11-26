.. aimms:procedure:: GMP::Stochastic::MergeSolution(GMP, solution1, solution2, updObj)

.. _GMP::Stochastic::MergeSolution:

GMP::Stochastic::MergeSolution
==============================

The procedure :aimms:func:`GMP::Stochastic::MergeSolution` merges a solution of a
Benders problem into a solution of the stochastic mathematical program
belonging to the Benders problem. Only the level values of the columns
are merged. The objective level value is updated by using the objective
definition and the level values in the solution.

.. code-block:: aimms

    GMP::Stochastic::MergeSolution(
         GMP,            ! (input) a generated mathematical program
         solution1,      ! (input) a solution
         solution2,      ! (input) a solution
         [updObj]        ! (optional) a binary scalar value
    )

Arguments
---------

    *GMP*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

    *solution1*
        An integer scalar reference to a solution of *GMP*.

    *solution2*
        An integer scalar reference to a solution of the stochastic mathematical
        program that belongs to *GMP*.

    *updObj*
        A binary scalar indicating whether the (stochastic) objective value
        should be updated. Its default value is 1 which means that the objective
        is updated.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  The *GMP* should have been created by the function
       :aimms:func:`GMP::Stochastic::CreateBendersRootproblem` or by the function
       :aimms:func:`GMP::Stochastic::BendersFindReference`.

    -  It is most efficient to only update the objective value during the
       last call to :aimms:func:`GMP::Stochastic::MergeSolution`, i.e., set *updObj*
       to 1 for the last call and to 0 for all preceding calls.

.. seealso::

    The routines :aimms:func:`GMP::Instance::GenerateStochasticProgram`, :aimms:func:`GMP::Stochastic::CreateBendersRootproblem` and :aimms:func:`GMP::Stochastic::BendersFindReference`.
