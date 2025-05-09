.. aimms:procedure:: GMP::Solver::SetEnvironmentIntegerParameter(solver, parameter, value)

.. _GMP::Solver::SetEnvironmentIntegerParameter:

GMP::Solver::SetEnvironmentIntegerParameter
===========================================

| The procedure :aimms:func:`GMP::Solver::SetEnvironmentIntegerParameter` can be used to
  set a integer-valued parameter to be used for starting a solver environment. This
  procedure is typically used for solvers running on a remote server or a cloud system.

.. code-block:: aimms

    GMP::Solver::SetEnvironmentIntegerParameter(
         solver,            ! (input) a solver
         parameter,         ! (input) a string expression
         value              ! (input) a numerical expression
         )

Arguments
---------

    *solver*
        An element in the set :aimms:set:`AllSolvers`.

    *parameter*
        The name of the parameter.

    *value*
        The desired value of the parameter.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  This procedure is only supported by Gurobi. Typically it is only used in combination
       with a Gurobi link-only license.

    -  This procedure cannot be called inside a solver callback procedure.

Parameters
----------

    This procedure and the procedures :aimms:func:`GMP::Solver::SetEnvironmentDoubleParameter` and :aimms:func:`GMP::Solver::SetEnvironmentStringParameter`
    can be used to set Gurobi `Configuration Parameters <https://docs.gurobi.com/projects/optimizer/en/current/concepts/parameters/groups.html#secparametergroups>`__. Typically
    these procedures are used to set Gurobi parameters for
    `Cloud <https://docs.gurobi.com/projects/optimizer/en/current/concepts/parameters/groups.html#instant-cloud>`__,
    `Compute Server <https://docs.gurobi.com/projects/optimizer/en/current/concepts/parameters/groups.html#compute-server>`__,
    `Cluster Manager <https://docs.gurobi.com/projects/optimizer/en/current/concepts/parameters/groups.html#cluster-manager>`__ or
    `Token Server <https://docs.gurobi.com/projects/optimizer/en/current/concepts/parameters/groups.html#token-server>`__.
    Note that normally these parameters are set in the Gurobi license file.

Example
-------

    .. code-block:: aimms

               MIPSolver := 'Gurobi 12.0';
               
               GMP::Solver::SetEnvironmentStringParameter( MIPSolver, "ComputeServer", "myserver1:61000" );
               GMP::Solver::SetEnvironmentIntegerParameter( MIPSolver, "ServerTimeout", 30 );

               GMP::Solver::InitializeEnvironment( MIPSolver );

               solve MP1;

               GMP::Solver::FreeEnvironment( MIPSolver );

.. seealso::

    The procedures :aimms:func:`GMP::Solver::InitializeEnvironment`, :aimms:func:`GMP::Solver::SetEnvironmentDoubleParameter` and :aimms:func:`GMP::Solver::SetEnvironmentStringParameter`.
