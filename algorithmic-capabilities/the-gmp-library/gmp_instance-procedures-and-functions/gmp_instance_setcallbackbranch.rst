.. aimms:procedure:: GMP::Instance::SetCallbackBranch(GMP, callback)

.. _GMP::Instance::SetCallbackBranch:

GMP::Instance::SetCallbackBranch
================================

The procedure :aimms:func:`GMP::Instance::SetCallbackBranch` installs a callback
procedure to be called after a branch has been selected but before the
branch is carried out during the MIP optimization. In the callback
routine, the branch selected by the solver can be changed to a
user-selected branch.

.. code-block:: aimms

    GMP::Instance::SetCallbackBranch(
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

    -  This callback is not called when the subproblem is infeasible.

    -  In the callback procedure at most 2 branches can be specified.

    -  The callback procedure should have exactly one argument; a scalar
       input element parameter into the set :aimms:set:`AllSolverSessions`.

    -  The ``CallbackBranch`` callback procedure should have a return value
       of

       -  0, if you want the solution process to stop, or

       -  1, if you want the solution process to continue.

    -  To remove the callback the empty element should be used as the
       *callback* argument.

    -  The ``CallbackBranch`` callback procedure cannot be used to get the
       column on which the solver will branch.

    -  A ``CallbackBranch`` callback procedure will only be called when
       solving mixed integer programs with CPLEX.

.. seealso::

    The routines :aimms:func:`GMP::Solution::RetrieveFromSolverSession`, :aimms:func:`GMP::Solution::SendToModel`, :aimms:func:`GMP::Solution::RetrieveFromModel`, :aimms:func:`GMP::Solution::SendToSolverSession`, :aimms:func:`GMP::SolverSession::GenerateBranchLowerBound`,
    :aimms:func:`GMP::SolverSession::GenerateBranchUpperBound`, :aimms:func:`GMP::SolverSession::GenerateBranchRow`, :aimms:func:`GMP::SolverSession::GetNumberOfBranchNodes`, :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::SetCallbackAddCut`, :aimms:func:`GMP::Instance::SetCallbackAddLazyConstraint`,
    :aimms:func:`GMP::Instance::SetCallbackCandidate`, :aimms:func:`GMP::Instance::SetCallbackHeuristic` and :aimms:func:`GMP::Instance::SetCallbackIncumbent`.
