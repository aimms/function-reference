.. aimms:procedure:: GMP::Instance::SetCallbackHeuristic(GMP, callback)

.. _GMP::Instance::SetCallbackHeuristic:

GMP::Instance::SetCallbackHeuristic
===================================

The procedure :aimms:func:`GMP::Instance::SetCallbackHeuristic` installs a
callback procedure that is called during the solution process of a MIP
model every time the subproblem has been solved to optimality.

.. code-block:: aimms

    GMP::Instance::SetCallbackHeuristic(
         GMP,            ! (input) a generated mathematical program
         callback        ! (input) an AIMMS procedure
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *callback*
        A reference to a procedure in the set :aimms:set:`AllIdentifiers`.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  This callback is not called when the subproblem is infeasible or cut
       off.

    -  The callback should supply the solver with a heuristically-derived
       integer solution.

    -  The callback procedure should have exactly one argument; a scalar
       input element parameter into the set :aimms:set:`AllSolverSessions`.

    -  The ``CallbackHeuristic`` callback procedure should have a return
       value of

       -  0, if you want the solution process to stop, or

       -  1, if you want the solution process to continue.

    -  To remove the callback the empty element should be used as the
       *callback* argument.

    -  A ``CallbackHeuristic`` callback procedure will only be called when
       solving mixed integer programs with CPLEX, Gurobi or ODH-CPLEX.

.. seealso::

   - The routines :aimms:func:`GMP::Solution::RetrieveFromSolverSession`, :aimms:func:`GMP::Solution::SendToModel`, :aimms:func:`GMP::Solution::RetrieveFromModel`, :aimms:func:`GMP::Solution::SendToSolverSession`, :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::SetCallbackAddCut`, :aimms:func:`GMP::Instance::SetCallbackAddLazyConstraint`, :aimms:func:`GMP::Instance::SetCallbackBranch`, :aimms:func:`GMP::Instance::SetCallbackCandidate` and :aimms:func:`GMP::Instance::SetCallbackIncumbent`.
