.. aimms:procedure:: GMP::Row::SetType(GMP, row, type)

.. _GMP::Row::SetType:

GMP::Row::SetType
=================

The procedure :aimms:func:`GMP::Row::SetType` changes the type of a row in the
matrix of a generated mathematical program.

.. code-block:: aimms

    GMP::Row::SetType(
         GMP,            ! (input) a generated mathematical program
         row,            ! (input) a scalar reference or row number
         type            ! (input) an element in AllRowTypes
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *row*
        A scalar reference to an existing row in the matrix or the number of
        that row in the range :math:`\{ 0 .. m-1 \}` where :math:`m` is the
        number of rows in the matrix.

    *type*
        An element in :aimms:set:`AllRowTypes`.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    Use ``GMP::Row::SetTypeMulti`` if the type of many rows corresponding to some constraint
    have to be changed, because that will be more efficient.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Row::GetType` and :aimms:func:`GMP::Row::SetTypeMulti`.
