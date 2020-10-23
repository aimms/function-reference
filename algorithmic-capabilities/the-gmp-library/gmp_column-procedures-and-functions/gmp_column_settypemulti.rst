.. aimms:procedure:: GMP::Column::SetTypeMulti(GMP, column, type)

.. _GMP::Column::SetTypeMulti:

GMP::Column::SetTypeMulti
=========================

The procedure :aimms:func:`GMP::Column::SetTypeMulti` changes the type of a
group of columns, belonging to a variable, in the matrix of a generated mathematical program.

.. code-block:: aimms

    GMP::Column::SetTypeMulti(
         GMP,            ! (input) a generated mathematical program
         binding,        ! (input) an index binding
         column,         ! (input) a variable expression
         type            ! (input) an element parameter in AllColumnTypes
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

    *type*
        An element parameter in :aimms:set:`AllColumnTypes`, defined over the binding domain ``binding``.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. seealso::

    The functions :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Column::GetType` and :aimms:func:`GMP::Column::SetType`.
