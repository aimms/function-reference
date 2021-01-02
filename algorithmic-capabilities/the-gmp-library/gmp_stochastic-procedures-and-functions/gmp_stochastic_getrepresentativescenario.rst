.. aimms:function:: GMP::Stochastic::GetRepresentativeScenario(GMP, stage, scenario)

.. _GMP::Stochastic::GetRepresentativeScenario:

GMP::Stochastic::GetRepresentativeScenario
==========================================

The function :aimms:func:`GMP::Stochastic::GetRepresentativeScenario` returns the
representive scenario of a scenario at some stage in the scenario tree
belonging to a stochastic mathematical program.

.. code-block:: aimms

    GMP::Stochastic::GetRepresentativeScenario(
         GMP,            ! (input) a generated mathematical program
         stage,          ! (input) a scalar reference
         scenario        ! (input) a scenario
    )

Arguments
---------

    *GMP*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

    *stage*
        An integer scalar reference to a stage.

    *scenario*
        An element in the set :aimms:set:`AllStochasticScenarios`.

Return Value
------------

    An element in the set :aimms:set:`AllStochasticScenarios`.

.. note::

    The *GMP* should have been created by the function
    ``GMP::Instance::GenerateStochasticProgram``.

.. seealso::

    The routines :aimms:func:`GMP::Instance::GenerateStochasticProgram` and :aimms:func:`GMP::Stochastic::GetRelativeWeight`. See :doc:`optimization-modeling-components/robust-optimization/basic-concepts` of the Language
    Reference for more details on scenario tree, scenarios and stages.
