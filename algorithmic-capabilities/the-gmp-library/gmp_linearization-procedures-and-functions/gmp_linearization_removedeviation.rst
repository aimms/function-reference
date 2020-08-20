.. aimms:procedure:: GMP::Linearization::RemoveDeviation(GMP, row, linNo)

.. _GMP::Linearization::RemoveDeviation:

GMP::Linearization::RemoveDeviation
===================================

The procedure :aimms:func:`GMP::Linearization::RemoveDeviation` removes the
deviation of a linearization of a row in a generated mathematical
program. That is, it deletes the extra column created (if any) when
adding the linearization of the row to the generated mathematical
program.

.. code-block:: aimms

    GMP::Linearization::RemoveDeviation(
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

    The procedure returns 1 on success, or 0 otherwise.

.. seealso::

    The routines :aimms:func:`GMP::Linearization::GetDeviation`, :aimms:func:`GMP::Linearization::Add` and :aimms:func:`GMP::Linearization::AddSingle`.
