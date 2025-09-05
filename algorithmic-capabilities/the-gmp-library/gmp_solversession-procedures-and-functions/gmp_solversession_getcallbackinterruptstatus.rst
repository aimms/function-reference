.. aimms:function:: GMP::SolverSession::GetCallbackInterruptStatus(solverSession)

.. _GMP::SolverSession::GetCallbackInterruptStatus:

GMP::SolverSession::GetCallbackInterruptStatus
==============================================

The function :aimms:func:`GMP::SolverSession::GetCallbackInterruptStatus` returns
the type of the last callback function that had been called during a
specific solver session.

.. code-block:: aimms

    GMP::SolverSession::GetCallbackInterruptStatus(
         solverSession   ! (input) a solver session
         )

Arguments
---------

    *solverSession*
        An element in the set :aimms:set:`AllSolverSessions`.

Return Value
------------

    An element in the set :aimms:set:`AllSolverInterrupts`.

.. note::

    When the solver session has not yet been executed, the empty element
    will be returned.

.. seealso::

    - :aimms:func:`GMP::SolverSession::Execute`. 
    - :aimms:func:`GMP::Instance::SetCallbackAddCut`. 
    - :aimms:func:`GMP::Instance::SetCallbackAddLazyConstraint`. 
    - :aimms:func:`GMP::Instance::SetCallbackBranch`. 
    - :aimms:func:`GMP::Instance::SetCallbackCandidate`.
    - :aimms:func:`GMP::Instance::SetCallbackIncumbent`. 
    - :aimms:func:`GMP::Instance::SetCallbackIterations`. 
    - :aimms:func:`GMP::Instance::SetCallbackHeuristic`. 
    - :aimms:func:`GMP::Instance::SetCallbackStatusChange`.
    - :aimms:func:`GMP::Instance::SetCallbackTime`.
