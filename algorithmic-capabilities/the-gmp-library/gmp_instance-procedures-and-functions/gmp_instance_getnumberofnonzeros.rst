.. aimms:function:: GMP::Instance::GetNumberOfNonzeros(GMP)

.. _GMP::Instance::GetNumberOfNonzeros:

GMP::Instance::GetNumberOfNonzeros
==================================

The function :aimms:func:`GMP::Instance::GetNumberOfNonzeros` returns the number
of nonzero elements in the coefficient matrix of a generated
mathematical program.

.. code-block:: aimms

    GMP::Instance::GetNumberOfNonzeros(
         GMP             ! (input) a generated mathematical program
         )

Arguments
---------

    *GMP*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

Return Value
------------

    The function returns the number of nonzeros.

.. seealso::

    The functions :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::GetNumberOfColumns` and :aimms:func:`GMP::Instance::GetNumberOfRows`.
