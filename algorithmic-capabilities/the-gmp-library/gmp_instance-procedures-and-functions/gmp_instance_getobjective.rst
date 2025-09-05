.. aimms:function:: GMP::Instance::GetObjective(GMP)

.. _GMP::Instance::GetObjective:

GMP::Instance::GetObjective
===========================

The function :aimms:func:`GMP::Instance::GetObjective` returns the current
objective function value of a generated mathematical program.

.. code-block:: aimms

    GMP::Instance::GetObjective(
         GMP             ! (input) a generated mathematical program
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

Return Value
------------

    In case of success, the function returns the current objective function
    value. Otherwise it returns ``UNDF``.

.. note::

    For multi-objective models, the objective value refers to the (blended) objective
    with the highest priority.

.. seealso::

    - The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::Solve` and :aimms:func:`GMP::Instance::GetBestBound`.
