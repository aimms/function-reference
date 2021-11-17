.. aimms:procedure:: GMP::Column::Add(GMP, column)

.. _GMP::Column::Add:

GMP::Column::Add
================

The procedure :aimms:func:`GMP::Column::Add` adds a column to a
generated mathematical program.

.. code-block:: aimms

    GMP::Column::Add(
         GMP,            ! (input) a generated mathematical program
         column          ! (input) a scalar reference
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *column*
        A scalar reference to a column.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  Use :aimms:func:`GMP::Column::AddMulti` if many columns corresponding to some variable
       have to be added, because that will be more efficient.

    -  Coefficients for this column can be added to the matrix by using the
       procedure :aimms:func:`GMP::Coefficient::Set`. After calling :aimms:func:`GMP::Column::Add`
       the type and the lower and upper bound of the column are set according
       to the definition of the corresponding symbolic variable. By using the
       procedures :aimms:func:`GMP::Column::SetType`, :aimms:func:`GMP::Column::SetLowerBound` and
       :aimms:func:`GMP::Column::SetUpperBound` the column type and the lower and upper
       bound can be changed.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Coefficient::Set`, :aimms:func:`GMP::Column::AddMulti`, :aimms:func:`GMP::Column::Delete`, :aimms:func:`GMP::Column::SetType`, :aimms:func:`GMP::Column::SetLowerBound` and
    :aimms:func:`GMP::Column::SetUpperBound`.
