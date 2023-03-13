.. aimms:function:: GMP::Column::GetScale(GMP, column)

.. _GMP::Column::GetScale:

GMP::Column::GetScale
=====================

The function :aimms:func:`GMP::Column::GetScale` returns the scaling factor of a
column in the generated mathematical program.

.. code-block:: aimms

    GMP::Column::GetScale(
         GMP,            ! (input) a generated mathematical program
         column          ! (input) a scalar reference or column number
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *column*
        A scalar reference to an existing column in the matrix or an element in the
        set :aimms:set:`Integers` in the range :math:`\{ 0 .. n-1 \}` where :math:`n` is the
        number of columns in the matrix.

Return Value
------------

    The scaling factor for the specified column.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate` and :aimms:func:`GMP::Row::GetScale`.
