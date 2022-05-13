.. aimms:procedure:: GMP::SolverSession::GenerateBinaryEliminationRow(solverSession, solution, branch)

.. _GMP::SolverSession::GenerateBinaryEliminationRow:

GMP::SolverSession::GenerateBinaryEliminationRow
================================================

The procedure :aimms:func:`GMP::SolverSession::GenerateBinaryEliminationRow` adds
a binary row to a solver session which will eliminate a binary solution.

.. code-block:: aimms

    GMP::SolverSession::GenerateBinaryEliminationRow(
         solverSession,    ! (input) a solver session
         solution,         ! (input) a solution
         branch            ! (input) a scalar value
         )

Arguments
---------

    *solverSession*
        An element in the set :aimms:set:`AllSolverSessions`.

    *solution*
        An integer scalar reference to a solution.

    *branch*
        An integer scalar reference to a branch. Value should be either 1 or 2.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  This procedure will fail if the GMP corresponding to the solver
       session does not have model type MIP.

    -  This procedure can only be called from within a ``CallbackBranch``,
       ``CallbackAddCut`` or ``CallbackAddLazyConstraint`` callback
       procedure.

    -  The *branch* argument will be ignored if this procedure is called
       from within a ``CallbackAddCut`` or ``CallbackAddLazyConstraint``
       callback procedure.

    -  Every call to :aimms:func:`GMP::SolverSession::GenerateBinaryEliminationRow`
       adds the following row:

       .. math::
          :label: eq:gber1

          \begin{aligned}
           \sum_{i\in S_{lo}} x_i - \sum_{i\in S_{up}} x_i \geq 1 - \sum_{i\in S_{up}} lev_i  \end{aligned}

       \ where :math:`S_{lo}` defines the set of binary columns whose level
       values equals 0 and :math:`S_{up}` the set of binary columns whose
       level values equals 1.

Example
-------

    The procedure :aimms:func:`GMP::SolverSession::GenerateBinaryEliminationRow` can
    be used to enforce a MIP solver to branch a node that would have been
    fathomed otherwise. We can achieve this by installing a branching
    callback using procedure :aimms:func:`GMP::Instance::SetCallbackBranch` and adding
    the following code to the callback procedure: 

    .. code-block:: aimms

               ! Get LP solution at the current node.

               GMP::Solution::RetrieveFromSolverSession(ThisSession,1);

               ! Get the number of nodes that the MIP solver wants to create from the
               ! current branch.

               NrBranches := GMP::SolverSession::GetNumberOfBranchNodes(ThisSession);

               if ( NrBranches = 0 ) then

                   ! The LP solution at the current node appears to be integer feasible.
                   ! We enforce the MIP solver to branch the current node by creating a
                   ! branch containing one constraint that cuts off this LP solution.

                   GMP::SolverSession::GenerateBinaryEliminationRow(ThisSession,1,1);

               endif;
               
               return 1;

    Here
    'ThisSession' is an input argument of the callback procedure and a
    scalar element parameter into the set :aimms:set:`AllSolverSessions`.

.. seealso::

    The routines :aimms:func:`GMP::Instance::AddIntegerEliminationRows`, :aimms:func:`GMP::Instance::SetCallbackAddCut`, :aimms:func:`GMP::Instance::SetCallbackBranch`, :aimms:func:`GMP::Instance::SetCallbackAddLazyConstraint` and :aimms:func:`GMP::SolverSession::GetNumberOfBranchNodes`.
