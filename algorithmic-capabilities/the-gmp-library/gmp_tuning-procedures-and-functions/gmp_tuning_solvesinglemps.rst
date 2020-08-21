.. aimms:procedure:: GMP::Tuning::SolveSingleMPS(FileName, Solver, SolverStatus, ProgramStatus, Objective, Iterations, Nodes, SolutionTime, SolutionFile)

.. _GMP::Tuning::SolveSingleMPS:

GMP::Tuning::SolveSingleMPS
===========================

The procedure :aimms:func:`GMP::Tuning::SolveSingleMPS` solves a MPS, LP or SAV
file.

.. code-block:: aimms

    GMP::Tuning::SolveSingleMPS(
         FileName,             ! (input) scalar string expression
         Solver,               ! (input) scalar element parameter
         SolverStatus,         ! (output) scalar element parameter
         ProgramStatus,        ! (output) scalar element parameter
         Objective,            ! (output) scalar numerical parameter
         Iterations,           ! (output) scalar numerical parameter
         Nodes,                ! (output) scalar numerical parameter
         SolutionTime,         ! (output) scalar numerical parameter
         [SolutionFile]        ! (optional) a scalar numerical expression
    )

Arguments
---------

    *FileName*
        The name of the file, with file format '.mps', '.lp' or '.sav', to be
        solved.

    *Solver*
        An element in the set :aimms:set:`AllSolvers`.

    *SolverStatus*
        The solver status as an element in the set :aimms:set:`AllSolutionStates`.

    *ProgramStatus*
        The program status as an element in the set :aimms:set:`AllSolutionStates`.

    *Objective*
        The objective value returned by the solver.

    *Iterations*
        The number of iterations used by the solver to solve the model.

    *Nodes*
        The number of nodes used by the solver to solve the model.

    *SolutionTime*
        The solution time (in seconds) used by the solver to solve the model.

    *SolutionFile*
        A 0-1 value indicating whether a solution file should be created. If 1,
        then the solution file will be named '\ *FileName*.sol'. The default is
        0.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  The solver will use the option settings as specified in the AIMMS
       project.

    -  This procedure is supported by the solvers CPLEX, GUROBI, CBC,
       ODH-CPLEX and XA. XA does not support the LP format. Only CPLEX
       supports the SAV format.

Example
-------

    To solve model 'mod1.mps' using CPLEX 12.10 execute: 

    .. code-block:: aimms

               GMP::Tuning::SolveSingleMPS( 'mod1.mps', 'CPLEX 12.10', SolStat, ProStat, obj, iter,
                                            nodes, soltime );

.. seealso::

    The routine :aimms:func:`GMP::Tuning::TuneMultipleMPS`.
