.. aimms:procedure:: GMP::Solution::SetRowValue(GMP, solution, row, value, valueType)

.. _GMP::Solution::SetRowValue:

GMP::Solution::SetRowValue
==========================

The procedure :aimms:func:`GMP::Solution::SetRowValue` sets the level value or
shadow price of a row in a solution in the solution repository of a
generated mathematical program.

.. code-block:: aimms

    GMP::Solution::SetRowValue(
         GMP,            ! (input) a generated mathematical program
         solution,       ! (input) a solution
         row,            ! (input) a scalar reference or row number
         value,          ! (input) a scalar value
         [valueType]     ! (input/optional) a scalar value
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *solution*
        An integer scalar reference to a solution.

    *row*
        A scalar reference to an existing row in the matrix or the number of
        that row in the range :math:`\{ 0 .. n-1 \}` where :math:`n` is the
        number of rows in the matrix.

    *value*
        The value to be assigned to the row.

    *valueType*
        A scalar value specifying the value type. If 0 (the default) then the
        level value will be set. If 1, the shadow price.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    If the row has a unit then the scaled value should be passed. You can
    get the scale factor by using the function ``GMP::Row::GetScale``.

Example
-------

    Assume we have a GMP for which we want to multiply all shadow prices in
    a solution by some value, say 10. This can be done in a generic way
    using the function ``GMP::Instance::GetRowNumbers`` as follows. Here
    ``RowNrs`` is a subset of :aimms:set:`Integers` with index ``r``. 

    .. code-block:: aimms

               ! Get the row numbers of all constraints in myGMP.
               RowNrs := GMP::Instance::GetRowNumbers( myGMP, AllConstraints );

               for ( r ) do
                   ! Get shadow price of row r in solution 1.
                   val := GMP::Solution::GetRowValue( myGMP, 1, r, valueType : 1 );

                   ! Assign new value for shadow price to row r in solution 1.
                   GMP::Solution::SetRowValue( myGMP, 1, r, 10 * val, valueType : 1 );
               endfor;

               ! Send solution to the (symbolic) model identifiers.
               GMP::Solution::SendToModel( myGMP, 1 );

    Note:
    the shadow prices will only be stored in the data structures of the
    constraints if the ``ShadowPrice`` property of the variables is set, or
    if the option ``Always_Store_Marginals`` is set.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::GetRowNumbers`, :aimms:func:`GMP::Row::GetScale`, :aimms:func:`GMP::Solution::GetRowValue`, :aimms:func:`GMP::Solution::SendToModel` and
    :aimms:func:`GMP::Solution::SetColumnValue`.
