.. aimms:function:: GMP::Stochastic::BendersFindFeasibilityReference(GMP, stage, scenario)

.. _GMP::Stochastic::BendersFindFeasibilityReference:

GMP::Stochastic::BendersFindFeasibilityReference
================================================

The function :aimms:func:`GMP::Stochastic::BendersFindFeasibilityReference`
returns the reference to the (feasibility) generated math program
belonging to a node in the scenario tree. This generated math program
represents the Benders feasibility problem for a stage and for some
representive scenario in the scenario tree of a stochastic mathematical
program.

.. code-block:: aimms

    GMP::Stochastic::BendersFindFeasibilityReference(
         GMP,               ! (input) a generated mathematical program
         stage,             ! (input) a scalar reference
         scenario           ! (input) a scenario
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

    An element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

.. note::

    -  The function :aimms:func:`GMP::Stochastic::CreateBendersRootproblem` creates
       all Benders feasibility problems for all nodes in the scenario tree,
       and must be called before calling
       :aimms:func:`GMP::Stochastic::BendersFindReference`.

    -  The *GMP* should correspond to a root node, i.e., be created by using
       the function :aimms:func:`GMP::Stochastic::CreateBendersRootproblem`.

.. seealso::

    - :aimms:func:`GMP::Instance::GenerateStochasticProgram`. 
    - :aimms:func:`GMP::Stochastic::BendersFindReference`. 
    - :aimms:func:`GMP::Stochastic::CreateBendersRootproblem`.
