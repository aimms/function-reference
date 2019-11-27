.. aimms:function:: GMP::Row::GetLeftHandSide(GMP, row)

.. _GMP::Row::GetLeftHandSide:

GMP::Row::GetLeftHandSide
=========================

| The function :aimms:func:`GMP::Row::GetLeftHandSide` returns the left-hand-side
  value of a row as present in the generated mathematical program. This
  function is typically used for ranged constraints.
| Note that this function does not return the (evaluated) level value of
  a row; you should use the function ``GMP::Solution::GetRowValue``
  instead.

.. code-block:: aimms

    GMP::Row::GetLeftHandSide(
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

    The function returns the left-hand-side value of the specified row.

.. note::

    If the row has a unit then the scaled left-hand-side value is returned
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
               Parameter wght_lower {
                   Unit          :  ton;
                   InitialValue  :  20;
               }
               Parameter wght_upper {
                   Unit          :  ton;
                   InitialValue  :  60;
               }
               Constraint c1 {
                   Unit          :  ton;
                   Definition    :  wght_lower <= -x1 + 2 * x2 <= wght_upper;
               }

    If we want to multiply the
    left-hand-side value by 1.5 and assign it as the new value by using
    function ``GMP::Row::SetLeftHandSide`` we can use 

    .. code-block:: aimms

               lhs1 := 1.5 * (GMP::Row::GetLeftHandSide( 'MP', c1 )) [ton];

               GMP::Row::SetLeftHandSide( 'MP', c1, lhs1 );

    if 'lhs1'
    is a parameter with unit [ton], or we can use 

    .. code-block:: aimms

               lhs2 := 1.5 * GMP::Row::GetLeftHandSide( 'MP', c1 );

               GMP::Row::SetLeftHandSide( 'MP', c1, lhs2 * GMP::Row::GetScale( 'MP', c1 ) );

    if 'lhs2' is a
    parameter without a unit.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Row::SetLeftHandSide`, :aimms:func:`GMP::Row::GetRightHandSide`, :aimms:func:`GMP::Row::GetScale` and :aimms:func:`GMP::Solution::GetRowValue`.
