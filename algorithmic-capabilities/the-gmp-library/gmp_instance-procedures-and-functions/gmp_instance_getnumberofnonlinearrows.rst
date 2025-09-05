.. aimms:function:: GMP::Instance::GetNumberOfNonlinearRows(GMP)

.. _GMP::Instance::GetNumberOfNonlinearRows:

GMP::Instance::GetNumberOfNonlinearRows
=======================================

The function :aimms:func:`GMP::Instance::GetNumberOfNonlinearRows` returns the
number of nonlinear rows of a generated mathematical program.

.. code-block:: aimms

    GMP::Instance::GetNumberOfNonlinearRows(
         GMP             ! (input) a generated mathematical program
         )

Arguments
---------

    *GMP*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

Return Value
------------

    The function returns the number of nonlinear rows.

.. seealso::

    - The functions :aimms:func:`GMP::Instance::Generate` and :aimms:func:`GMP::Instance::GetNumberOfRows`.
