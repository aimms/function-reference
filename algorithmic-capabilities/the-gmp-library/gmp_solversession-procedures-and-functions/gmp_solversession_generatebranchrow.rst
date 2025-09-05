.. aimms:procedure:: GMP::SolverSession::GenerateBranchRow(solverSession, row, branch)

.. _GMP::SolverSession::GenerateBranchRow:

GMP::SolverSession::GenerateBranchRow
=====================================

The procedure :aimms:func:`GMP::SolverSession::GenerateBranchRow` adds a row to a
branch to be taken from the current node during MIP branch-and-cut.

.. code-block:: aimms

    GMP::SolverSession::GenerateBranchRow(
         solverSession,    ! (input) a solver session
         row,              ! (input) a scalar reference
         branch            ! (input) a branch number
         )

Arguments
---------

    *solverSession*
        An element in the set :aimms:set:`AllSolverSessions`.

    *row*
        A scalar reference to an existing row in the model.

    *branch*
        An integer scalar reference to the branch number. It should be equal to
        1 or 2.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  A branch can be specified by adding multiple rows and bound changes
       (with :aimms:func:`GMP::SolverSession::GenerateBranchLowerBound` and
       :aimms:func:`GMP::SolverSession::GenerateBranchUpperBound`) to the node
       problem.

    -  This procedure can only be called from within a ``CallbackBranch``
       callback procedure.

    -  A ``CallbackBranch`` callback procedure will only be called when
       solving mixed integer programs with CPLEX.

.. seealso::

    - :aimms:func:`GMP::Instance::SetCallbackBranch`.
    - :aimms:func:`GMP::SolverSession::GenerateBranchLowerBound`.
    - :aimms:func:`GMP::SolverSession::GenerateBranchUpperBound`.
