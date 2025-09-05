.. aimms:procedure:: GMP::Instance::SetIterationLimit(GMP, iterations)

.. _GMP::Instance::SetIterationLimit:

GMP::Instance::SetIterationLimit
================================

The procedure :aimms:func:`GMP::Instance::SetIterationLimit` limits the number of
iterations that can be used to solve a generated mathematical program.

.. code-block:: aimms

    GMP::Instance::SetIterationLimit(
         GMP,             ! (input) a generated mathematical program
         iterations       ! (input) number of iterations
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *iterations*
        Maximum number of iterations allowed to solve the generated mathematical
        program.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. seealso::

    - The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::Solve`, :aimms:func:`GMP::Instance::SetCutoff`, :aimms:func:`GMP::Instance::SetMemoryLimit` and :aimms:func:`GMP::Instance::SetTimeLimit`.
