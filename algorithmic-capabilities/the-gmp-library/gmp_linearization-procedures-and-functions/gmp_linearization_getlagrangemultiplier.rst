.. aimms:function:: GMP::Linearization::GetLagrangeMultiplier(GMP, row, linNo)

.. _GMP::Linearization::GetLagrangeMultiplier:

GMP::Linearization::GetLagrangeMultiplier
=========================================

The function :aimms:func:`GMP::Linearization::GetLagrangeMultiplier` returns the
Lagrange multiplier used when adding the linearization of a row to a
generated mathematical program. (In other words, the marginal value of
the row that was used when the linearization was added.)

.. code-block:: aimms

    GMP::Linearization::GetLagrangeMultiplier(
         GMP,    ! (input) a generated mathematical program
         row,    ! (input) a scalar reference
         linNo   ! (input) a linearization number
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *row*
        A scalar reference to an existing nonlinear row in in the matrix.

    *linNo*
        An integer scalar reference to the rows and columns of the
        linearization.

Return Value
------------

    The function returns the Lagrange multiplier used when adding the
    linearization of a row.

.. seealso::

    The procedure :aimms:func:`GMP::Linearization::Add`.
