.. aimms:procedure:: GMP::Column::SetAsMultiObjective(GMP, column, priority, weight, abstol, reltol)

.. _GMP::Column::SetAsMultiObjective:

GMP::Column::SetAsMultiObjective
================================

| The procedure :aimms:func:`GMP::Column::SetAsMultiObjective` sets a column as one
  of the multi-objectives of a generated mathematical program, thereby
  creating a multi-objective optimization problem.
|
| Lexicographic (or hierarchical) multi-objective optimization will optimize for the
  different objectives in the mathematical program one step at a time, in priority order.

.. code-block:: aimms

    GMP::Column::SetAsMultiObjective(
         GMP,            ! (input) a generated mathematical program
         column,         ! (input) a scalar reference or column number
         priority,       ! (input) a numerical expression
         weight,         ! (input) a numerical expression
         [abstol],       ! (input/optional) a numerical expression
         [reltol]        ! (input/optional) a numerical expression
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *column*
        A scalar reference to an existing column in the matrix or an element in the
        set :aimms:set:`Integers` in the range :math:`\{ 0 .. n-1 \}` where :math:`n` is the
        number of columns in the matrix.

    *priority*
        A scalar value specifying the priority of the objective. An objective
        with the highest priority is considered first.

    *weight*
        A scalar value specifying the weight of the objective. It defines the
        weight by which the objective coefficients are multiplied when forming a
        blended objective, i.e., if multiple objectives have the same priority.

    *abstol*
        A scalar value specifying the absolute tolerance. In subsequent steps
        (for objectives with a lower priority) the solution value of *column*
        may deviate from the optimized value of *column*, as calculated in this step,
        using this absolute tolerance. The default value is 0.0.

    *reltol*
        A scalar value specifying the relative tolerance. In subsequent steps
        (for objectives with a lower priority) the solution value of *column*
        may deviate from the optimized value of *column*, as calculated in this step,
        using this relative tolerance. The default value is 0.0.

Return Value
------------

    The procedure returns 1 on success, and 0 otherwise.

.. note::

    -  The column should be linear and have at exactly one coefficient in
       the matrix.

    -  The column should be free, i.e., not have a lower or upper bound.

    -  If :aimms:func:`GMP::Column::SetAsMultiObjective` is called twice for the same
       column then only the information from the second call is used (and
       the information from the first call is ignored).

    -  Use the procedure :aimms:func:`GMP::Instance::DeleteMultiObjectives` to delete
       all multi-objectives.

    -  Multi-objective optimization is only supported by CPLEX and Gurobi.
    
    -  If you specify :math:`n` different priorities then CPLEX or Gurobi will
       optimize the mathematical program :math:`n` times using different
       objectives (in priority order).

    -  CPLEX and Gurobi allow you to use different option settings for each optimization round
       by using parameter files. See the option ``Read Parameter File`` in the CPLEX Help
       or the Gurobi Help for more information.
    
    -  Multi-objective optimization is not supported for generated mathematical programs
       created by one of the following functions:

       -  GMP::Instance::GenerateRobustCounterpart,
       
       -  GMP::Instance::GenerateStochasticProgram,
       
       -  GMP::Instance::CreatePresolved,
       
       -  GMP::Instance::CreateDual, or
       
       -  GMP::Instance::CreateMasterMIP.

    -  The meaning of the relaxation of the objective, which is controlled
       by the *abstol* and *reltol* arguments, depends on whether the
       multi-objective problem is an LP or MIP. See the Multi-Objective
       Optimization section in the CPLEX Help or the Gurobi Help for more
       information.

    -  The *abstol* and *reltol* arguments are meaningless for the objective(s) with the
       lowest priority.

Example
-------

In the example below two multi-objectives are specified:

.. code-block:: aimms

    myGMP := GMP::Instance::Generate( MP );

    GMP::Column::SetAsMultiObjective( myGMP, TotalDist, 2, 1.0, 0, 0.1 );
    GMP::Column::SetAsMultiObjective( myGMP, TotalTime, 1, 1.0, 0, 0.0 );

    GMP::Instance::Solve( myGMP );

We can now switch the priorities of the two objectives by adding:

.. code-block:: aimms

    GMP::Column::SetAsMultiObjective( myGMP, TotalDist, 1, 1.0, 0, 0.1 );
    GMP::Column::SetAsMultiObjective( myGMP, TotalTime, 2, 1.0, 0, 0.0 );

    GMP::Instance::Solve( myGMP );

.. seealso::

    The procedure :aimms:func:`GMP::Instance::DeleteMultiObjectives`.

