.. aimms:procedure:: GMP::Linearization::SetDeviationBound(GMP, row, linNo, value)

.. _GMP::Linearization::SetDeviationBound:

GMP::Linearization::SetDeviationBound
=====================================

The procedure :aimms:func:`GMP::Linearization::SetDeviationBound` sets the
deviation bound of a linearization of a row in a generated mathematical
program. The lower bound of the extra column generated for the
linearization is always 0; this procedure sets the upper bound.

.. code-block:: aimms

    GMP::Linearization::SetDeviationBound(
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
        A scalar value representing the deviaton upper bound of the row.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. seealso::

    The routines :aimms:func:`GMP::Linearization::GetDeviationBound`, :aimms:func:`GMP::Linearization::GetDeviation` and :aimms:func:`GMP::Linearization::RemoveDeviation`.
