.. aimms:procedure:: GMP::Row::SetLeftHandSide(GMP, row, value)

.. _GMP::Row::SetLeftHandSide:

GMP::Row::SetLeftHandSide
=========================

The procedure :aimms:func:`GMP::Row::SetLeftHandSide` changes the left-hand-side
of a row in a generated mathematical program.

.. code-block:: aimms

    GMP::Row::SetLeftHandSide(
         GMP,            ! (input) a generated mathematical program
         row,            ! (input) a scalar reference or row number
         value           ! (input) a numerical expression
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *row*
        A scalar reference to an existing row in the matrix or an element in the
        set :aimms:set:`Integers` in the range :math:`\{ 0 .. m-1 \}` where :math:`m` is the
        number of rows in the matrix.

    *value*
        The new value that should be assigned to the left-hand-side of the row.

Return Value
------------

    The procedure returns 1 on success, and 0 otherwise.

.. note::

    If the row has a unit then *value* should have the same unit. If *value*
    has no unit then you should multiply it by the row scale, as returned by
    the function :aimms:func:`GMP::Row::GetScale`.

Example
-------

Assume that ``c1`` is a constraint in mathematical program ``MP`` with a
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

    GMP::Row::SetLeftHandSide( 'MP', c1, 20 [ton] );
    lhs1 := GMP::Row::GetLeftHandSide( 'MP', c1 );
    display lhs1;

    GMP::Row::SetLeftHandSide( 'MP', c1, 30 );
    lhs2 := GMP::Row::GetLeftHandSide( 'MP', c1 );
    display lhs2;

    GMP::Row::SetLeftHandSide( 'MP', c1, 40 * GMP::Row::GetScale( 'MP', c1 ) );
    lhs3 := GMP::Row::GetLeftHandSide( 'MP', c1 );
    display lhs3;

(where ``lhs1``, ``lhs2`` and ``lhs3`` are parameters without a
unit) we get the following results: 

.. code-block:: aimms

    lhs1 := 20 ;

    lhs2 := 0.030 ;

    lhs3 := 40 ;

.. seealso::

    - The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Row::SetRightHandSide`, :aimms:func:`GMP::Row::GetLeftHandSide` and :aimms:func:`GMP::Row::GetScale`.
