.. aimms:procedure:: GMP::Instance::SetTimeLimit(GMP, seconds)

.. _GMP::Instance::SetTimeLimit:

GMP::Instance::SetTimeLimit
===========================

The procedure :aimms:func:`GMP::Instance::SetTimeLimit` limits the elapsed time to
solve a generated mathematical program.

.. code-block:: aimms

    GMP::Instance::SetTimeLimit(
         GMP,             ! (input) a generated mathematical program
         seconds          ! (input) number of seconds
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *seconds*
        Maximum number of seconds available to solve the generated mathematical
        program.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. seealso::

    - The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::Solve`, :aimms:func:`GMP::Instance::SetCutoff`, :aimms:func:`GMP::Instance::SetIterationLimit` and :aimms:func:`GMP::Instance::SetMemoryLimit`.
