.. aimms:procedure:: GMP::Solver::FreeEnvironment(solver)

.. _GMP::Solver::FreeEnvironment:

GMP::Solver::FreeEnvironment
============================

| The procedure :aimms:func:`GMP::Solver::FreeEnvironment` can be used to free a
  solver environment. By using the procedure
  :aimms:func:`GMP::Solver::InitializeEnvironment` you can initialize a solver
  environment; by using this procedure you can free it again.
|
| Normally AIMMS initializes solver environments at startup and frees
  them when it is closed. The procodures
  :aimms:func:`GMP::Solver::InitializeEnvironment` and
  :aimms:func:`GMP::Solver::FreeEnvironment` can be used to initialize and free a
  solver environment multiple times inside one AIMMS sesstion. Both
  procedures are typically used for solvers running on a remote server
  or a cloud system.

.. code-block:: aimms

    GMP::Solver::FreeEnvironment(
         solver      ! (input) a solver
         )

Arguments
---------

    *solver*
        An element in the set :aimms:set:`AllSolvers`.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  This procedure can be used in combination with a normal solve
       statement.

    -  This procedure is only supported by Gurobi.

    -  This procedure cannot be called inside a solver callback procedure.

    -  This procedure cannot be called if one of the solver sessions is
       asynchronous executing.

Example
-------

    Assume that 'MIPSolver' is an element parameter with range :aimms:set:`AllSolvers`
    and 'myGMP' is an element parameter with range :aimms:set:`AllGeneratedMathematicalPrograms`.

    .. code-block:: aimms

               MIPSolver := 'Gurobi 12.0';

               ! First solve using normal solve statement.

               GMP::Solver::InitializeEnvironment( MIPSolver );

               solve MP1;

               GMP::Solver::FreeEnvironment( MIPSolver );

               ! Second solve using GMP solve.

               GMP::Solver::InitializeEnvironment( MIPSolver );

               mgGMP := GMP::Instance::Generate( MP2 );
               GMP::Instance::Solve( myGMP );

               GMP::Solver::FreeEnvironment( MIPSolver );

.. seealso::

    The procedure :aimms:func:`GMP::Solver::InitializeEnvironment`.
