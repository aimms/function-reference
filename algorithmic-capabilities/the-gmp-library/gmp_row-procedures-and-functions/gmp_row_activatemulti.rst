.. aimms:procedure:: GMP::Row::ActivateMulti(GMP, binding, row)

.. _GMP::Row::ActivateMulti:

GMP::Row::ActivateMulti
=======================

The procedure :aimms:func:`GMP::Row::ActivateMulti` activates a group of deactivated rows,
belonging to a constraint, in a generated mathematical program.

.. code-block:: aimms

    GMP::Row::ActivateMulti(
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

    The procedure returns 1 on success, and 0 otherwise.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Row::Activate` and :aimms:func:`GMP::Row::Deactivate`.
