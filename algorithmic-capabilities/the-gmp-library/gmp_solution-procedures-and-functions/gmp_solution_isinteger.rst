.. aimms:function:: GMP::Solution::IsInteger(GMP, solution, tolerance)

.. _GMP::Solution::IsInteger:

GMP::Solution::IsInteger
========================

The function :aimms:func:`GMP::Solution::IsInteger` checks whether the solution
for a generated mathematical program is an integer solution.

.. code-block:: aimms

    GMP::Solution::IsInteger(
         GMP,            ! (input) a generated mathematical program
         solution,       ! (input) a solution
         [tolerance]     ! (optional) a tolerance
         )

Arguments
---------

    *GMP*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

    *solution*
        An integer scalar reference to a solution.

    *tolerance*
        A numerical value. The default is 0.

Return Value
------------

    The function returns 1 if the solution is integer, and 0 otherwise.

.. note::

    If the mathematical program contains Special Ordered Sets (SOS) then
    this function also checks whether the solution satisfies them. If one of
    the SOS sets is violated then this function returns 0.

.. seealso::

    - The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Solution::RetrieveFromModel` and :aimms:func:`GMP::Solution::RetrieveFromSolverSession`.
