.. aimms:procedure:: GMP::Row::DeleteIndicatorCondition(GMP, row)

.. _GMP::Row::DeleteIndicatorCondition:

GMP::Row::DeleteIndicatorCondition
==================================

The procedure :aimms:func:`GMP::Row::DeleteIndicatorCondition` deletes an
indicator column and condition from a row in a generated mathematical
program.

.. code-block:: aimms

    GMP::Row::DeleteIndicatorCondition(
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

.. note::

    This procedure transforms an indicator row into a normal row.

.. seealso::

    The routines :aimms:func:`GMP::Row::GetIndicatorColumn`, :aimms:func:`GMP::Row::GetIndicatorCondition` and :aimms:func:`GMP::Row::SetIndicatorCondition`.
