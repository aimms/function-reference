.. aimms:function:: GMP::Instance::GetNumberOfColumns(GMP)

.. _GMP::Instance::GetNumberOfColumns:

GMP::Instance::GetNumberOfColumns
=================================

The function :aimms:func:`GMP::Instance::GetNumberOfColumns` returns the number of
columns of a generated mathematical program.

.. code-block:: aimms

    GMP::Instance::GetNumberOfColumns(
         GMP             ! (input) a generated mathematical program
         )

Arguments
---------

    *GMP*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

Return Value
------------

    The function returns the number of columns.

.. seealso::

    - The functions :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::GetNumberOfRows` and :aimms:func:`GMP::Instance::GetNumberOfNonzeros`.
