.. aimms:function:: GMP::Row::GetScale(GMP, row)

.. _GMP::Row::GetScale:

GMP::Row::GetScale
==================

The function :aimms:func:`GMP::Row::GetScale` returns the scaling factor of a row
in the generated mathematical program.

.. code-block:: aimms

    GMP::Row::GetScale(
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

    The scaling factor for the specified row.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate` and :aimms:func:`GMP::Column::GetScale`.
