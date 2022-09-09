.. aimms:function:: GMP::Stochastic::GetObjectiveBound(GMP, solution)

.. _GMP::Stochastic::GetObjectiveBound:

GMP::Stochastic::GetObjectiveBound
==================================

The function :aimms:func:`GMP::Stochastic::GetObjectiveBound` returns the level
value of the column ``mp.SubproblemObjectiveBound`` in a solution of a
Benders problem, where ``mp`` denotes the corresponding symbolic
mathematical program.

.. code-block:: aimms

    GMP::Stochastic::GetObjectiveBound(
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

    In case of success, the level value. Otherwise it returns ``UNDF``.

.. note::

    -  The *GMP* should have been created by the function
       :aimms:func:`GMP::Stochastic::BendersFindReference`.

    -  Initially, the column ``mp.SubproblemObjectiveBound`` is not part of
       the Benders problem but it will be added if the procedure
       :aimms:func:`GMP::Stochastic::AddBendersOptimalityCut` is called.

.. seealso::

    The routines :aimms:func:`GMP::Instance::GenerateStochasticProgram`, :aimms:func:`GMP::Stochastic::AddBendersOptimalityCut` and :aimms:func:`GMP::Stochastic::BendersFindReference`.
