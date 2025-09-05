.. aimms:function:: GMP::Instance::GetNumberOfRows(GMP)

.. _GMP::Instance::GetNumberOfRows:

GMP::Instance::GetNumberOfRows
==============================

The function :aimms:func:`GMP::Instance::GetNumberOfRows` returns the number of
rows of a generated mathematical program.

.. code-block:: aimms

    GMP::Instance::GetNumberOfRows(
         GMP             ! (input) a generated mathematical program
         )

Arguments
---------

    *GMP*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

Return Value
------------

    The function returns the number of rows.

.. seealso::

    - The functions :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::GetNumberOfColumns` and :aimms:func:`GMP::Instance::GetNumberOfNonzeros`.
