.. aimms:function:: GMP::Linearization::GetWeight(GMP, row, linNo)

.. _GMP::Linearization::GetWeight:

GMP::Linearization::GetWeight
=============================

The function :aimms:func:`GMP::Linearization::GetWeight` returns the weight of a
linearization of a row in a generated mathematical program. The weight
of a linearization is defined as the objective coefficient of the column
that was added to the generated mathematical program when the
linearization was added and if a deviation was permitted.

.. code-block:: aimms

    GMP::Linearization::GetWeight(
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

    The function returns the weight of the linearization.

.. note::

    -  This function returns 0 if no extra column was added for the
       linearization.

    -  If the objective coefficient of the deviation column (if any) was not
       changed, the weight equals the penalty multiplier multiplied with the
       marginal value of the row that was used when the linearization was
       added with :aimms:func:`GMP::Linearization::Add` or
       :aimms:func:`GMP::Linearization::AddSingle`.

.. seealso::

    - The procedures :aimms:func:`GMP::Linearization::Add`, :aimms:func:`GMP::Linearization::AddSingle` and :aimms:func:`GMP::Linearization::SetWeight`.
