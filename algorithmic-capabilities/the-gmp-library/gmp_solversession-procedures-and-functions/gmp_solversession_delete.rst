.. aimms:procedure:: GMP::SolverSession::Delete(solverSession)

.. _GMP::SolverSession::Delete:

GMP::SolverSession::Delete
==========================

The procedure :aimms:func:`GMP::SolverSession::Delete` deletes the
specified solver session.

.. code-block:: aimms

    GMP::SolverSession::Delete(
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

    This procedure was added in AIMMS version 25.7, and replaces the deprecated procedure ``GMP::Instance::DeleteSolverSession``.

.. seealso::

    - The functions :aimms:func:`GMP::Instance::CreateSolverSession` and :aimms:func:`GMP::SolverSession::GetInstance`.
