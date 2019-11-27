.. aimms:procedure:: GMP::Benders::AddOptimalityCut(GMP1, GMP2, solution, cutNo)

.. _GMP::Benders::AddOptimalityCut:

GMP::Benders::AddOptimalityCut
==============================

The procedure :aimms:func:`GMP::Benders::AddOptimalityCut` generates an optimality
cut for a Benders' master problem using the (dual) solution of a
Benders' subproblem. This procedure is typically used in a Benders'
decomposition algorithm.

.. code-block:: aimms

    GMP::Benders::AddOptimalityCut(
         GMP1,             ! (input) a generated mathematical program
         GMP2,             ! (input) a generated mathematical program
         solution,         ! (input) a solution
         cutNo             ! (input) a scalar reference
    )

Arguments
---------

    *GMP1*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms` representing a Benders' master problem.

    *GMP2*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms` representing a Benders' subproblem.

    *solution*
        An integer scalar reference to a solution of *GMP2*.

    *cutNo*
        An integer scalar reference to a cut number.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  The *GMP1* should have been created using the function
       ``GMP::Benders::CreateMasterProblem``.

    -  The *GMP2* should have been created using the function
       ``GMP::Benders::CreateSubProblem``.

    -  The *solution* of the Benders' subproblem (represented by *GMP2*) is
       used to generate an optimality cut for the Benders' master problem
       (represented by *GMP1*). More precise, the shadow prices of the
       constraints and the reduced costs of the variables in the Benders'
       subproblem are used.

Example
-------

    In the example below we assume that the Benders' subproblem is feasible.
    Its program status is stored in the element parameter ``ProgramStatus``
    with range :aimms:set:`AllSolutionStates`. Note that the subproblem is updated before it is
    solved. 

    .. code-block:: aimms

               ! Initialization.
               myGMP := GMP::Instance::Generated( MP );

               gmpM := GMP::Benders::CreateMasterProblem( myGMP, AllIntegerVariables,
                                                          'BendersMasterProblem', 0, 0 );

               gmpS := GMP::Benders::CreateSubProblem( myGMP, masterGMP, 'BendersSubProblem',
                                                       0, 0 );

               NumberOfOptimalityCuts := 1;

               ! First iteration of Benders' decomposition algorithm (simplified).
               GMP::Instance::Solve( gmpM );

               GMP::Benders::UpdateSubProblem( gmpS, gmpM, 1, round : 1 );

               GMP::Instance::Solve( gmpS );

               ProgramStatus := GMP::Solution::GetProgramStatus( gmpS, 1 ) ;
               if ( ProgramStatus = 'Optimal' ) then
                   GMP::Benders::AddOptimalityCut( gmpM, gmpS, 1, NumberOfOptimalityCuts );
                   NumberOfOptimalityCuts += 1;
               endif;

.. seealso::

    The routines :aimms:func:`GMP::Benders::CreateMasterProblem`, :aimms:func:`GMP::Benders::CreateSubProblem`, :aimms:func:`GMP::Benders::AddFeasibilityCut`, :aimms:func:`GMP::SolverSession::AddBendersFeasibilityCut` and :aimms:func:`GMP::SolverSession::AddBendersOptimalityCut`.
