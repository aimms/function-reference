.. aimms:procedure:: GMP::Row::SetTypeMulti(GMP, binding, row, type)

.. _GMP::Row::SetTypeMulti:

GMP::Row::SetTypeMulti
======================

The procedure :aimms:func:`GMP::Row::SetTypeMulti` changes the types of a group of rows,
belonging to a constraint, in a generated mathematical program.

.. code-block:: aimms

    GMP::Row::SetTypeMulti(
         GMP,            ! (input) a generated mathematical program
         binding,        ! (input) an index binding
         row,            ! (input) a constraint expression
         type            ! (input) an element parameter in AllRowTypes
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *binding*
        An index binding that specifies and possibly limits the scope of
        indices.

    *row*
        A constraint that, combined with the *binding* domain, specifies the
        rows.

    *type*
        An element parameter in :aimms:set:`AllRowTypes`, defined over the *binding* domain.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. seealso::

    - The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Row::GetType` and :aimms:func:`GMP::Row::SetType`.
