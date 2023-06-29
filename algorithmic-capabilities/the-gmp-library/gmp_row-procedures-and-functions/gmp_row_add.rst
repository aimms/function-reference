.. aimms:procedure:: GMP::Row::Add(GMP, row)

.. _GMP::Row::Add:

GMP::Row::Add
=============

The procedure :aimms:func:`GMP::Row::Add` adds an empty row to the matrix of a
generated mathematical program.

.. code-block:: aimms

    GMP::Row::Add(
         GMP,            ! (input) a generated mathematical program
         row             ! (input) a scalar reference
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *row*
        A scalar reference to a row.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  Use :aimms:func:`GMP::Row::AddMulti` if many rows corresponding to some constraint
       have to be added, because that will be more efficient.

    -  Coefficients for this row can be added to the matrix by using the
       procedure :aimms:func:`GMP::Coefficient::Set`.

    -  The procedure :aimms:func:`GMP::Row::Add` sets the row type to '<=' and the
       right-hand-side value to ``INF``. By using the procedures
       :aimms:func:`GMP::Row::SetType` and :aimms:func:`GMP::Row::SetRightHandSide`
       the row type and the right-hand-side value can be changed.

    -  Use procedure :aimms:func:`GMP::Row::Generate` to generate a (non-empty) row
       according to the definition of its associated symbolic constraint.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Coefficient::Set`, :aimms:func:`GMP::Row::AddMulti`, :aimms:func:`GMP::Row::Delete`, :aimms:func:`GMP::Row::SetType`,
    :aimms:func:`GMP::Row::SetRightHandSide` and :aimms:func:`GMP::Row::Generate`.
