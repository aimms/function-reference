.. aimms:function:: GMP::Solution::GetIterationsUsed(GMP, solution)

.. _GMP::Solution::GetIterationsUsed:

GMP::Solution::GetIterationsUsed
================================

The function :aimms:func:`GMP::Solution::GetIterationsUsed` returns the number of
iterations used to create a solution in the solution repository of a
generated mathematical program.

.. code-block:: aimms

    GMP::Solution::GetIterationsUsed(
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

    The number of iterations used to create a solution.

.. seealso::

    - The procedures :aimms:func:`GMP::Instance::SetIterationLimit` and :aimms:func:`GMP::Solution::SetIterationCount`.
