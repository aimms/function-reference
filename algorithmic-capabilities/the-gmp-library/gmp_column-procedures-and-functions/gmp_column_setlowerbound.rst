.. aimms:procedure:: GMP::Column::SetLowerBound(GMP, column, value)

.. _GMP::Column::SetLowerBound:

GMP::Column::SetLowerBound
==========================

The procedure :aimms:func:`GMP::Column::SetLowerBound` changes the lower bound of
a column in a generated mathematical program.

.. code-block:: aimms

    GMP::Column::SetLowerBound(
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
        The new value assigned to the lower bound of the column.

Return Value
------------

    The procedure returns 1 on success, and 0 otherwise.

.. note::

    -  Use :aimms:func:`GMP::Column::SetLowerBoundMulti` or :aimms:func:`GMP::Column::SetLowerBoundRaw`
       if the lower bounds of many columns have to be set, because that will
       be more efficient.

    -  If the column has a unit then *value* should have the same unit. If
       *value* has no unit then you should multiply it by the column scale,
       as returned by the function :aimms:func:`GMP::Column::GetScale`.

Example
-------

    Assume that 'x1' is a variable in mathematical program 'MP' with a unit
    as defined by: 

    .. code-block:: aimms

               Quantity SI_Mass {
                   BaseUnit      :  kg;
                   Conversions   :  ton -> kg : # -> # * 1000;
               }
               Parameter min_wght {
                   Unit          :  ton;
                   InitialValue  :  20;
               }
               Variable x1 {
                   Range         :  [min_wght, inf);
                   Unit          :  ton;
               }

    Then if we run the following code 

    .. code-block:: aimms

               GMP::Column::SetLowerBound( 'MP', x1, 20 [ton] );
               lb1 := GMP::Column::GetLowerBound( 'MP', x1 );
               display lb1;

               GMP::Column::SetLowerBound( 'MP', x1, 30 );
               lb2 := GMP::Column::GetLowerBound( 'MP', x1 );
               display lb2;

               GMP::Column::SetLowerBound( 'MP', x1, 40 * GMP::Column::GetScale( 'MP', x1 ) );
               lb3 := GMP::Column::GetLowerBound( 'MP', x1 );
               display lb3;
    
    (where 'lb1', 'lb2' and 'lb3' are parameters without a unit) we get the following results: 
    
    .. code-block:: aimms

               lb1 := 20 ;

               lb2 := 0.030 ;

               lb3 := 40 ;

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Column::SetLowerBoundMulti`, :aimms:func:`GMP::Column::SetLowerBoundRaw`, :aimms:func:`GMP::Column::SetUpperBound`, :aimms:func:`GMP::Column::GetLowerBound` and :aimms:func:`GMP::Column::GetScale`.
