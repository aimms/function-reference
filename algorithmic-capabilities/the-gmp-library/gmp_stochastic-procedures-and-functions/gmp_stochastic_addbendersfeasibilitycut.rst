.. aimms:procedure:: GMP::Stochastic::AddBendersFeasibilityCut(GMP, solution, cutNo)

.. _GMP::Stochastic::AddBendersFeasibilityCut:

GMP::Stochastic::AddBendersFeasibilityCut
=========================================

The procedure :aimms:func:`GMP::Stochastic::AddBendersFeasibilityCut` adds a
Benders feasibility cut to the parent of a Benders feasibility problem.
(The parent of a Benders feasibility problem is the parent of the
corresponding Benders problem.) It uses the dual information from a
solution of the Benders feasibility problem.

.. code-block:: aimms

    GMP::Stochastic::AddBendersFeasibilityCut(
         GMP,            ! (input) a generated mathematical program
         solution,       ! (input) a solution
         cutNo           ! (input) a scalar reference
    )

Arguments
---------

    *GMP*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

    *solution*
        An integer scalar reference to a solution.

    *cutNo*
        An integer scalar reference to a cut number.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise..

.. note::

    -  The *GMP* should have been created by the function
       :aimms:func:`GMP::Stochastic::CreateBendersFeasibilitySubproblem`.

    -  By using the suffix ``.SubproblemFeasibilityCuts`` of the associated
       symbolic mathematical program it is possible to refer to the row that
       is added by :aimms:func:`GMP::Stochastic::AddBendersFeasibilityCut`. Let
       ``gmpBen`` be a Benders problem corresponding to the symbolic
       mathematical program ``mp``. Then the row
       ``mp.SubproblemFeasibilityCuts(gmpBen,lbl)`` is added to the *GMP*,
       where ``lbl`` is an element in the set :aimms:set:`AllGMPExtensions` created by this
       procedure using *cutNo*.

.. seealso::

    The routines :aimms:func:`GMP::Instance::GenerateStochasticProgram`, :aimms:func:`GMP::Stochastic::AddBendersOptimalityCut`, :aimms:func:`GMP::Stochastic::CreateBendersFeasibilitySubproblem` and :aimms:func:`GMP::Stochastic::BendersFindReference`.
