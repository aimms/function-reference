.. aimms:function:: GMP::Instance::GenerateStochasticProgram(MP, StochasticParameters, StochasticVariables, Scenarios, ScenarioProbability, ScenarioTreeMap, RootScenarioName, GenerationMode, Name)

.. _GMP::Instance::GenerateStochasticProgram:

GMP::Instance::GenerateStochasticProgram
========================================

The function :aimms:func:`GMP::Instance::GenerateStochasticProgram` generates the
deterministic equivalent of a stochastic mathematical program.

.. code-block:: aimms

    GMP::Instance::GenerateStochasticProgram(
         MP,                    ! (input) a symbolic mathematical program
         StochasticParameters,  ! (input) a set of stochastic parameters
         StochasticVariables,   ! (input) a set of stochastic variables
         Scenarios,             ! (input) a set of stochastic scenarios
         ScenarioProbability,   ! (input) a double parameter
         ScenarioTreeMap,       ! (input) an element parameter
         RootScenarioName,      ! (input) a string expression
         [GenerationMode],      ! (optional) a stochatic generation mode
         [Name]                 ! (optional) a string expression
    )

Arguments
---------

    *MP*
        A symbolic mathematical program in the set :aimms:set:`AllMathematicalPrograms`. The mathematical
        program should have model type ``LP`` or ``MIP``.

    *StochasticParameters*
        A subset of :aimms:set:`AllStochasticParameters`.

    *StochasticVariables*
        A subset of :aimms:set:`AllStochasticVariables`.

    *Scenarios*
        A subset of :aimms:set:`AllStochasticScenarios`.

    *ScenarioProbability*
        A double parameter over ``Scenarios`` representing the objective
        probabilities of the scenarios.

    *ScenarioTreeMap*
        An element parameter that defines the scenario-and-stage to scenario
        mapping. The range of this parameter should be the set ``Scenarios``.

    *RootScenarioName*
        A string that holds the name of the artificial element that will be
        added to the set :aimms:set:`AllStochasticScenarios`. This element will be used to store the
        solution of non-stochastic variables in their respective ``.Stochastic``
        suffixes.

    *GenerationMode*
        An element in the predefined set :aimms:set:`AllStochasticGenerationModes`. The default is
        '\ ``SubstituteStochasticVariables``\ '.

    *Name*
        A string that holds the name for the generated stochastic mathematical
        program.

Return Value
------------

    A new element in the set :aimms:set:`AllGeneratedMathematicalPrograms` with the name as specified by the
    *name* argument.

.. note::

    -  If the *Name* argument is not specified, or if it is the empty
       string, then the name of the symbolic mathematical program preceded
       by 'Stochastic' is used to create a new element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

    -  The objective of the symbolic mathematical program must be a defined
       variable.

.. seealso::

    -  Stochastic programming is discussed in :doc:`optimization-modeling-components/stochastic-programming/index` of the Language
       Reference.

    -  The procedure :aimms:func:`GMP::Instance::Solve`.
