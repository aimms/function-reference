.. aimms:procedure:: GMP::Column::SetAsObjective(GMP, column)

.. _GMP::Column::SetAsObjective:

GMP::Column::SetAsObjective
===========================

The procedure :aimms:func:`GMP::Column::SetAsObjective` sets a column as the new
objective of a generated mathematical program.

.. code-block:: aimms

    GMP::Column::SetAsObjective(
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

    The procedure returns 1 on success, and 0 otherwise.

.. note::

    -  The column should be linear and have at least one coefficient in the
       matrix.

    -  The column should be free, i.e., not have a lower or upper bound.

    -  After a call to :aimms:func:`GMP::Column::SetAsObjective` the old objective
       column will be treated as a normal column.

.. seealso::

    - The routines :aimms:func:`GMP::Column::Add` and :aimms:func:`GMP::Instance::CreateDual`.
