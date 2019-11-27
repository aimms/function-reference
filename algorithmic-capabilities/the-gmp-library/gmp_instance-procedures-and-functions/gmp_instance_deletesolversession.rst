.. aimms:procedure:: GMP::Instance::DeleteSolverSession(solverSession)

.. _GMP::Instance::DeleteSolverSession:

GMP::Instance::DeleteSolverSession
==================================

The procedure :aimms:func:`GMP::Instance::DeleteSolverSession` deletes the
specified solver session.

.. code-block:: aimms

    GMP::Instance::DeleteSolverSession(
         solverSession      ! (input) a solver session
         )

Arguments
---------

    *solverSession*
        An element in the set :aimms:set:`AllSolverSessions`.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. seealso::

    The functions :aimms:func:`GMP::Instance::CreateSolverSession` and :aimms:func:`GMP::SolverSession::GetInstance`.
