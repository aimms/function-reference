.. aimms:function:: GMP::Instance::GetDirection(GMP)

.. _GMP::Instance::GetDirection:

GMP::Instance::GetDirection
===========================

The function :aimms:func:`GMP::Instance::GetDirection` returns the optimization
direction of a generated mathematical program.

.. code-block:: aimms

    GMP::Instance::GetDirection(
         GMP             ! (input) a generated mathematical program
         )

Arguments
---------

    *GMP*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

Return Value
------------

    The function returns the optimization direction as an element in
    :aimms:set:`AllMatrixManipulationDirections`.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate` and the procedure :aimms:func:`GMP::Instance::SetDirection`.
