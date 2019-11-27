.. aimms:procedure:: GMP::Column::Delete(GMP, column)

.. _GMP::Column::Delete:

GMP::Column::Delete
===================

The procedure :aimms:func:`GMP::Column::Delete` marks a column in the matrix of a
generated mathematical program as deleted.

.. code-block:: aimms

    GMP::Column::Delete(
         GMP,            ! (input) a generated mathematical program
         column          ! (input) a scalar reference or column number
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *column*
        A scalar reference to an existing column in the matrix or the number of
        that column in the range :math:`\{ 0 .. n-1 \}` where :math:`n` is the
        number of columns in the matrix.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  The column will not be printed in the constraint listing, nor be
       visible in the math program inspector and it will be removed from any
       solver maintained copies.

    -  Use ``GMP::Column::Add`` to undo this action.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate` and :aimms:func:`GMP::Column::Add`.
