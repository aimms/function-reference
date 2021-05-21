.. aimms:procedure:: GMP::SolverSession::AsynchronousExecute(solverSession)

.. _GMP::SolverSession::AsynchronousExecute:

GMP::SolverSession::AsynchronousExecute
=======================================

The procedure :aimms:func:`GMP::SolverSession::AsynchronousExecute` invokes the
solution algorithm to asynchronous solve a generated mathematical
program by using a solver session.

.. code-block:: aimms

    GMP::SolverSession::AsynchronousExecute(
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

    -  The following solvers are thread-safe and can be used for solving
       multiple mathematical programs in parallel using the same solver:
       CPLEX, Gurobi, XA, CONOPT, and Knitro.

    -  The following solvers are not thread-safe but the AIMMS-solver
       interface is thread safe and therefore they can be used in parallel
       with another solver: IPOPT and SNOPT. For example, SNOPT 7.1 can be
       used in parallel with IPOPT but it cannot be used in parallel with
       SNOPT 7.1.

    -  The procedure :aimms:func:`GMP::SolverSession::AsynchronousExecute` cannot be
       used by the following solvers: AOA, BARON, CBC, ODH-CPLEX, and PATH.

    -  Calling :aimms:func:`GMP::SolverSession::AsynchronousExecute` inside a callback
       procedure is not allowed.

    -  The procedure :aimms:func:`GMP::SolverSession::AsynchronousExecute` cannot be
       used if an external function is used in a constraint.

    -  The procedures ``GMP::SolverSession::WaitForCompletion`` and
       ``GMP::SolverSession::WaitForSingleCompletion`` can be used to let
       AIMMS wait until one or more asynchronous executing solver sessions
       are finished.

    -  Normal solve statements will be ignored during an asynchronous
       execution of a solver session.

    -  Sensitivity ranges will not be calculated during an asynchronous
       solve.

    -  This procedure does not create a listing file but you can use the
       procedure ``GMP::Solution::ConstraintListing`` for that.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Copy`, :aimms:func:`GMP::SolverSession::Execute`, :aimms:func:`GMP::SolverSession::ExecutionStatus` :aimms:func:`GMP::SolverSession::Interrupt`, :aimms:func:`GMP::SolverSession::WaitForCompletion`,
    :aimms:func:`GMP::SolverSession::WaitForSingleCompletion`, :aimms:func:`GMP::Solution::ConstraintListing` and :aimms:func:`GMP::Solver::GetAsynchronousSessionsLimit`.
