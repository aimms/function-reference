.. aimms:function:: GMP::Linearization::GetType(GMP, row, linNo)

.. _GMP::Linearization::GetType:

GMP::Linearization::GetType
===========================

The function :aimms:func:`GMP::Linearization::GetType` returns the row type of a
linearization of a row in a generated mathematical program.

.. code-block:: aimms

    GMP::Linearization::GetType(
         GMP,    ! (input) a generated mathematical program
         row,    ! (input) a scalar reference or row number
         linNo   ! (input) a linearization number
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

Return Value
------------

    An element in the set :aimms:set:`AllRowTypes`.

.. seealso::

    The procedure :aimms:func:`GMP::Linearization::SetType`.
