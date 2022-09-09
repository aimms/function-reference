.. aimms:function:: GMP::Row::GetRightHandSide(GMP, row)

.. _GMP::Row::GetRightHandSide:

GMP::Row::GetRightHandSide
==========================

The function :aimms:func:`GMP::Row::GetRightHandSide` returns the right-hand-side
value of a row as present in the generated mathematical program.

.. code-block:: aimms

    GMP::Row::GetRightHandSide(
         GMP,            ! (input) a generated mathematical program
         row             ! (input) a scalar reference or row number
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *row*
        A scalar reference to an existing row in the matrix or the number of
        that row in the range :math:`\{ 0 .. m-1 \}` where :math:`m` is the
        number of rows in the matrix.

Return Value
------------

    The function returns the right-hand-side value of the specified row.

.. note::

    If the row has a unit then the scaled right-hand-side value is returned
    (without unit).

Example
-------

    Assume that 'c1' is a constraint in mathematical program 'MP' with a
    unit as defined by: 

    .. code-block:: aimms

               Quantity SI_Mass {
                   BaseUnit      :  kg;
                   Conversions   :  ton -> kg : # -> # * 1000;
               }
               Parameter wght {
                   Unit          :  ton;
                   InitialValue  :  20;
               }
               Constraint c1 {
                   Unit          :  ton;
                   Definition    :  -x1 + 2 * x2 <= wght;
               }

    If we want to multiply the
    right-hand-side value by 1.5 and assign it as the new value by using
    function :aimms:func:`GMP::Row::SetRightHandSide` we can use 

    .. code-block:: aimms

               rhs1 := 1.5 * (GMP::Row::GetRightHandSide( 'MP', c1 )) [ton];

               GMP::Row::SetRightHandSide( 'MP', c1, rhs1 );

    if 'rhs1'
    is a parameter with unit [ton], or we can use 

    .. code-block:: aimms

               rhs2 := 1.5 * GMP::Row::GetRightHandSide( 'MP', c1 );

               GMP::Row::SetRightHandSide( 'MP', c1, rhs2 * GMP::Row::GetScale( 'MP', c1 ) );

    if 'rhs2' is a
    parameter without a unit.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Row::SetRightHandSide`, :aimms:func:`GMP::Row::GetLeftHandSide` and :aimms:func:`GMP::Row::GetScale`.
