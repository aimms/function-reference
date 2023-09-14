.. aimms:function:: GMP::Solution::GetObjective(GMP, solution)

.. _GMP::Solution::GetObjective:

GMP::Solution::GetObjective
===========================

The function :aimms:func:`GMP::Solution::GetObjective` retrieves the objective
function value of a solution in the solution repository of a generated
mathematical program.

.. code-block:: aimms

    GMP::Solution::GetObjective(
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

    The objective function value of the solution.

.. note::

    -  The objective function value is only available if the solution has been
       retrieved from the solver, or if the function
       ``GMP::Solution::SetObjective`` has been called before.

    -  For multi-objective models, the objective value refers to the (blended) objective
       with the highest priority.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Solution::GetProgramStatus`, :aimms:func:`GMP::Solution::GetSolverStatus` and :aimms:func:`GMP::Solution::SetObjective`.
