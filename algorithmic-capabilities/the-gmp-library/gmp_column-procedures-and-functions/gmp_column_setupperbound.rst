.. aimms:procedure:: GMP::Column::SetUpperBound(GMP, column, value)

.. _GMP::Column::SetUpperBound:

GMP::Column::SetUpperBound
==========================

The procedure :aimms:func:`GMP::Column::SetUpperBound` changes the upper bound of
a column in the generated mathematical program.

.. code-block:: aimms

    GMP::Column::SetUpperBound(
         GMP,            ! (input) a generated mathematical program
         column,         ! (input) a scalar reference or column number
         value           ! (input) a numerical expression
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *column*
        A scalar reference to an existing column in the matrix or the number of
        that column in the range :math:`\{ 0 .. n-1 \}` where :math:`n` is the
        number of columns in the matrix.

    *value*
        The new value assigned to the upper bound of the column.

Return Value
------------

    The procedure returns 1 on success, and 0 otherwise.

.. note::

    -  Use ``GMP::Column::SetUpperBoundMulti`` if the upper bound of many
       columns corresponding to some variable have to be set, because that
       will be more efficient.

    -  If the column has a unit then *value* should have the same unit. If
       *value* has no unit then you should multiply it by the column scale,
       as returned by the function ``GMP::Column::GetScale``.

Example
-------

    Assume that 'x1' is a variable in mathematical program 'MP' with a unit
    as defined by: 

    .. code-block:: aimms

               Quantity SI_Mass {
                   BaseUnit      :  kg;
                   Conversions   :  ton -> kg : # -> # * 1000;
               }
               Parameter max_wght {
                   Unit          :  ton;
                   InitialValue  :  20;
               }
               Variable x1 {
                   Range         :  [0, max_wght];
                   Unit          :  ton;
               }

    Then if we run the following code 

    .. code-block:: aimms

               GMP::Column::SetUpperBound( 'MP', x1, 20 [ton] );
               ub1 := GMP::Column::GetUpperBound( 'MP', x1 );
               display ub1;

               GMP::Column::SetUpperBound( 'MP', x1, 30 );
               ub2 := GMP::Column::GetUpperBound( 'MP', x1 );
               display ub2;

               GMP::Column::SetUpperBound( 'MP', x1, 40 * GMP::Column::GetScale( 'MP', x1 ) );
               ub3 := GMP::Column::GetUpperBound( 'MP', x1 );
               display ub3;

        (where 'ub1', 'ub2' and 'ub3' are parameters without a unit) we get the
    following results: 

    .. code-block:: aimms

               ub1 := 20 ;

               ub2 := 0.030 ;

               ub3 := 40 ;

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Column::SetUpperBoundMulti`, :aimms:func:`GMP::Column::SetLowerBound`, :aimms:func:`GMP::Column::GetUpperBound` and :aimms:func:`GMP::Column::GetScale`.
