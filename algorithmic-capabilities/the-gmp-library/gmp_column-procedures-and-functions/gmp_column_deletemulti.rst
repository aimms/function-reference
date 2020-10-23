.. aimms:procedure:: GMP::Column::DeleteMulti(GMP, binding, column)

.. _GMP::Column::DeleteMulti:

GMP::Column::DeleteMulti
========================

The procedure :aimms:func:`GMP::Column::DeleteMulti` marks a column in the matrix of a
generated mathematical program as deleted.

.. code-block:: aimms

    GMP::Column::DeleteMulti(
         GMP,            ! (input) a generated mathematical program
         binding,        ! (input) an index binding
         column          ! (input) a variable expression
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *binding*
        An index binding that specifies and possibly limits the scope of
        indices.

    *column*
        A variable that, combined with the ``binding`` domain, specifies the
        columns.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  The columns will not be printed in the constraint listing, nor be
       visible in the Math Program Inspector and they will be removed from any
       solver maintained copies.

    -  Use ``GMP::Column::Add`` to undo this action.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Column::Add` and :aimms:func:`GMP::Column::Delete`.
