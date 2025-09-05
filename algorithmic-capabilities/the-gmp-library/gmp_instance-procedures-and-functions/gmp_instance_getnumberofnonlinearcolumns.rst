.. aimms:function:: GMP::Instance::GetNumberOfNonlinearColumns(GMP)

.. _GMP::Instance::GetNumberOfNonlinearColumns:

GMP::Instance::GetNumberOfNonlinearColumns
==========================================

The function :aimms:func:`GMP::Instance::GetNumberOfNonlinearColumns` returns the
number of nonlinear columns of a generated mathematical program.

.. code-block:: aimms

    GMP::Instance::GetNumberOfNonlinearColumns(
         GMP             ! (input) a generated mathematical program
         )

Arguments
---------

    *GMP*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

Return Value
------------

    The function returns the number of nonlinear columns.

.. seealso::

    - The functions :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::GetNumberOfColumns` and :aimms:func:`GMP::Instance::GetNumberOfIntegerColumns`.
