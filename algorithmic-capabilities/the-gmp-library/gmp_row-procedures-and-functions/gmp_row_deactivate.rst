.. aimms:procedure:: GMP::Row::Deactivate(GMP, row)

.. _GMP::Row::Deactivate:

GMP::Row::Deactivate
====================

The procedure :aimms:func:`GMP::Row::Deactivate` deactivates a row in a generated
mathematical program. A deactivated row will not be passed to a solver
session.

.. code-block:: aimms

    GMP::Row::Deactivate(
         GMP,            ! (input) a generated mathematical program
         row             ! (input) a scalar reference or row number
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *row*
        A scalar reference to an existing row in the matrix or an element in the
        set :aimms:set:`Integers` in the range :math:`\{ 0 .. m-1 \}` where :math:`m` is the
        number of rows in the matrix.

Return Value
------------

    The procedure returns 1 on success, and 0 otherwise.

.. note::

    Use :aimms:func:`GMP::Row::DeactivateMulti` or :aimms:func:`GMP::Row::DeactivateRaw`
    if many rows have to be deactivated, because that will be more efficient.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Row::Activate`, :aimms:func:`GMP::Row::DeactivateMulti` and :aimms:func:`GMP::Row::DeactivateRaw`.
