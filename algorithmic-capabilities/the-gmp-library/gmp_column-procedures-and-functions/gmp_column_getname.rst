.. aimms:function:: GMP::Column::GetName(GMP, column)

.. _GMP::Column::GetName:

GMP::Column::GetName
====================

The function :aimms:func:`GMP::Column::GetName` returns the name of a column in
the matrix of a generated mathematical program.

.. code-block:: aimms

    GMP::Column::GetName(
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

    The function returns a string.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate` and :aimms:func:`GMP::row::GetName`.
