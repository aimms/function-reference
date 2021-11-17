.. aimms:procedure:: GMP::Row::SetRightHandSide(GMP, row, value)

.. _GMP::Row::SetRightHandSide:

GMP::Row::SetRightHandSide
==========================

The procedure :aimms:func:`GMP::Row::SetRightHandSide` changes the right-hand-side
of a row in a generated mathematical program.

.. code-block:: aimms

    GMP::Row::SetRightHandSide(
         GMP,            ! (input) a generated mathematical program
         row,            ! (input) a scalar reference or row number
         value           ! (input) a numerical expression
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *row*
        A scalar reference to an existing row in the matrix or the number of
        that row in the range :math:`\{ 0 .. m-1 \}` where :math:`m` is the
        number of rows in the matrix.

    *value*
        The new value that should be assigned to the right-hand-side of the row.

Return Value
------------

    The procedure returns 1 on success, and 0 otherwise.

.. note::

    -  Use :aimms:func:`GMP::Row::SetRightHandSideMulti` or
       :aimms:func:`GMP::Row::SetRightHandSideRaw` if the right-hand-side
       values of many rows have to be set, because that will be more efficient.

    -  If the row has a unit then *value* should have the same unit. If
       *value* has no unit then you should multiply it by the row scale, as
       returned by the function :aimms:func:`GMP::Row::GetScale`.

Example
-------

    Assume that 'c1' is a constraint in mathematical program 'MP' with a
    unit as defined by: 

    .. code-block:: aimms

               Quantity SI_Mass {
                   BaseUnit     :  kg;
                   Conversions  :  ton -> kg : # -> # * 1000;
               }
               Constraint c1 {
                   Unit         :  ton;
                   Definition   :  -x1 + 2 * x2 <= wght;
               }

    Then if we run the following code

    .. code-block:: aimms

               GMP::Row::SetRightHandSide( 'MP', c1, 20 [ton] );
               rhs1 := GMP::Row::GetRightHandSide( 'MP', c1 );
               display rhs1;

               GMP::Row::SetRightHandSide( 'MP', c1, 30 );
               rhs2 := GMP::Row::GetRightHandSide( 'MP', c1 );
               display rhs2;

               GMP::Row::SetRightHandSide( 'MP', c1, 40 * GMP::Row::GetScale( 'MP', c1 ) );
               rhs3 := GMP::Row::GetRightHandSide( 'MP', c1 );
               display rhs3;

    (where 'rhs1', 'rhs2' and 'rhs3' are parameters without a
    unit) we get the following results: 

    .. code-block:: aimms

               rhs1 := 20 ;

               rhs2 := 0.030 ;

               rhs3 := 40 ;

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Row::SetRightHandSideMulti`, :aimms:func:`GMP::Row::SetRightHandSideRaw`, :aimms:func:`GMP::Row::SetLeftHandSide`, :aimms:func:`GMP::Row::GetRightHandSide` and :aimms:func:`GMP::Row::GetScale`.
