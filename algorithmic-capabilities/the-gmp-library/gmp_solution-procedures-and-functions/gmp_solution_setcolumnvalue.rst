.. aimms:procedure:: GMP::Solution::SetColumnValue(GMP, solution, column, value, valueType)

.. _GMP::Solution::SetColumnValue:

GMP::Solution::SetColumnValue
=============================

| The procedure :aimms:func:`GMP::Solution::SetColumnValue` sets the level value,
  reduced cost, hint value or hint priority of a column in a solution in
  the solution repository of a generated mathematical program.
|
| Hint values and hint priorities can be used as follows: If you know
  that a variable is likely to take a particular value in high quality
  solutions of a MIP model, you can provide that value as a hint. You
  can also (optionally) provide a hint priority which resembles your
  level of confidence in a hint.

.. code-block:: aimms

    GMP::Solution::SetColumnValue(
         GMP,            ! (input) a generated mathematical program
         solution,       ! (input) a solution
         column,         ! (input) a scalar reference or column number
         value,          ! (input) a scalar value
         [valueType]     ! (input/optional) a scalar value
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *solution*
        An integer scalar reference to a solution.

    *column*
        A scalar reference to an existing column in the matrix or an element in the
        set :aimms:set:`Integers` in the range :math:`\{ 0 .. n-1 \}` where :math:`n` is the
        number of columns in the matrix.

    *value*
        The value to be assigned to the column.

    *valueType*
        A scalar value specifying the value type. If 0 (the default) then the
        level value will be set. If 1, the reduced cost. If 2, the hint value,
        and if 3 the hint priority.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  If the column has a unit then the scaled value should be passed. You
       can get the scale factor by using the function
       :aimms:func:`GMP::Column::GetScale`.

    -  Hint values and priorities are only supported by Gurobi.

Example
-------

Assume we have a GMP for which we have two solutions in the solution
repository at positions 1 and 2. Our goal is to add up the level values
of each column in the solutions, and place the result in the solution at
position 3 in the solution repository. This can be done in a generic way
using the function :aimms:func:`GMP::Instance::GetColumnNumbers` as follows. Here
``ColumnNrs`` is a subset of :aimms:set:`Integers` with index ``c``. 

.. code-block:: aimms

    ! Get the column numbers of all variables in myGMP.
    ColumnNrs := GMP::Instance::GetColumnNumbers( myGMP, AllVariables );

    for ( c ) do
        ! Get level value of column c in solution 1.
        val1 := GMP::Solution::GetColumnValue( myGMP, 1, c );
        ! Get level value of column c in solution 2.
        val2 := GMP::Solution::GetColumnValue( myGMP, 2, c );

        ! Assign the sum to column c in solution 3.
        GMP::Solution::SetColumnValue( myGMP, 3, c, val1 + val2 );
    endfor;

    ! Send solution 3 to the (symbolic) model identifiers.
    GMP::Solution::SendToModel( myGMP, 3 );

In
the next example, we use the current level values of the variable
``JobSchedule`` as variable hints: 

.. code-block:: aimms

    myGMP := GMP::Instance::Generate( FlowShopModel );

    for (j,s) do
        GMP::Solution::SetColumnValue( myGMP, 1, JobSchedule(j,s),
                                        JobSchedule(j,s).level, 2 );
        GMP::Solution::SetColumnValue( myGMP, 1, JobSchedule(j,s), 10, 3 );
    endfor;

    GMP::Instance::Solve( myGMP );

In this example the hint
priority for ``JobSchedule`` is set to 10.

.. seealso::

    The routines :aimms:func:`GMP::Column::GetScale`, :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::GetColumnNumbers`, :aimms:func:`GMP::Solution::GetColumnValue`, :aimms:func:`GMP::Solution::SendToModel` and
    :aimms:func:`GMP::Solution::SetRowValue`.
