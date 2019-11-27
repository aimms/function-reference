.. aimms:procedure:: GMP::Solver::FreeEnvironment(solver)

.. _GMP::Solver::FreeEnvironment:

GMP::Solver::FreeEnvironment
============================

| The procedure :aimms:func:`GMP::Solver::FreeEnvironment` can be used to free a
  solver environment. By using the procedure
  ``GMP::Solver::InitializeEnvironment`` you can initialize a solver
  environment; by using this procedure you can free it again.
| Normally AIMMS initializes solver environments at startup and frees
  them when it is closed. The procodures
  ``GMP::Solver::InitializeEnvironment`` and
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

    -  This procedure is only supported by GUROBI 7.0 or higher.

    -  This procedure cannot be called inside a solver callback procedure.

    -  This procedure cannot be called if one of the solver sessions is
       asynchronous executing.

Example
-------

    .. code-block:: aimms

               GMP::Solver::InitializeEnvironment( 'Gurobi 7.5' );

               solve MP1;

               GMP::Solver::FreeEnvironment( 'Gurobi 7.5' );

               GMP::Solver::InitializeEnvironment( 'Gurobi 7.5' );

               mgGMP := GMP::Instance::Generate( MP2 );
               GMP::Instance::Solve( myGMP );

               GMP::Solver::FreeEnvironment( 'Gurobi 7.5' );

.. seealso::

    The procedure :aimms:func:`GMP::Solver::InitializeEnvironment`.
