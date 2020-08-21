.. aimms:procedure:: GMP::Solver::InitializeEnvironment(solver, computeserver, port, password, priority, timeout, logfile)

.. _GMP::Solver::InitializeEnvironment:

GMP::Solver::InitializeEnvironment
==================================

| The procedure :aimms:func:`GMP::Solver::InitializeEnvironment` can be used to
  initialize a solver environment. By using the procedure
  ``GMP::Solver::FreeEnvironment`` you can free a solver environment; by
  using this procedure you can initialize it again.
| Normally AIMMS initializes solver environments at startup and frees
  them when it is closed. The procodures
  :aimms:func:`GMP::Solver::InitializeEnvironment` and
  ``GMP::Solver::FreeEnvironment`` can be used to initialize and free a
  solver environment multiple times inside one AIMMS sesstion. Both
  procedures are typically used for solvers running on a remote server
  or a cloud system.

.. code-block:: aimms

    GMP::Solver::InitializeEnvironment(
         solver,            ! (input) a solver
         [computeserver],   ! (input, optional) a string expression
         [port],            ! (input, optional) integer, default -1
         [password],        ! (input, optional) a string expression
         [priority],        ! (input, optional) integer, default 0
         [timeout],         ! (input, optional) integer, default -1
         [logfile]          ! (input, optional) a string expression
         )

Arguments
---------

    *solver*
        An element in the set :aimms:set:`AllSolvers`.

    *computeserver*
        A string containing a comma-separated list of compute servers. You can
        refer to compute server machines using their names or their IP
        addresses.

    *port*
        The port number used to connect to the compute server. Use the default
        value of -1, which indicates that the default port should be used,
        unless your server administrator has changed the recommended port
        settings.

    *password*
        The password for gaining access to the specified compute servers. Do not
        specify this argument if no password is required.

    *priority*
        The priority of the job. Priorities must be between -100 and 100, with a
        default value of 0. Higher priority jobs are chosen from the server job
        queue before lower priority jobs.

    *timeout*
        Job timeout (in seconds). If the job does not reach the front of the
        queue before the specified timeout, the call will exit with an error.
        Use the default value of -1 to indicate that the call should never
        timeout.

    *logfile*
        The name of the log file for this environment. If this argument is not
        specified then no log file will be created for this environment.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  If the solver environment is already initialized when this procedure
       is called, the solver environment will be freed first.

    -  This procedure can be used in combination with a normal solve
       statement.

    -  This procedure is only supported by GUROBI.

    -  If the *computeserver* argument is not specified then the compute
       server must be specified via a Gurobi client license key file.

    -  The optional arguments *port*, *password*, *priority*, *timeout* and
       *logfile* are only used if the optional argument *computeserver* is
       specified.

    -  A job with priority 100 runs immediately, bypassing the job queue and
       ignoring the job limit on the server. You should exercise caution
       with priority 100 jobs, since they can severely overload a server,
       which can cause jobs to fail, and in extreme cases can cause the
       server to crash.

    -  This procedure cannot be called inside a solver callback procedure.

    -  This procedure cannot be called if one of the solver sessions is
       asynchronous executing.

    -  Technical note: if the optional argument *computeserver* is specified
       then the Gurobi function ``GRBloadclientenv`` is called underneath,
       otherwise the Gurobi function ``GRBloadenv`` (if the AIMMS license
       features the Gurobi Link-only).

Example
-------

    .. code-block:: aimms

               GMP::Solver::InitializeEnvironment( 'Gurobi 9.0' );

               solve MP1;

               GMP::Solver::FreeEnvironment( 'Gurobi 9.0' );

               GMP::Solver::InitializeEnvironment( 'Gurobi 9.0', computeserver: "my.server.com",
                                                   priority: 10 );

               mgGMP := GMP::Instance::Generate( MP2 );
               GMP::Instance::Solve( myGMP );

               GMP::Solver::FreeEnvironment( 'Gurobi 9.0' );

.. seealso::

    The procedure :aimms:func:`GMP::Solver::FreeEnvironment`.
