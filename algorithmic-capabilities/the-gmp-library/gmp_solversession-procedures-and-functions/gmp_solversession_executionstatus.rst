.. aimms:function:: GMP::SolverSession::ExecutionStatus(solverSession)

.. _GMP::SolverSession::ExecutionStatus:

GMP::SolverSession::ExecutionStatus
===================================

The function :aimms:func:`GMP::SolverSession::ExecutionStatus` returns the
execution status of a solver session.

.. code-block:: aimms

    GMP::SolverSession::ExecutionStatus(
         solverSession     ! (input) a solver session
         )

Arguments
---------

    *solverSession*
        An element in the set :aimms:set:`AllSolverSessions`.

Return Value
------------

    An element in the set :aimms:set:`AllExecutionStatuses`. This set contains the following
    elements:

    -  NotStarted,

    -  Pending,

    -  Running,

    -  Interrupted,

    -  Finished.

.. seealso::

    The routines :aimms:func:`GMP::SolverSession::AsynchronousExecute`, :aimms:func:`GMP::SolverSession::Interrupt`, :aimms:func:`GMP::SolverSession::WaitForCompletion` and :aimms:func:`GMP::SolverSession::WaitForSingleCompletion`.
