.. aimms:procedure:: GMP::Row::Delete(GMP, row)

.. _GMP::Row::Delete:

GMP::Row::Delete
================

The procedure :aimms:func:`GMP::Row::Delete` marks a row in a
generated mathematical program as deleted.

.. code-block:: aimms

    GMP::Row::Delete(
         GMP,            ! (input) a generated mathematical program
         row             ! (input) a scalar reference or row number
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *row*
        A scalar reference to an existing row in the matrix or the number of
        that row in the range :math:`\{ 0 .. m-1 \}` where :math:`m` is the
        number of rows in the matrix.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  Use :aimms:func:`GMP::Row::DeleteMulti` or :aimms:func:`GMP::Row::DeleteMulti`
       if many rows have to be deleted, because that will be more efficient.

    -  A deleted row remains present in the generated mathematical program
       but its content will not be copied to a solver session.

    -  The row will not be printed in the constraint listing, nor be visible
       in the Math Program Inspector and it will be removed from any solver
       maintained copies.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Row::Add`, :aimms:func:`GMP::Row::DeleteMulti` and :aimms:func:`GMP::Row::DeleteRaw`.
