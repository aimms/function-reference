.. aimms:function:: GMP::SolverSession::GetBestBound(solverSession)

.. _GMP::SolverSession::GetBestBound:

GMP::SolverSession::GetBestBound
================================

The function :aimms:func:`GMP::SolverSession::GetBestBound` returns the best known
bound for a solver session.

.. code-block:: aimms

    GMP::SolverSession::GetBestBound(
         solverSession     ! (input) a solver session
         )

Arguments
---------

    *solverSession*
        An element in the set :aimms:set:`AllSolverSessions`.

Return Value
------------

    In case of success, the best known bound. Otherwise it returns ``UNDF``.

.. note::

    -  This function has only meaning for solver sessions with a
       corresponding generated mathematical program that has model type MIP,
       MIQP or MIQCP.

.. seealso::

    The routines :aimms:func:`GMP::SolverSession::Execute`, :aimms:func:`GMP::SolverSession::GetObjective`, :aimms:func:`GMP::SolverSession::GetIterationsUsed`, :aimms:func:`GMP::SolverSession::GetMemoryUsed` and :aimms:func:`GMP::SolverSession::GetTimeUsed`.
