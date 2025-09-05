.. aimms:procedure:: GMP::SolverSession::GenerateBranchUpperBound(solverSession, column, bound, branch)

.. _GMP::SolverSession::GenerateBranchUpperBound:

GMP::SolverSession::GenerateBranchUpperBound
============================================

The procedure :aimms:func:`GMP::SolverSession::GenerateBranchUpperBound` specifies
the upper bound change of a column in a branch to be taken from the
current node during MIP branch-and-cut.

.. code-block:: aimms

    GMP::SolverSession::GenerateBranchUpperBound(
         solverSession,    ! (input) a solver session
         column,           ! (input) a scalar reference
         bound,            ! (input) a numerical expression
         branch            ! (input) a branch number
         )

Arguments
---------

    *solverSession*
        An element in the set :aimms:set:`AllSolverSessions`.

    *column*
        A scalar reference to an existing column in the model.

    *bound*
        The value assigned to the upper bound change of the column in the
        branch.

    *branch*
        An integer scalar reference to the branch number. It should be equal to
        1 or 2.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  A branch can be specified by adding multiple bound changes and rows
       (with :aimms:func:`GMP::SolverSession::GenerateBranchRow`) to the node problem.

    -  This procedure can only be called from within a ``CallbackBranch``
       callback procedure.

    -  A ``CallbackBranch`` callback procedure will only be called when
       solving mixed integer programs with CPLEX.

.. seealso::

    - :aimms:func:`GMP::Instance::SetCallbackBranch`.
    - :aimms:func:`GMP::SolverSession::GenerateBranchLowerBound`. 
    - :aimms:func:`GMP::SolverSession::GenerateBranchRow`.
