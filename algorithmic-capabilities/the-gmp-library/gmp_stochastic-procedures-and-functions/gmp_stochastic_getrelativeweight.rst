.. aimms:function:: GMP::Stochastic::GetRelativeWeight(GMP, stage, scenario)

.. _GMP::Stochastic::GetRelativeWeight:

GMP::Stochastic::GetRelativeWeight
==================================

The function :aimms:func:`GMP::Stochastic::GetRelativeWeight` returns the relative
weight of a scenario at some stage in the scenario tree belonging to a
stochastic mathematical program. The weight is relative to the sum of
the weights of all scenarios that have the same parent at that stage.

.. code-block:: aimms

    GMP::Stochastic::GetRelativeWeight(
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

    In case of success, the relative weight. Otherwise it returns ``UNDF``.

.. note::

    The *GMP* should have been created by the function
    :aimms:func:`GMP::Instance::GenerateStochasticProgram`.

.. seealso::

    The routines :aimms:func:`GMP::Instance::GenerateStochasticProgram` and :aimms:func:`GMP::Stochastic::GetRepresentativeScenario`. See :doc:`optimization-modeling-components/robust-optimization/basic-concepts` of the Language
    Reference for more details on scenario tree, scenarios and stages.
