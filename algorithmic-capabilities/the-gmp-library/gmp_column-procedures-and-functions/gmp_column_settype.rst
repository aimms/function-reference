.. aimms:procedure:: GMP::Column::SetType(GMP, column, type)

.. _GMP::Column::SetType:

GMP::Column::SetType
====================

The procedure :aimms:func:`GMP::Column::SetType` changes the type of a column in
a generated mathematical program.

.. code-block:: aimms

    GMP::Column::SetType(
         GMP,            ! (input) a generated mathematical program
         column,         ! (input) a scalar reference or column number
         type            ! (input) an element in AllColumnTypes
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *column*
        A scalar reference to an existing column in the matrix or an element in the
        set :aimms:set:`Integers` in the range :math:`\{ 0 .. n-1 \}` where :math:`n` is the
        number of columns in the matrix.

    *type*
        An element in :aimms:set:`AllColumnTypes`.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    Use :aimms:func:`GMP::Column::SetTypeMulti` or :aimms:func:`GMP::Column::SetTypeRaw`
    if the types of many columns have to be set, because that will be more efficient.

.. seealso::

    The functions :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Column::GetType`, :aimms:func:`GMP::Column::SetTypeMulti` and :aimms:func:`GMP::Column::SetTypeRaw`.
