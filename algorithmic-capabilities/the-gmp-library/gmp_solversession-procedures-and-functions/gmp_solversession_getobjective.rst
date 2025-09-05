.. aimms:function:: GMP::SolverSession::GetObjective(solverSession)

.. _GMP::SolverSession::GetObjective:

GMP::SolverSession::GetObjective
================================

The function :aimms:func:`GMP::SolverSession::GetObjective` returns the objective
function value associated with a solver session.

.. code-block:: aimms

    GMP::SolverSession::GetObjective(
         solverSession   ! (input) a solver session
         )

Arguments
---------

    *solverSession*
        An element in the set :aimms:set:`AllSolverSessions`.

Return Value
------------

    The objective function value associated with a solver session.

.. note::

    For multi-objective models, the objective value refers to the (blended) objective
    with the highest priority.

.. seealso::

    - :aimms:func:`GMP::SolverSession::Execute`.
    - :aimms:func:`GMP::SolverSession::GetBestBound`.
    - :aimms:func:`GMP::SolverSession::GetIterationsUsed`.
    - :aimms:func:`GMP::SolverSession::GetMemoryUsed`.
    - :aimms:func:`GMP::SolverSession::GetTimeUsed`.
    - :aimms:func:`GMP::SolverSession::SetObjective`.
