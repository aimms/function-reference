.. aimms:procedure:: GMP::Instance::SetCutoff(GMP, cutoff)

.. _GMP::Instance::SetCutoff:

GMP::Instance::SetCutoff
========================

The procedure :aimms:func:`GMP::Instance::SetCutoff` specifies a cutoff value that
is used during the solution process of the generated mathematical
program.

.. code-block:: aimms

    GMP::Instance::SetCutoff(
         GMP,            ! (input) a generated mathematical program
         cutoff          ! (input) scalar numerical expression
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *cutoff*
        A scalar value.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    This procedure is only used for MIP models.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::Solve`, :aimms:func:`GMP::Instance::SetIterationLimit`, :aimms:func:`GMP::Instance::GMP::Instance::SetMemoryLimit` and :aimms:func:`GMP::Instance::SetTimeLimit`.
