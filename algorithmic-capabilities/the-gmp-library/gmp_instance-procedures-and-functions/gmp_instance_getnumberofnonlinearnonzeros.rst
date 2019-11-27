.. aimms:function:: GMP::Instance::GetNumberOfNonlinearNonzeros(GMP)

.. _GMP::Instance::GetNumberOfNonlinearNonzeros:

GMP::Instance::GetNumberOfNonlinearNonzeros
===========================================

The function :aimms:func:`GMP::Instance::GetNumberOfNonlinearNonzeros` returns the
number of nonlinear nonzero elements in the coefficient matrix of a
generated mathematical program.

.. code-block:: aimms

    GMP::Instance::GetNumberOfNonlinearNonzeros(
         GMP             ! (input) a generated mathematical program
         )

Arguments
---------

    *GMP*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

Return Value
------------

    The function returns the number of nonlinear nonzeros.

.. seealso::

    The functions :aimms:func:`GMP::Instance::Generate` and :aimms:func:`GMP::Instance::GetNumberOfNonzeros`.
