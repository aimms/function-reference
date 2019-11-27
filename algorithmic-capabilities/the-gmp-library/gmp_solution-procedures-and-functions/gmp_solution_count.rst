.. aimms:function:: GMP::Solution::Count(GMP)

.. _GMP::Solution::Count:

GMP::Solution::Count
====================

The function :aimms:func:`GMP::Solution::Count` returns the number of non-empty
solutions in the solution repository of a generated mathematical
program.

.. code-block:: aimms

    GMP::Solution::Count(
         GMP             ! (input) a generated mathematical program
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

Return Value
------------

    The number of non-empty solutions stored in the solution repository.

.. note::

    In order to make the solution repository flexible, it may contain both
    feasible and infeasible solutions; any solution algorithm, or hybrid
    combinations thereof, may add or remove solutions.

.. seealso::

    The functions :aimms:func:`GMP::Instance::Generate` and :aimms:func:`GMP::Solution::GetSolutionsSet`.
