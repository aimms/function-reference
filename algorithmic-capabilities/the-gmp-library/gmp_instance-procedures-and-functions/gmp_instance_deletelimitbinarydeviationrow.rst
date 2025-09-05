.. aimms:procedure:: GMP::Instance::DeleteLimitBinaryDeviationRow(GMP, refNo)

.. _GMP::Instance::DeleteLimitBinaryDeviationRow:

GMP::Instance::DeleteLimitBinaryDeviationRow
============================================

The procedure :aimms:func:`GMP::Instance::DeleteIntegerEliminationRows` deletes a
row from a GMP that was added using the procedure
:aimms:func:`GMP::Instance::AddLimitBinaryDeviationRow`.

.. code-block:: aimms

    GMP::Instance::DeleteLimitBinaryDeviationRow(
         GMP,          ! (input) a generated mathematical program
         [refNo]       ! (optional, default 1) a scalar integer value
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *refNo*
        A positive integer scalar value representing a reference number. The default is 1.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. seealso::

    - The procedure :aimms:func:`GMP::Instance::AddLimitBinaryDeviationRow`.
