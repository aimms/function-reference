.. aimms:procedure:: GMP::SolverSession::SetObjective(solverSession, Value)

.. _GMP::SolverSession::SetObjective:

GMP::SolverSession::SetObjective
================================

The procedure :aimms:func:`GMP::SolverSession::SetObjective` sets the objective
value for the solution belonging to a solver session.

.. code-block:: aimms

    GMP::SolverSession::SetObjective(
         solverSession,    ! (input) a solver session
         Value             ! (input) a scalar numeric expression
         )

Arguments
---------

    *solverSession*
        An element in the set :aimms:set:`AllSolverSessions`.

    *Value*
        A scalar numeric expression representing the new value to be assigned as
        the objective value.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. seealso::

    - The routine :aimms:func:`GMP::SolverSession::Execute` and :aimms:func:`GMP::SolverSession::GetObjective`.
