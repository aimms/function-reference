.. aimms:procedure:: GMP::SolverSession::RejectIncumbent(solverSession)

.. _GMP::SolverSession::RejectIncumbent:

GMP::SolverSession::RejectIncumbent
===================================

The procedure :aimms:func:`GMP::SolverSession::RejectIncumbent` rejects the
integer solution found by a solver session during the solution process
of a MIP model.

.. code-block:: aimms

    GMP::SolverSession::RejectIncumbent(
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

    -  This procedure can only be called from within a ``CallbackCandidate``
       callback procedure.

    -  A ``CallbackCandidate`` callback procedure will only be called when
       solving mixed integer programs with CPLEX.

.. seealso::

    The procedure :aimms:func:`GMP::Instance::SetCallbackCandidate`. See :doc:`optimization-modeling-components/implementing-advanced-algorithms-for-mathematical-programs/managing-generated-mathematical-program-instances` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__ for
    more details on how to install a candidate callback procedure.
