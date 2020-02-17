.. aimms:function:: GMP::SolverSession::GetMemoryUsed(solverSession)

.. _GMP::SolverSession::GetMemoryUsed:

GMP::SolverSession::GetMemoryUsed
=================================

| The function :aimms:func:`GMP::SolverSession::GetMemoryUsed` returns the amount
  of memory used by the solver session.
| During a solve this function returns the current amount of memory used
  by the solver. After the solve, this function returns the peak memory
  used by the solver.

.. code-block:: aimms

    GMP::SolverSession::GetMemoryUsed(
         solverSession   ! (input) a solver session
         )

Arguments
---------

    *solverSession*
        An element in the set :aimms:set:`AllSolverSessions`.

Return Value
------------

    The amount of megabytes used to execute a solver session.

.. note::

    -  This function should be called inside a callback procedure to
       retrieve the current amount of memory used by the solver during a
       solve.

    -  During a solve, the memory used by the solver can fluctuate.
    
    -  For CPLEX and GUROBI, AIMMS calculates the memory in use
       based on the virtual memory used by the process. This approach is not
       reliable for asynchronous solver sessions.

.. seealso::

    The routines :aimms:func:`GMP::Instance::SetCallbackIterations`, :aimms:func:`GMP::Instance::SetCallbackTime`, :aimms:func:`GMP::Instance::SetMemoryLimit`, :aimms:func:`GMP::SolverSession::Execute`, :aimms:func:`GMP::SolverSession::GetIterationsUsed` and
    :aimms:func:`GMP::SolverSession::GetTimeUsed`.
