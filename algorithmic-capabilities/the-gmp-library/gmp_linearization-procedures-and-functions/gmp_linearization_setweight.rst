.. aimms:procedure:: GMP::Linearization::SetWeight(GMP, row, linNo, value)

.. _GMP::Linearization::SetWeight:

GMP::Linearization::SetWeight
=============================

The procedure :aimms:func:`GMP::Linearization::SetWeight` sets the weight of a
linearization of a row in a generated mathematical program. The weight
of a linearization is defined as the objective coefficient of the column
that was added to the generated mathematical program when the
linearization was added and if a deviation was permitted.

.. code-block:: aimms

    GMP::Linearization::SetWeight(
         GMP,    ! (input) a generated mathematical program
         row,    ! (input) a scalar reference or row number
         linNo,  ! (input) a linearization number
         value   ! (input) a scalar value
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

    *value*
        A scalar value representing the new weight of the row.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. seealso::

    The function :aimms:func:`GMP::Linearization::GetWeight`.
