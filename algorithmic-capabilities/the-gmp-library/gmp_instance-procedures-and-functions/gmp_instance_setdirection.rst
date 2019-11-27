.. aimms:procedure:: GMP::Instance::SetDirection(GMP, direction)

.. _GMP::Instance::SetDirection:

GMP::Instance::SetDirection
===========================

The procedure :aimms:func:`GMP::Instance::SetDirection` changes the direction of a
generated mathematical program.

.. code-block:: aimms

    GMP::Instance::SetDirection(
         GMP,              ! (input) a generated mathematical program
         direction         ! (input) an optimization direction
         )

Arguments
---------

    *GMP*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

    *direction*
        An element expression in the set :aimms:set:`AllMatrixManipulationDirections`.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. seealso::

    The functions :aimms:func:`GMP::Instance::Generate` and :aimms:func:`GMP::Instance::GetDirection`.
