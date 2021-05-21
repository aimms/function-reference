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

    -  This function can be used for GMPs with model type MIP, MIQP or MIQCP.

    -  This function can also be used for GMPs solved with BARON,
       regardless of the model type.

    -  This function can also be used for GMPs with model type QP that are
       solved with CPLEX, if the CPLEX option *Solution Target* is set to
       'Search for global optimum'.

    -  This function can also be used for GMPs with model type QP or QCP that are
       solved with Gurobi 9.0 or higher, if the Gurobi option *Nonconvex Strategy*
       is set to 'Translate'.

.. seealso::

    The routines :aimms:func:`GMP::SolverSession::Execute`, :aimms:func:`GMP::SolverSession::GetObjective`, :aimms:func:`GMP::SolverSession::GetIterationsUsed`, :aimms:func:`GMP::SolverSession::GetMemoryUsed` and :aimms:func:`GMP::SolverSession::GetTimeUsed`.
