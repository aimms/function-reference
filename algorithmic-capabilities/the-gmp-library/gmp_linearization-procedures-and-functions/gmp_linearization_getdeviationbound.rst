.. aimms:function:: GMP::Linearization::GetDeviationBound(GMP, row, linNo)

.. _GMP::Linearization::GetDeviationBound:

GMP::Linearization::GetDeviationBound
=====================================

The function :aimms:func:`GMP::Linearization::GetDeviationBound` returns the
deviation bound of a linearization of a row in a generated mathematical
program. The lower bound of the extra column generated for the
linearization is always 0; this function returns the upper bound.

.. code-block:: aimms

    GMP::Linearization::GetDeviationBound(
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

    The function returns the deviation upperbound of a linearization.

.. seealso::

    - The routines :aimms:func:`GMP::Linearization::SetDeviationBound` and :aimms:func:`GMP::Linearization::GetDeviation`.
