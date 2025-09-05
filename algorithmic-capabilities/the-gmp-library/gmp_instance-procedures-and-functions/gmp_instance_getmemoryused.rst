.. aimms:function:: GMP::Instance::GetMemoryUsed(GMP)

.. _GMP::Instance::GetMemoryUsed:

GMP::Instance::GetMemoryUsed
============================

The function :aimms:func:`GMP::Instance::GetMemoryUsed` returns for a generated
mathematical program the amount of memory used by AIMMS to store it.

.. code-block:: aimms

    GMP::Instance::GetMemoryUsed(
         GMP             ! (input) a generated mathematical program
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

Return Value
------------

    - The amount of megabytes used to store a generated mathematical program.
