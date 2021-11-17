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
       procedure :aimms:func:`GMP::Coefficient::Set`.

    -  After calling :aimms:func:`GMP::Row::Add` the type and the left-hand-side and
       right-hand-side values are set according to the definition of the
       corresponding symbolic constraint. By using the procedures
       :aimms:func:`GMP::Row::SetType`, :aimms:func:`GMP::Row::SetLeftHandSide` and
       :aimms:func:`GMP::Row::SetRightHandSide` the row type and row bounds can be
       changed.

    -  Use procedure :aimms:func:`GMP::Row::GenerateMulti` to generate (non-empty) rows
       according to the definition of the associated symbolic constraint.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Coefficient::Set`, :aimms:func:`GMP::Row::Add`, :aimms:func:`GMP::Row::Delete`, :aimms:func:`GMP::Row::SetType`, :aimms:func:`GMP::Row::SetLeftHandSide`,
    :aimms:func:`GMP::Row::SetRightHandSide` and :aimms:func:`GMP::Row::GenerateMulti`.
