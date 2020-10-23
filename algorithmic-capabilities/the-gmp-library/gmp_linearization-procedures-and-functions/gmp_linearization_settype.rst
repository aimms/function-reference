.. aimms:procedure:: GMP::Linearization::SetType(GMP, row, linNo, rowtype)

.. _GMP::Linearization::SetType:

GMP::Linearization::SetType
===========================

The procedure :aimms:func:`GMP::Linearization::SetType` sets the row type of
linearization of a row in a generated mathematical program.

.. code-block:: aimms

    GMP::Linearization::SetType(
         GMP,    ! (input) a generated mathematical program
         row,    ! (input) a scalar reference or row number
         linNo,  ! (input) a linearization number
         rowtype ! (input) a row type
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *row*
        A scalar reference to an existing nonlinear row in the matrix or the number of
        that row in the range :math:`\{ 0 .. m-1 \}` where :math:`m` is the
        number of rows in the matrix.

    *linNo*
        An integer scalar reference to the rows and columns of the
        linearization.

    *rowtype*
        An element (or element parameter or element valued expression) in the
        predeclared set :aimms:set:`AllRowTypes`.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. seealso::

    The function :aimms:func:`GMP::Linearization::GetType`.
