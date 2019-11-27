.. aimms:function:: GMP::Row::GetType(GMP, row)

.. _GMP::Row::GetType:

GMP::Row::GetType
=================

The function :aimms:func:`GMP::Row::GetType` returns the type of a row in the
matrix of a generated mathematical program.

.. code-block:: aimms

    GMP::Row::GetType(
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

    The function returns an element in the predefined set :aimms:set:`AllRowTypes`.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate` and :aimms:func:`GMP::Row::SetType`.
