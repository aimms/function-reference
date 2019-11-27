.. aimms:procedure:: GMP::Instance::SetMemoryLimit(GMP, memory)

.. _GMP::Instance::SetMemoryLimit:

GMP::Instance::SetMemoryLimit
=============================

The procedure :aimms:func:`GMP::Instance::SetMemoryLimit` limits the amount of
memory available to solve a generated mathematical program.

.. code-block:: aimms

    GMP::Instance::SetMemoryLimit(
         GMP,             ! (input) a generated mathematical program
         memory           ! (input) amount of memory
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *memory*
        Maximum number of megabytes available to solve the generated
        mathematical program.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::Solve`, :aimms:func:`GMP::Instance::SetCutoff`, :aimms:func:`GMP::Instance::SetIterationLimit` and :aimms:func:`GMP::Instance::SetTimeLimit`.
