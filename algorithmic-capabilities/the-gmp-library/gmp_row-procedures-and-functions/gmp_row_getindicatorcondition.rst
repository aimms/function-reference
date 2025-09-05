.. aimms:function:: GMP::Row::GetIndicatorCondition(GMP, row)

.. _GMP::Row::GetIndicatorCondition:

GMP::Row::GetIndicatorCondition
===============================

The function :aimms:func:`GMP::Row::GetIndicatorCondition` returns the indicator
condition of a row in a generated mathematical program.

.. code-block:: aimms

    GMP::Row::GetIndicatorCondition(
         GMP,            ! (input) a generated mathematical program
         row             ! (input) a scalar reference
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *row*
        A scalar reference to an existing row in the matrix.

Return Value
------------

    The function returns the indicator condition.

.. note::

    This function fails if the row has no indicator column.

.. seealso::

    - The routines :aimms:func:`GMP::Row::DeleteIndicatorCondition`, :aimms:func:`GMP::Row::GetIndicatorColumn` and :aimms:func:`GMP::Row::SetIndicatorCondition`.
