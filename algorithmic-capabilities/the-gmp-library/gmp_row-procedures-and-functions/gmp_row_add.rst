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

    -  After calling :aimms:func:`GMP::Row::Add` the type and the left-hand-side and
       right-hand-side values are set according to the definition of the
       corresponding symbolic constraint. By using the procedures
       :aimms:func:`GMP::Row::SetType`, :aimms:func:`GMP::Row::SetLeftHandSide` and
       :aimms:func:`GMP::Row::SetRightHandSide` the row type and row bounds can be
       changed.

    -  Use procedure :aimms:func:`GMP::Row::Generate` to generate a (non-empty) row
       according to the definition of its associated symbolic constraint.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Coefficient::Set`, :aimms:func:`GMP::Row::AddMulti`, :aimms:func:`GMP::Row::Delete`, :aimms:func:`GMP::Row::SetType`, :aimms:func:`GMP::Row::SetLeftHandSide`,
    :aimms:func:`GMP::Row::SetRightHandSide` and :aimms:func:`GMP::Row::Generate`.
