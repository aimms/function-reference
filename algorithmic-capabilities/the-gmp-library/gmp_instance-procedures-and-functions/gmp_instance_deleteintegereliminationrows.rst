.. aimms:procedure:: GMP::Instance::DeleteIntegerEliminationRows(GMP, elimNo)

.. _GMP::Instance::DeleteIntegerEliminationRows:

GMP::Instance::DeleteIntegerEliminationRows
===========================================

The procedure :aimms:func:`GMP::Instance::DeleteIntegerEliminationRows` deletes a
particular set of integer elimination rows and columns of a generated
mathematical program.

.. code-block:: aimms

    GMP::Instance::DeleteIntegerEliminationRows(
         GMP,          ! (input) a generated mathematical program
         elimNo        ! (input) an elimination number
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *elimNo*
        An integer scalar reference to an elimination number.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. seealso::

    The procedure :aimms:func:`GMP::Instance::AddIntegerEliminationRows`.
