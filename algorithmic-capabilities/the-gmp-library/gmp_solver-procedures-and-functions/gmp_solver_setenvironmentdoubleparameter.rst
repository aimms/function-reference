.. aimms:procedure:: GMP::Solver::SetEnvironmentDoubleParameter(solver, parameter, value)

.. _GMP::Solver::SetEnvironmentDoubleParameter:

GMP::Solver::SetEnvironmentDoubleParameter
==========================================

| The procedure :aimms:func:`GMP::Solver::SetEnvironmentDoubleParameter` can be used to
  set a double-valued parameter to be used for starting a solver environment. This
  procedure is typically used for solvers running on a remote server or a cloud system.

.. code-block:: aimms

    GMP::Solver::SetEnvironmentDoubleParameter(
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

    -  This procedure is only supported by Gurobi, version 9.1 or higher. Typically it is only used in combination
       with a Gurobi link-only license.

    -  This procedure cannot be called inside a solver callback procedure.

Parameters
----------

    This procedure and the procedures :aimms:func:`GMP::Solver::SetEnvironmentIntegerParameter` and :aimms:func:`GMP::Solver::SetEnvironmentStringParameter`
    can be used to set Gurobi `Configuration Parameters <https://docs.gurobi.com/projects/optimizer/en/11.0/concepts/parameters/groups.html#secparametergroups>`__. Typically
    these procedures are used to set Gurobi `Parameters <https://docs.gurobi.com/projects/optimizer/en/11.0/concepts/parameters/groups.html#secparametergroups>`__ for
    Cloud, Compute Server, Cluster Manager or Token Server. Note that normally these parameters are set in the Gurobi license file.

Example
-------

    .. code-block:: aimms

               MIPSolver := 'Gurobi 11.0';
               
               GMP::Solver::SetEnvironmentStringParameter( MIPSolver, "ComputeServer", "myserver1:61000" );
               GMP::Solver::SetEnvironmentDoubleParameter( MIPSolver, "CSQueueTimeout", 60 );
               GMP::Solver::SetEnvironmentDoubleParameter( MIPSolver, "MemLimit", 64 );

               GMP::Solver::InitializeEnvironment( MIPSolver );

               solve MP1;

               GMP::Solver::FreeEnvironment( MIPSolver );

.. seealso::

    The procedures :aimms:func:`GMP::Solver::InitializeEnvironment`, :aimms:func:`GMP::Solver::SetEnvironmentIntegerParameter` and :aimms:func:`GMP::Solver::SetEnvironmentStringParameter`.
