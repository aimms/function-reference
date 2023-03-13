.. aimms:function:: GMP::Column::GetUpperBound(GMP, column)

.. _GMP::Column::GetUpperBound:

GMP::Column::GetUpperBound
==========================

The function :aimms:func:`GMP::Column::GetUpperBound` returns the upper bound of a
column in the generated mathematical program.

.. code-block:: aimms

    GMP::Column::GetUpperBound(
         GMP,            ! (input) a generated mathematical program
         column          ! (input) a scalar reference or column number
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *column*
        A scalar reference to an existing column in the matrix or an element in the
        set :aimms:set:`Integers` in the range :math:`\{ 0 .. n-1 \}` where :math:`n` is the
        number of columns in the matrix.

Return Value
------------

    The upper bound value for the specified column.

.. note::

    -  If the column has a unit then the scaled upper bound is returned
       (without unit).

    -  This function can be used to retrieve the upper bound after
       presolving in case the GMP was created by
       :aimms:func:`GMP::Instance::CreatePresolved`, even if the column was deleted
       by the AIMMS Presolver.

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

    If we want to multiply the upper bound by 1.5
    and assign it as the new value by using function
    :aimms:func:`GMP::Column::SetUpperBound` we can use 

    .. code-block:: aimms

               ub1 := 1.5 * (GMP::Column::GetUpperBound( 'MP', x1 )) [ton];

               GMP::Column::SetUpperBound( 'MP', x1, ub1 );

    if 'ub1' is a
    parameter with unit [ton], or we can use 

    .. code-block:: aimms

               ub2 := 1.5 * GMP::Column::GetUpperBound( 'MP', x1 );

               GMP::Column::SetUpperBound( 'MP', x1, ub2 * GMP::Column::GetScale( 'MP', x1 ) );

    if 'ub2' is a
    parameter without a unit.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Column::SetUpperBound`, :aimms:func:`GMP::Column::GetLowerBound`, :aimms:func:`GMP::Column::GetScale` and :aimms:func:`GMP::Instance::CreatePresolved`.
