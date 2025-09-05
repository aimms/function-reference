.. aimms:procedure:: GMP::Instance::AddLimitBinaryDeviationRow(GMP, solution, varSet, deviation, refNo)

.. _GMP::Instance::AddLimitBinaryDeviationRow:

GMP::Instance::AddLimitBinaryDeviationRow
=========================================

The procedure :aimms:func:`GMP::Instance::AddLimitBinaryDeviationRow` adds a row to a GMP that sets a
limit on the number of binary columns, from a given set of variables, of which the solution value is allowed
to vary.

A scenario in which the procedure could be used is the following. Imagine you have created a production
plan based on optimizing some mathematical program and that something unexpected
happened that (partly) ruined the plan. You now have to re-optimize the mathematical program, with some
changes, but would like the solution of the new optimization to be close to the previous one.

.. code-block:: aimms

    GMP::Instance::AddLimitBinaryDeviationRow(
         GMP,          ! (input) a generated mathematical program
         solution,     ! (input) a solution
         variableSet,  ! (input) a reference number
         deviation,    ! (input) a scalar integer value
         [refNo]       ! (optional, default 1) a scalar integer value
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *solution*
        An integer scalar reference to a solution.

    *variableSet*
        A subset of :aimms:set:`AllVariables`.

    *deviation*
        A nonnegative integer scalar value representing the total number of binary variables that are allowed to deviate.

    *refNo*
        A positive integer scalar value representing a reference number. The default is 1.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  This procedure will fail if *variableSet* contains no binary variable.
    
    -  Non-binary variables in the *variableSet* will be ignored. It is therefore possible
       to pass :aimms:set:`AllVariables` as the *variableSet* (provided that the mathematical
       program contains a least one binary variable).

    -  A row added before for *refNo* will be deleted first.

    -  Every call to :aimms:func:`GMP::Instance::AddLimitBinaryDeviationRow`
       adds the following row:

       .. math::
          \begin{aligned}
           \sum_{i\in S_{0}} x_i - \sum_{i\in S_{1}} x_i \leq d - |S_{1}|  \end{aligned}

       \ where :math:`S_{0}` defines the set of binary columns whose level
       values equals 0, :math:`S_{1}` the set of binary columns whose
       level values equals 1 and :math:`d` the *deviation* value.

    -  By using the suffix ``.ExtendedConstraint`` it is possible to refer to the row
       added by :aimms:func:`GMP::Instance::AddLimitBinaryDeviationRow`. The
       constraint ``mp.ExtendedConstraint('Deviation``\ *k*\ ``')``,
       where ``mp`` denotes the symbolic mathematical program, is added
       for every call to this procedure.
       Here :math:`k` denotes the value of the argument *refNo*.

Example
-------

Assume that ``MP`` is a mathematical program containing the binary variables ``x(i)`` and
``y(j)``. Furthermore, we have solved this mathematical program and found a solution but
now we want to resolve the mathematical program after we made some changes in the data,
resulting in a different generated mathematical program. However, we want to enforce
that the solution variables of the binary variables in the second solve does not change
much compared to the first solve. This can be achieved using the procedure
:aimms:func:`GMP::Instance::AddLimitBinaryDeviationRow`.

To use this procedure we declare the following identifiers (in ams format):

.. code-block:: aimms

    ElementParameter myGMP {
        Range: AllGeneratedMathematicalPrograms;
    }
    Set VarSet {
        SubsetOf: AllIntegerVariables;
    }

If we want to enforce that at most 4 of the ``x(i)`` and ``y(j)`` variables can get different
solution values compared to the first solve then we could use:

.. code-block:: aimms

    myGMP := GMP::Instance::Generate(MP);
    
    GMP::Solution::RetrieveFromModel( myGMP, 1 );

    VarSet := { 'x', 'y' };
    GMP::Instance::AddLimitBinaryDeviationRow( myGMP, 1, varSet, 4, 1 );

    GMP::Instance::Solve( myGMP );

After executing this code, it could be that all ``x(i)`` variables get
the same solution values as before and that 4 of the ``y(j)`` variables get different
solution values. If we also want to add the restriction that at most 3 of the ``y(j)`` variables
get different solution values then we should use:

.. code-block:: aimms

    myGMP := GMP::Instance::Generate(MP);
    
    GMP::Solution::RetrieveFromModel( myGMP, 1 );

    VarSet := { 'x', 'y' };
    GMP::Instance::AddLimitBinaryDeviationRow( myGMP, 1, varSet, 4, 1 );
    VarSet := { 'y' };
    GMP::Instance::AddLimitBinaryDeviationRow( myGMP, 1, varSet, 3, 2 );

    GMP::Instance::Solve( myGMP );

.. seealso::

    - The routines :aimms:func:`GMP::Instance::DeleteIntegerEliminationRows`. 
    - See :ref:`sec:matrix.extended` of the Language Reference for more details on extended suffixes.
