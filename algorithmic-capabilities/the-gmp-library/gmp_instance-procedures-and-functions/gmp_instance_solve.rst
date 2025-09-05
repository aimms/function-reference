.. aimms:procedure:: GMP::Instance::Solve(GMP)

.. _GMP::Instance::Solve:

GMP::Instance::Solve
====================

The procedure :aimms:func:`GMP::Instance::Solve` starts up a solver session to
solve a generated mathematical program. In addition, it copies the
initial solution from the model identifiers via solution 1 in the
solution repository and stores the final solution via solution 1 back in
the model identifiers.

.. code-block:: aimms

    GMP::Instance::Solve(
         GMP             ! (input) a generated mathematical program
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    The procedure :aimms:func:`GMP::Instance::Solve` automatically creates a solver
    session with the same name as the generated mathematical program in the
    set :aimms:set:`AllSolverSessions`.

.. seealso::

    - The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::CreateSolverSession`, :aimms:func:`GMP::Solution::RetrieveFromModel`, :aimms:func:`GMP::Solution::SendToSolverSession`, :aimms:func:`GMP::SolverSession::Execute`, :aimms:func:`GMP::Solution::RetrieveFromSolverSession` and :aimms:func:`GMP::Solution::SendToModel`.
