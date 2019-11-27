.. aimms:procedure:: GMP::Row::Activate(GMP, row)

.. _GMP::Row::Activate:

GMP::Row::Activate
==================

The procedure :aimms:func:`GMP::Row::Activate` activates a deactivated row in a
generated mathematical program.

.. code-block:: aimms

    GMP::Row::Activate(
         GMP,            ! (input) a generated mathematical program
         row             ! (input) a scalar reference or row number
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *row*
        A scalar reference to an existing row in the matrix or the number of
        that row in the range :math:`\{ 0 .. m-1 \}` where :math:`m` is the
        number of rows in the matrix.

Return Value
------------

    The procedure returns 1 on success, and 0 otherwise.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate` and :aimms:func:`GMP::Row::Deactivate`.
