.. aimms:function:: GMP::Row::GetName(GMP, row)

.. _GMP::Row::GetName:

GMP::Row::GetName
=================

The function :aimms:func:`GMP::Row::GetName` returns the name of a row in the
matrix of a generated mathematical program.

.. code-block:: aimms

    GMP::Row::GetName(
         GMP,            ! (input) a generated mathematical program
         row             ! (input) a scalar reference or row number
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *row*
        A scalar reference to an existing row in the matrix or an element in the
        set :aimms:set:`Integers` in the range :math:`\{ 0 .. m-1 \}` where :math:`m` is the
        number of rows in the matrix.

Return Value
------------

    The function returns a string.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate` and :aimms:func:`GMP::Column::GetName`.
