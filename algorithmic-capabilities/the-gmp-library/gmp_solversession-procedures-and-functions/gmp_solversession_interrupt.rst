.. aimms:procedure:: GMP::SolverSession::Interrupt(solverSession, timeout)

.. _GMP::SolverSession::Interrupt:

GMP::SolverSession::Interrupt
=============================

The procedure :aimms:func:`GMP::SolverSession::Interrupt` interrupts a solver
session that is (asynchronous) executing.

.. code-block:: aimms

    GMP::SolverSession::Interrupt(
         solverSession,    ! (input) a solver session
         [timeout]         ! (optional) timeout interval
         )

Arguments
---------

    *solverSession*
        An element in the set :aimms:set:`AllSolverSessions`.

    *timeout*
        A scalar value indicating the time-out interval (in seconds). The
        default value is 600.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  This interrupt procedure will wait until the solver session is
       successfully interrupted or the time-out interval elapses.

    -  This procedure can also be called for a solver session that is not
       asynchronous executing. In that case the *timeout* argument will be
       ignored.

.. seealso::

    The routines :aimms:func:`GMP::SolverSession::AsynchronousExecute`, :aimms:func:`GMP::SolverSession::ExecutionStatus`, :aimms:func:`GMP::SolverSession::Interrupt`, :aimms:func:`GMP::SolverSession::WaitForCompletion` and :aimms:func:`GMP::SolverSession::WaitForSingleCompletion`.
