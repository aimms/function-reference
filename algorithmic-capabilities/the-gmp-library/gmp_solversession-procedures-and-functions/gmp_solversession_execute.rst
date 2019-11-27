.. aimms:procedure:: GMP::SolverSession::Execute(solverSession)

.. _GMP::SolverSession::Execute:

GMP::SolverSession::Execute
===========================

The procedure :aimms:func:`GMP::SolverSession::Execute` invokes the solution
algorithm to solve the mathematical program for which it had been
generated.

.. code-block:: aimms

    GMP::SolverSession::Execute(
         solverSession   ! (input) a solver session
         )

Arguments
---------

    *solverSession*
        An element in the set :aimms:set:`AllSolverSessions`.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  This procedure will not copy the initial solution into the solver, or
       copy the final solution back into solution repository or model
       identifiers. When you use this function you always have to explicitly
       call functions from the ``GMP::Solution`` namespace to accomplish
       these tasks.

    -  This procedure does not create a listing file but you can use the
       procedure ``GMP::Solution::ConstraintListing`` for that.

.. seealso::

    The routines :aimms:func:`GMP::Instance::CreateSolverSession`, :aimms:func:`GMP::Instance::Solve`, :aimms:func:`GMP::SolverSession::AsynchronousExecute` and :aimms:func:`GMP::Solution::ConstraintListing`.
