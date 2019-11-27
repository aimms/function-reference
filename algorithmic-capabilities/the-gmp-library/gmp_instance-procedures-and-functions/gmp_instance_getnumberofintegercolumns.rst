.. aimms:function:: GMP::Instance::GetNumberOfIntegerColumns(GMP)

.. _GMP::Instance::GetNumberOfIntegerColumns:

GMP::Instance::GetNumberOfIntegerColumns
========================================

The function :aimms:func:`GMP::Instance::GetNumberOfIntegerColumns` returns the
number of integer columns of a generated mathematical program.

.. code-block:: aimms

    GMP::Instance::GetNumberOfIntegerColumns(
         GMP             ! (input) a generated mathematical program
         )

Arguments
---------

    *GMP*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

Return Value
------------

    The function returns the number of integer columns.

.. seealso::

    The functions :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::GetNumberOfColumns` and :aimms:func:`GMP::Instance::GetNumberOfNonlinearColumns`.
