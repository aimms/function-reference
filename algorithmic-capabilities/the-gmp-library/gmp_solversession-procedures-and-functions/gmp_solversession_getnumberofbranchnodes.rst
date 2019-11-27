.. aimms:function:: GMP::SolverSession::GetNumberOfBranchNodes(solverSession)

.. _GMP::SolverSession::GetNumberOfBranchNodes:

GMP::SolverSession::GetNumberOfBranchNodes
==========================================

The function :aimms:func:`GMP::SolverSession::GetNumberOfBranchNodes` returns the
number of nodes that the solver will create from the current branch.

.. code-block:: aimms

    GMP::SolverSession::GetNumberOfBranchNodes(
         solverSession   ! (input) a solver session
         )

Arguments
---------

    *solverSession*
        An element in the set :aimms:set:`AllSolverSessions`.

Return Value
------------

    The number of nodes that the solver will create from the current branch.

.. note::

    -  If the value returned equals 0, the node will be fathomed unless
       user-specified branches are made. That is, no child nodes are created
       and the node itself is discarded.

    -  This function has only meaning for solver sessions belonging to a GMP
       with type MIP, MIQP or MIQCP.

    -  This function can be used inside a **branch** callback.

.. seealso::

    The routines :aimms:func:`GMP::Instance::SetCallbackBranch`.
