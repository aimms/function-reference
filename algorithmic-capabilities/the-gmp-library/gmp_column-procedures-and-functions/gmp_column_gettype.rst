.. aimms:function:: GMP::Column::GetType(GMP, column)

.. _GMP::Column::GetType:

GMP::Column::GetType
====================

The function :aimms:func:`GMP::Column::GetType` returns the type of a column in
the matrix of a generated mathematical program.

.. code-block:: aimms

    GMP::Column::GetType(
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

    An element in the predefined set :aimms:set:`AllColumnTypes`.

.. seealso::

    - The routines :aimms:func:`GMP::Instance::Generate` and :aimms:func:`GMP::Column::SetType`.
