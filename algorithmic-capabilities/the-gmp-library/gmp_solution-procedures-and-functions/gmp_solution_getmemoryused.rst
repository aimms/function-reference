.. aimms:function:: GMP::Solution::GetMemoryUsed(GMP, solution)

.. _GMP::Solution::GetMemoryUsed:

GMP::Solution::GetMemoryUsed
============================

The function :aimms:func:`GMP::Solution::GetMemoryUsed` returns the amount of
(peak) memory used to create a solution in the solution repository of a
generated mathematical program.

.. code-block:: aimms

    GMP::Solution::GetMemoryUsed(
         GMP,            ! (input) a generated mathematical program
         solution        ! (input) a solution
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *solution*
        An integer scalar reference to a solution.

Return Value
------------

    The amount of megabytes used to create a solution.

.. note::

    For CPLEX and Gurobi, AIMMS calculates the memory in use
    based on the virtual memory used by the process. This approach is not
    reliable for asynchronous solver sessions.

.. seealso::

    The procedure :aimms:func:`GMP::Instance::SetMemoryLimit`.
