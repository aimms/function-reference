.. aimms:function:: GMP::Instance::GetSolver(GMP)

.. _GMP::Instance::GetSolver:

GMP::Instance::GetSolver
========================

The function :aimms:func:`GMP::Instance::GetSolver` returns for a generated
mathematical program the solver that is assigned to it.

.. code-block:: aimms

    GMP::Instance::GetSolver(
         GMP             ! (input) a generated mathematical program
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

Return Value
------------

    The function returns the solver as an element of :aimms:set:`AllSolvers`.

.. note::

    The solver can be assigned by the procedure
    :aimms:func:`GMP::Instance::SetSolver`, or derived by AIMMS as the default solver
    for the model class of the generated mathematical program.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate` and :aimms:func:`GMP::Instance::SetSolver`.
