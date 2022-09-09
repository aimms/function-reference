.. aimms:procedure:: GMP::Row::DeleteMulti(GMP, binding, row)

.. _GMP::Row::DeleteMulti:

GMP::Row::DeleteMulti
=====================

The procedure :aimms:func:`GMP::Row::DeleteMulti` marks a group of rows
in a generated mathematical program, belonging to a constraint, as deleted.

.. code-block:: aimms

    GMP::Row::DeleteMulti(
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

    -  Deleted rows remain present in the generated mathematical
       program but their content will not be copied to a solver session.

    -  The rows will not be printed in the constraint listing, nor be
       visible in the Math Program Inspector and they will be removed from any
       solver maintained copies.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Row::Add` and :aimms:func:`GMP::Row::Delete`.
