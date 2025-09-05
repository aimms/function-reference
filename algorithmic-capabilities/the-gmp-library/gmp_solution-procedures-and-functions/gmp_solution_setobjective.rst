.. aimms:procedure:: GMP::Solution::SetObjective(GMP, solution, value)

.. _GMP::Solution::SetObjective:

GMP::Solution::SetObjective
===========================

The procedure :aimms:func:`GMP::Solution::SetObjective` sets the objective
function value of a solution in the solution repository of a generated
mathematical program.

.. code-block:: aimms

    GMP::Solution::SetObjective(
         GMP,            ! (input) a generated mathematical program
         solution,       ! (input) a solution
         value           ! (input) a scalar value
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *solution*
        An integer scalar reference to a solution.

    *value*
        A scalar value to be assigned.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. seealso::

    - The functions :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Solution::GetObjective` and :aimms:func:`GMP::Solution::SendToModel`.
