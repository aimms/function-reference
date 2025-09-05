.. aimms:function:: GMP::SolverSession::GetInstance(solverSession)

.. _GMP::SolverSession::GetInstance:

GMP::SolverSession::GetInstance
===============================

The function :aimms:func:`GMP::SolverSession::GetInstance` returns the generated
mathematical program that was used to create a solver session.

.. code-block:: aimms

    GMP::SolverSession::GetInstance(
         solverSession   ! (input) a solver session
         )

Arguments
---------

    *solverSession*
        An element in the set :aimms:set:`AllSolverSessions`.

Return Value
------------

    An element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

.. seealso::

    - :aimms:func:`GMP::Instance::Generate`.
    - :aimms:func:`GMP::Instance::CreateSolverSession`.
