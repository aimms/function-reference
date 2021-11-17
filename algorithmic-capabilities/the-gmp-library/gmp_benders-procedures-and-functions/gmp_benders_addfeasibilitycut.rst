.. aimms:procedure:: GMP::Benders::AddFeasibilityCut(GMP1, GMP2, solution, cutNo, tighten)

.. _GMP::Benders::AddFeasibilityCut:

GMP::Benders::AddFeasibilityCut
===============================

The procedure :aimms:func:`GMP::Benders::AddFeasibilityCut` generates a
feasibility cut for a Benders' master problem using the solution of a
Benders' subproblem (or the corresponding feasibility problem). This
procedure is typically used in a Benders' decomposition algorithm.

.. code-block:: aimms

    GMP::Benders::AddFeasibilityCut(
         GMP1,             ! (input) a generated mathematical program
         GMP2,             ! (input) a generated mathematical program
         solution,         ! (input) a solution
         cutNo,            ! (input) a scalar reference
         [tighten]         ! (optional, default 0) a scalar binary expression
    )

Arguments
---------

    *GMP1*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms` representing a Benders' master problem.

    *GMP2*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms` representing a Benders' subproblem (or
        the corresponding feasibility problem).

    *solution*
        An integer scalar reference to a solution of *GMP2*.

    *cutNo*
        An integer scalar reference to a cut number.

    *tighten*
        A scalar binary value to indicate whether the feasibility cut should be
        tightened. If the value is 1, tightening is attempted.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  The *GMP1* should have been created using the function
       :aimms:func:`GMP::Benders::CreateMasterProblem`.

    -  The *GMP2* should have been created using the function
       :aimms:func:`GMP::Benders::CreateSubProblem` or the function
       :aimms:func:`GMP::Instance::CreateFeasibility`.

    -  If the GMP that was created by :aimms:func:`GMP::Benders::CreateSubProblem`
       represents the dual of the Benders' subproblem then this GMP should
       be used as argument *GMP2*. If it represents the primal of the
       Benders' subproblem then first the feasibility problem should be
       created which then should be used as argument *GMP2*.

    -  The *solution* of the Benders' subproblem or feasibility problem
       (represented by *GMP2*) is used to generate an optimality cut for the
       Benders' master problem (represented by *GMP1*).

    -  A feasibility cut :math:`a^T x \geq b` can be tightened to
       :math:`1^T x \geq 1` if :math:`x` is a vector of binary variables and
       :math:`a_i \geq b > 0` for all :math:`i`.

Example
-------

    In the examples below we assume that the Benders' subproblem is
    infeasible. The way :aimms:func:`GMP::Benders::AddFeasibilityCut` is called
    depends on whether the primal or dual of the Benders' subproblem was
    generated. In the first example we use the dual. In that case an
    unbounded extreme ray is used to create a feasibility cut. See :ref:`sec:benders.textbook.alg` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__. 

    .. code-block:: aimms

               ! Initialization.
               myGMP := GMP::Instance::Generated( MP );

               gmpM := GMP::Benders::CreateMasterProblem( myGMP, AllIntegerVariables,
                                                          'BendersMasterProblem', 0, 0 );

               gmpS := GMP::Benders::CreateSubProblem( myGMP, masterGMP, 'BendersSubProblem',
                                                       useDual : 1, normalizationType : 0 );

               NumberOfFeasibilityCuts := 1;

               ! Switch on solver option for calculating unbounded extreme ray. 
               GMP::Instance::SetOptionValue( gmpS, 'unbounded ray', 1 );

               ! First iteration of Benders' decomposition algorithm (simplified).
               GMP::Instance::Solve( gmpM );

               GMP::Benders::UpdateSubProblem( gmpS, gmpM, 1, round : 1 );

               GMP::Instance::Solve( gmpS );

               ProgramStatus := GMP::Solution::GetProgramStatus( gmpS, 1 ) ;
               if ( ProgramStatus = 'Unbounded' ) then
                   GMP::Benders::AddFeasibilityCut( gmpM, gmpS, 1, NumberOfFeasibilityCuts );
                   NumberOfFeasibilityCuts += 1;
               endif;

    In the second example we use
    the primal of the Benders' subproblem. If that problem turns out to be
    infeasible then we solve a feasibility problem to get a solution of
    minimum infeasibility (according to some measurement). The shadow prices
    of the constraints and the reduced costs of the variables in that
    solution are used to create a feasibility cut. See :ref:`sec:benders.textbook.alg` of the
    Language Reference. 

    .. code-block:: aimms

               ! Initialization.
               myGMP := GMP::Instance::Generated( MP );

               gmpM := GMP::Benders::CreateMasterProblem( myGMP, AllIntegerVariables,
                                                          'BendersMasterProblem', 0, 0 );

               gmpS := GMP::Benders::CreateSubProblem( myGMP, masterGMP, 'BendersSubProblem',
                                                       useDual : 0, normalizationType : 0 );

               NumberOfFeasibilityCuts := 1;

               ! First iteration of Benders' decomposition algorithm (simplified).
               GMP::Instance::Solve( gmpM );

               GMP::Benders::UpdateSubProblem( gmpS, gmpM, 1, round : 1 );

               GMP::Instance::Solve( gmpS );

               ProgramStatus := GMP::Solution::GetProgramStatus( gmpS, 1 ) ;
               if ( ProgramStatus = 'Infeasible' ) then
                   gmpF := GMP::Instance::CreateFeasibility( gmpS, "FeasProb", useMinMax : 1 );

                   GMP::Instance::Solve( gmpF );

                   GMP::Benders::AddFeasibilityCut( gmpM, gmpF, 1, NumberOfFeasibilityCuts );
                   NumberOfFeasibilityCuts += 1;
               endif;

.. seealso::

    The routines :aimms:func:`GMP::Benders::CreateMasterProblem`, :aimms:func:`GMP::Benders::CreateSubProblem`, :aimms:func:`GMP::Benders::AddOptimalityCut`, :aimms:func:`GMP::Instance::CreateFeasibility`, :aimms:func:`GMP::SolverSession::AddBendersFeasibilityCut` and
    :aimms:func:`GMP::SolverSession::AddBendersOptimalityCut`.
