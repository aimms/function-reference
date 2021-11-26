.. aimms:function:: GMP::SolverSession::WaitForSingleCompletion(Objects)

.. _GMP::SolverSession::WaitForSingleCompletion:

GMP::SolverSession::WaitForSingleCompletion
===========================================

The routine :aimms:func:`GMP::SolverSession::WaitForSingleCompletion` has a set of
objects as its input. The set of objects may contain solver sessions
that are asynchronous executing and events. This routine lets AIMMS
waits until one of the solver sessions has completed its asynchronous
execution or one of the events gets activated, and it returns the
completed object.

.. code-block:: aimms

    GMP::SolverSession::WaitForSingleCompletion(
         Objects           ! (input) a set of objects
         )

Arguments
---------

    *Objects*
        A subset of :aimms:set:`AllSolverSessionCompletionObjects`.

Return Value
------------

    An element in the set :aimms:set:`AllSolverSessionCompletionObjects`.

.. note::

    -  This routine ignores solver sessions that are not asynchronous
       executing but using the procedure :aimms:func:`GMP::SolverSession::Execute`.

    -  This routine will return immediately if one of the objects is a
       solver session that has execution status 'Finished'.

.. seealso::

    The routines :aimms:func:`GMP::Event::Create`, :aimms:func:`GMP::Event::Set`, :aimms:func:`GMP::SolverSession::AsynchronousExecute`, :aimms:func:`GMP::SolverSession::Execute`, :aimms:func:`GMP::SolverSession::ExecutionStatus`,
    :aimms:func:`GMP::SolverSession::Interrupt` and :aimms:func:`GMP::SolverSession::WaitForCompletion`.
