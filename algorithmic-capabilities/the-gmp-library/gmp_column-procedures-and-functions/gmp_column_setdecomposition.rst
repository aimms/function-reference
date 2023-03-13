.. aimms:procedure:: GMP::Column::SetDecomposition(GMP, column, value)

.. _GMP::Column::SetDecomposition:

GMP::Column::SetDecomposition
=============================

The procedure :aimms:func:`GMP::Column::SetDecomposition` can be used to specify
a decomposition to be used by a solver. It changes the decomposition
value of a single column in the generated mathematical program.

This procedure can be used to specify a decomposition for the Benders
algorithm in CPLEX by assigning the columns to the master problem or a
subproblem. It can also be used to specify a decompostion for
ODH-CPLEX. And it can be used to specify a partition for Gurobi to be
used by its partition heuristic.

.. code-block:: aimms

    GMP::Column::SetDecomposition(
         GMP,            ! (input) a generated mathematical program
         column,         ! (input) a scalar reference or column number
         value           ! (input) a numerical expression
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *column*
        A scalar reference to an existing column in the matrix or an element in the
        set :aimms:set:`Integers` in the range :math:`\{ 0 .. n-1 \}` where :math:`n` is the
        number of columns in the matrix.

    *value*
        The decomposition value assigned to the column.

Return Value
------------

    The procedure returns 1 on success, and 0 otherwise.

.. note::

    -  Use :aimms:func:`GMP::Column::SetDecompositionMulti` if the decomposition value of
       many columns corresponding to some variable have to be set, because
       that will be more efficient.

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
       partition heuristic of Gurobi. See the Gurobi option
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

               for (i) do
                   GMP::Column::SetDecomposition( myGMP, IntVar(i), 0 );
               endfor;

               for (j) do
                   GMP::Column::SetDecomposition( myGMP, ContVar(j), 1 );
               endfor;

               GMP::Instance::Solve( myGMP );

    The second example shows how to specify
    model structure used by ODH-CPLEX. All columns ``X(i,j)`` and
    ``Y(i,j,k)`` with the same ``i`` are assigned to the same
    subproblem. 

    .. code-block:: aimms

               myGMP := GMP::Instance::Generate( MP );

               for (i,j) do
                   GMP::Column::SetDecomposition( myGMP, X(i,j), Ord(i) );
               endfor;

               for (i,j,k) do
                   GMP::Column::SetDecomposition( myGMP, Y(i,j,k), Ord(i) );
               endfor;

               GMP::Instance::Solve( myGMP );

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::Solve` and :aimms:func:`GMP::Column::SetDecompositionMulti`.
