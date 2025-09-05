.. aimms:procedure:: GMP::Solution::SetMIPStartFlag(GMP, solution, flag, effortLevel)

.. _GMP::Solution::SetMIPStartFlag:

GMP::Solution::SetMIPStartFlag
==============================

The procedure :aimms:func:`GMP::Solution::SetMIPStartFlag` can be used to mark a
solution in the solution repository of a generated mathematical program
such that it should be used as a MIP start during the a MIP solve (or a
MIQP or MIQCP solve).

.. code-block:: aimms

    GMP::Solution::SetMIPStartFlag(
         GMP,            ! (input) a generated mathematical program
         solution,       ! (input) a solution
         flag,           ! (input) a scalar value
         [effortLevel]   ! (optional, default 0) a scalar value
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *solution*
        An integer scalar reference to a solution.

    *flag*
        A scalar binary value to indicate whether the solution should be marked
        (value 1) or unmarked (value 0) as MIP start.

    *effortLevel*
        A scalar value to specify the level of effort that the solver should
        apply to the solution when using it as MIP start solution. The default
        value of 0 indicates that the solver should decide; the other values are
        explained below.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  This procedure is only supported by CPLEX, Gurobi and COPT.
    
    -  The argument *effortLevel* is only used by CPLEX.
    
    -  The levels of effort and their effect as specified by argument
       *effortLevel* are:

       -  Level 0: The solver decides.

       -  Level 1: The solver checks feasibility of the corresponding MIP
          start.

       -  Level 2: The solver solves the fixed LP problem specified by the
          MIP start.

       -  Level 3: The solver solves a subMIP.

       -  Level 4: The solver attempts to repair the MIP start if it is
          infeasible.

       -  Level 5: A complete solution is injected without the solver
          performing the usual checks. If the solution defined by the MIP
          start is infeasible, behavior is undefined.

.. seealso::

    - The routines :aimms:func:`GMP::Instance::Generate`.
