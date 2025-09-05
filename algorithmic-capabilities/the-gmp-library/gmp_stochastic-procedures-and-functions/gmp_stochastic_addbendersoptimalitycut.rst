.. aimms:procedure:: GMP::Stochastic::AddBendersOptimalityCut(GMP, solution, cutNo)

.. _GMP::Stochastic::AddBendersOptimalityCut:

GMP::Stochastic::AddBendersOptimalityCut
========================================

The procedure :aimms:func:`GMP::Stochastic::AddBendersOptimalityCut` adds a
Benders optimality cut to the parent of a Benders problem by using the
dual information from a solution of the Benders problem.

.. code-block:: aimms

    GMP::Stochastic::AddBendersOptimalityCut(
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

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  The *GMP* should have been created by the function
       :aimms:func:`GMP::Stochastic::BendersFindReference`.

    -  By using the suffix ``.SubproblemOptimalityCuts`` of the associated
       symbolic mathematical program it is possible to refer to the row that
       is added by :aimms:func:`GMP::Stochastic::AddBendersOptimalityCut`. Let
       ``gmpBen`` be a Benders problem corresponding to the symbolic
       mathematical program ``mp``. Then the row
       ``mp.SubproblemOptimalityCuts(gmpBen,lbl)`` is added to the *GMP*,
       where ``lbl`` is an element in the set :aimms:set:`AllGMPExtensions` created by this
       procedure using *cutNo*.

    -  The first time this procedure is called for a Benders problem a new
       column ``mp.SubproblemObjectiveBound(gmpBen)`` is added to the parent
       of the Benders problem. For this column a coefficient equal to the
       relative weight of the Benders problem will be added to the objective
       of the parent. For this column a coefficient of 1 is added to the
       optimality cut.

.. seealso::

    - :aimms:func:`GMP::Instance::GenerateStochasticProgram`.
    - :aimms:func:`GMP::Stochastic::AddBendersFeasibilityCut`.
    - :aimms:func:`GMP::Stochastic::BendersFindReference`.
    - :aimms:func:`GMP::Stochastic::GetObjectiveBound`.
    - :aimms:func:`GMP::Stochastic::GetRelativeWeight`.
