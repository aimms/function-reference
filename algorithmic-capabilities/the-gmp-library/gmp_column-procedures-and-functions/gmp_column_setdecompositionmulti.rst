.. aimms:procedure:: GMP::Column::SetDecompositionMulti(GMP, binding, column, value)

.. _GMP::Column::SetDecompositionMulti:

GMP::Column::SetDecompositionMulti
==================================

The procedure :aimms:func:`GMP::Column::SetDecompositionMulti` can be used to
specify a decomposition to be used by a solver. It changes the
decomposition value of a group of columns, belonging to a variable, in
the generated mathematical program.

This procedure can be used to specify a decomposition for the Benders
algorithm in CPLEX by assigning the columns to the master problem or a
subproblem. It can also be used to specify a decompostion for
ODH-CPLEX. And it can be used to specify a partition for Gurobi to be
used by its partition heuristic.

.. code-block:: aimms

    GMP::Column::SetDecompositionMulti(
         GMP,            ! (input) a generated mathematical program
         binding,        ! (input) an index binding
         column,         ! (input) a scalar reference or column number
         value           ! (input) a numerical expression
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *binding*
        An index binding that specifies and possibly limits the scope of
        indices.

    *column*
        A variable that, combined with the *binding* domain, specifies the
        columns.

    *value*
        The new decomposition value for each column, defined over the binding
        domain *binding*.

Return Value
------------

    The procedure returns 1 on success, and 0 otherwise.

.. note::

    -  This procedure can be used to specify the decomposition in the
       Benders algorithm of CPLEX. See the CPLEX option
       ``Benders strategy`` for more information.

    -  For CPLEX, use a value of 0 to assign a column to the master problem,
       and a value between 1 and :math:`N` to assign a column to one of the
       :math:`N` subproblems (:math:`N` can be 1 if you only want to use one
       subproblem). A value of -1 indicates that the column is not assigned
       to the master problem or a subproblem.

    -  This procedure can be used to specify model structure or a
       decomposition used by ODH-CPLEX.

    -  For ODH-CPLEX, use a value between 1 and :math:`N` to assign a column
       to one of the :math:`N` subproblems. A value of 0 or lower indicates
       that the column is not assigned to any subproblem.

    -  This procedure can be used to specify a partition used by the
       partition heuristic of Gurobi 8.0 or higher. See the Gurobi option
       ``Partition heuristic`` for more information.

    -  For Gurobi, use a positive value to indicate that the column should
       be included when the correspondingly numbered sub-MIP is solved, a
       value of 0 to indicate that the column should be included in every
       sub-MIP, and a value of -1 to indicate that the column should not be
       included in any sub-MIP. (Variables that are not included in the
       sub-MIP are fixed to their values in the current incumbent solution.)

    -  This procedure is **not** used by the Automatic Benders' Decomposition module in AIMMS.

Example
-------

    The first example shows how to specify a decomposition for the Benders
    algorithm in CPLEX. The integer variable ``IntVar`` is assigned to the
    master problem while the continuous variable ``ContVar`` is assigned to
    the subproblem. 

    .. code-block:: aimms

               myGMP := GMP::Instance::Generate( MP );

               ! Switch on CPLEX option for using Benders strategy with decomposition specified by user. 
               GMP::Instance::SetOptionValue( myGMP, 'benders strategy', 1 );

               GMP::Column::SetDecompositionMulti( myGMP, i, IntVar(i), 0 );

               GMP::Column::SetDecompositionMulti( myGMP, j, ContVar(j), 1 );

               GMP::Instance::Solve( myGMP );

    The second example shows how to specify
    model structure used by ODH-CPLEX. All columns ``X(i,j)`` and
    ``Y(i,j,k)`` with the same ``i`` are assigned to the same
    subproblem. 

    .. code-block:: aimms

               myGMP := GMP::Instance::Generate( MP );

               GMP::Column::SetDecompositionMulti( myGMP, (i,j), X(i,j), Ord(i) );

               GMP::Column::SetDecompositionMulti( myGMP, (i,j,k), Y(i,j,k), Ord(i) );

               GMP::Instance::Solve( myGMP );

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::Solve` and :aimms:func:`GMP::Column::SetDecomposition`.
