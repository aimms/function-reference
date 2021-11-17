.. aimms:procedure:: GMP::Stochastic::UpdateBendersSubproblem(GMP, solution)

.. _GMP::Stochastic::UpdateBendersSubproblem:

GMP::Stochastic::UpdateBendersSubproblem
========================================

The procedure :aimms:func:`GMP::Stochastic::UpdateBendersSubproblem` updates the
right hand side values of a Benders problem by using a solution of the
parent Benders problem.

.. code-block:: aimms

    GMP::Stochastic::UpdateBendersSubproblem(
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

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  The *GMP* should have been created by the function
       :aimms:func:`GMP::Stochastic::CreateBendersRootproblem` or obtained by the
       function :aimms:func:`GMP::Stochastic::BendersFindReference`.

    -  This procedure does not use the *solution* if the *GMP* belongs to
       the Benders problem at (the unique node at) stage 1, i.e., if it was
       created by the function
       :aimms:func:`GMP::Stochastic::CreateBendersRootproblem`.

.. seealso::

    The routines :aimms:func:`GMP::Instance::GenerateStochasticProgram`, :aimms:func:`GMP::Stochastic::BendersFindReference` and :aimms:func:`GMP::Stochastic::CreateBendersRootproblem`.
