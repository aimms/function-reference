.. aimms:procedure:: GMP::Row::AddMulti(GMP, binding, row)

.. _GMP::Row::AddMulti:

GMP::Row::AddMulti
==================

The procedure :aimms:func:`GMP::Row::AddMulti` adds a group of empty rows, belonging to a constraint,
to the matrix of a generated mathematical program.

.. code-block:: aimms

    GMP::Row::AddMulti(
         GMP,            ! (input) a generated mathematical program
         binding,        ! (input) an index binding
         row             ! (input) a constraint expression
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

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  Coefficients for the rows can be added to the matrix by using the
       procedure :aimms:func:`GMP::Coefficient::SetMulti`.

    -  The procedure :aimms:func:`GMP::Row::AddMulti` sets the row type to '<=' and the
       right-hand-side values to ``INF``. By using the procedures
       :aimms:func:`GMP::Row::SetTypeMulti` and :aimms:func:`GMP::Row::SetRightHandSideMulti`
       the row type and the right-hand-side value can be changed.

    -  Use procedure :aimms:func:`GMP::Row::GenerateMulti` to generate (non-empty) rows
       according to the definition of the associated symbolic constraint.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Coefficient::SetMulti`, :aimms:func:`GMP::Row::Add`, :aimms:func:`GMP::Row::DeleteMulti`, :aimms:func:`GMP::Row::SetTypeMulti`,
    :aimms:func:`GMP::Row::SetRightHandSideMulti` and :aimms:func:`GMP::Row::GenerateMulti`.
