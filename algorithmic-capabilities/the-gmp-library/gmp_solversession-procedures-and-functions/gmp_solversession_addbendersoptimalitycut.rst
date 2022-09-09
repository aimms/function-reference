.. aimms:procedure:: GMP::SolverSession::AddBendersOptimalityCut(solverSession, GMP, solution, local, purgeable)

.. _GMP::SolverSession::AddBendersOptimalityCut:

GMP::SolverSession::AddBendersOptimalityCut
===========================================

The procedure :aimms:func:`GMP::SolverSession::AddBendersOptimalityCut` generates
an optimality cut for a Benders' master problem using the (dual)
solution of a Benders' subproblem. The Benders' master problem must be a
MIP problem. The cut is typically added as a lazy constraint in a
callback during the MIP branch-and-cut search. This procedure is typically
used in a Benders' decomposition algorithm in which a single master MIP
problem is solved.

.. code-block:: aimms

    GMP::SolverSession::AddBendersOptimalityCut(
         solverSession,    ! (input) a solver session
         GMP,              ! (input) a generated mathematical program
         solution,         ! (input) a solution
         [local],          ! (optional, default 0) a scalar binary expression
         [purgeable]       ! (optional, default 0) a scalar binary expression
    )

Arguments
---------

    *solverSession*
        An element in the set :aimms:set:`AllSolverSessions` representing a solver session for the
        Benders' master problem.

    *GMP*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms` representing a Benders' subproblem.

    *solution*
        An integer scalar reference to a solution of *GMP2*.

    *local*
        A scalar binary value to indicate whether the cut is valid for the local
        problem (i.e. the problem corresponding to the current node in the
        solution process and all its descendant nodes) only (value 1) or for the
        global problem (value 0).

    *purgeable*
        A scalar binary value to indicate whether the solver is allowed to purge
        the cut if it deems it ineffective. If the value is 1, then it is
        allowed.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  The generated mathematical program corresponding to the
       *solverSession* should have been created using the function
       :aimms:func:`GMP::Benders::CreateMasterProblem`.

    -  The *GMP* should have been created using the function
       :aimms:func:`GMP::Benders::CreateSubProblem`.

    -  The *solution* of the Benders' subproblem (represented by *GMP*) is
       used to generate an optimality cut for the Benders' master problem
       (represented by *solverSession*). More precise, the shadow prices of
       the constraints and the reduced costs of the variables in the
       Benders' subproblem are used.

    -  See :ref:`sec:benders.textbook.alg` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__ for more information about
       the Benders' decomposition algorithm in which a single master MIP
       problem is solved.

Example
-------

    In the example below we solve only one Benders' master problem (which is
    a MIP). During the solve, whenever the solver finds an integer
    (incumbent) solution we want to run a callback for lazy constraints.
    Therefore we install a callback for it. 

    .. code-block:: aimms

               myGMP := GMP::Instance::Generated( MP );

               gmpM := GMP::Benders::CreateMasterProblem( myGMP, AllIntegerVariables,
                                                          'BendersMasterProblem', 0, 0 );

               gmpS := GMP::Benders::CreateSubProblem( myGMP, masterGMP, 'BendersSubProblem',
                                                       0, 0 );

               GMP::Instance::SetCallbackAddLazyConstraint( gmpM, 'LazyCallback' );

               GMP::Instance::Solve( gmpM );

    The callback
    procedure ``LazyCallback`` has one argument, namely ``ThisSession``
    which is an element parameter with range :aimms:set:`AllSolverSessions`. Inside the callback
    procedure we solve the Benders' subproblem. We assume that the Benders'
    subproblem is always feasible. The program status of the subproblem is
    stored in the element parameter ``ProgramStatus`` with range :aimms:set:`AllSolutionStates`.
    Note that the subproblem is updated before it is solved. 

    .. code-block:: aimms

               ! Get MIP incumbent solution.
               GMP::Solution::RetrieveFromSolverSession( ThisSession, 1 );
               GMP::Solution::SendToModel( gmpM, 1 );

               GMP::Benders::UpdateSubProblem( gmpS, gmpM, 1, round : 1 );

               GMP::Instance::Solve( gmpS );

               ProgramStatus := GMP::Solution::GetProgramStatus( gmpS, 1 ) ;
               if ( ProgramStatus = 'Optimal' ) then
                   GMP::SolverSession::AddBendersOptimalityCut( ThisSession, gmpF, 1 );
               endif;

    In
    this example we skipped the check for optimality of the Benders'
    decomposition algorithm.

.. seealso::

    The routines :aimms:func:`GMP::Benders::CreateMasterProblem`, :aimms:func:`GMP::Benders::CreateSubProblem`, :aimms:func:`GMP::Benders::AddFeasibilityCut`, :aimms:func:`GMP::Benders::AddOptimalityCut` and :aimms:func:`GMP::SolverSession::AddBendersFeasibilityCut`.
