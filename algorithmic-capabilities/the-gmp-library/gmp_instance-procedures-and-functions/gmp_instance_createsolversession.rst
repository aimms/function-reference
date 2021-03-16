.. aimms:function:: GMP::Instance::CreateSolverSession(GMP, Name, Solver)

.. _GMP::Instance::CreateSolverSession:

GMP::Instance::CreateSolverSession
==================================

The function :aimms:func:`GMP::Instance::CreateSolverSession` creates a new solver
session for a generated mathematical program.

.. code-block:: aimms

    GMP::Instance::CreateSolverSession(
         GMP,              ! (input) a generated mathematical program
         [Name],           ! (input, optional) a string expression
         [Solver]          ! (input, optional) a solver
         )

Arguments
---------

    *GMP*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

    *Name*
        A string that holds the name of the solver session.

    *Solver*
        An element in the set :aimms:set:`AllSolvers`.

Return Value
------------

    The function returns an element in the set :aimms:set:`AllSolverSessions`.

.. note::

    -  The function :aimms:func:`GMP::Instance::CreateSolverSession` also determines
       which solver is assigned to the solver session. After the solver
       session is created it is not possible to change the solver assigned
       to the solver session! The solver is determined by:

       -  the *Solver* argument if it is specified (and not an empty
          string), else

       -  the solver that was assigned to the *GMP* if procedure
          ``GMP::Instance::SetSolver`` was called before, else

       -  the default solver in AIMMS for the GMP its model type.

    -  If the Name argument is not specified, or if it is the empty string,
       the names of the symbolic mathematical program, the solver and the
       host (if any) are used to create a new element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

    -  If an element with name specified by the *Name* argument is already
       present in the set :aimms:set:`AllSolverSessions` then the corresponding
       solver session will first be deleted.

.. seealso::

    The routines :aimms:func:`GMP::Instance::DeleteSolverSession`, :aimms:func:`GMP::Instance::SetSolver`, :aimms:func:`GMP::SolverSession::GetInstance` and :aimms:func:`GMP::SolverSession::GetSolver`.
