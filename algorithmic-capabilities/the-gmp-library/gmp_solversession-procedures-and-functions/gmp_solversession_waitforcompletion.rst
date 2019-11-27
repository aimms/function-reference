.. aimms:procedure:: GMP::SolverSession::WaitForCompletion(solSesSet)

.. _GMP::SolverSession::WaitForCompletion:

GMP::SolverSession::WaitForCompletion
=====================================

The procedure :aimms:func:`GMP::SolverSession::WaitForCompletion` has a set of
objects as its input. The set of objects may contain solver sessions
that are asynchronous executing and events. This procedure lets AIMMS
wait until all the solver sessions have completed their asynchronous
execution and all the events get activated.

.. code-block:: aimms

    GMP::SolverSession::WaitForCompletion(
         solSesSet           ! (input) a set of objects
         )

Arguments
---------

    *solSesSet*
        A subset of :aimms:set:`AllSolverSessionCompletionObjects`.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    This procedure ignores solver sessions that are not asynchronous
    executing but using the procedure ``GMP::SolverSession::Execute``.

.. seealso::

    The routines :aimms:func:`GMP::Event::Create`, :aimms:func:`GMP::Event::Set`, :aimms:func:`GMP::SolverSession::AsynchronousExecute`, :aimms:func:`GMP::SolverSession::Execute`, :aimms:func:`GMP::SolverSession::ExecutionStatus`,
    :aimms:func:`GMP::SolverSession::Interrupt` and :aimms:func:`GMP::SolverSession::WaitForSingleCompletion`.
