.. aimms:procedure:: GMP::Column::SetAsMultiObjective(GMP, column, priority, weight, abstol, reltol)

.. _GMP::Column::SetAsMultiObjective:

GMP::Column::SetAsMultiObjective
================================

The procedure :aimms:func:`GMP::Column::SetAsMultiObjective` sets a column as one
of the multi-objectives of a generated mathematical program, thereby
creating a multi-objective optimization problem.

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
        A scalar reference to an existing column in the matrix or the number of
        that column in the range :math:`\{ 0 .. n-1 \}` where :math:`n` is the
        number of columns in the matrix.

    *priority*
        A scalar value specifying the priority of the objective. An objective
        with the highest priority is considered first.

    *weight*
        A scalar value specifying the weight of the objective. It defines the
        weight by which the objective coefficients are multiplied when forming a
        blended objective, i.e., if multiple objectives have the same priority.

    *abstol*
        A scalar value specifying the absolute tolerance by which a solution may
        deviate from the optimal value of the objective of the previous
        optimization problem. The default value is 0.0.

    *reltol*
        A scalar value specifying the relative tolerance by which a solution may
        deviate from the optimal value of the objective of the previous
        optimization problem. The default value is 0.0.

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

    -  Use the procedure ``GMP::Instance::DeleteMultiObjectives`` to delete
       all multi-objectives.

    -  Multi-objective optimization is only supported by CPLEX 12.9 or
       higher, and GUROBI 8.0 or higher.

    -  The meaning of the relaxation of the objective, which is controlled
       by the *abstol* and *reltol* arguments, depends on whether the
       multi-objective problem is an LP or MIP. See the Multi-Objective
       Optimization section in the CPLEX Help or the GUROBI Help for more
       information.

Example
-------

    In the example below two multi-objectives are specified:: 

    .. code-block:: aimms

               myGMP := GMP::Instance::Generate( MP );

               GMP::Column::SetAsMultiObjective( myGMP, TotalDist, 2, 1.0, 0, 0.1 );
               GMP::Column::SetAsMultiObjective( myGMP, TotalTime, 1, 1.0, 0, 0.0 );

               GMP::Instance::Solve( myGMP );

    We
    can now switch the priorities of the two objectives by adding:

    .. code-block:: aimms

               GMP::Column::SetAsMultiObjective( myGMP, TotalDist, 1, 1.0, 0, 0.1 );
               GMP::Column::SetAsMultiObjective( myGMP, TotalTime, 2, 1.0, 0, 0.0 );

               GMP::Instance::Solve( myGMP );

.. seealso::

    The procedure :aimms:func:`GMP::Instance::DeleteMultiObjectives`.
