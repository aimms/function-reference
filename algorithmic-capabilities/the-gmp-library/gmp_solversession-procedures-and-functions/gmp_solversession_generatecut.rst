.. aimms:procedure:: GMP::SolverSession::GenerateCut(solverSession, row, local, purgeable)

.. _GMP::SolverSession::GenerateCut:

GMP::SolverSession::GenerateCut
===============================

The procedure :aimms:func:`GMP::SolverSession::GenerateCut` adds a cut to the LP
subproblem of the current node during MIP branch-and-cut. It can also be
used to add a lazy constraint inside a callback for adding lazy
constraints.

.. code-block:: aimms

    GMP::SolverSession::GenerateCut(
         solverSession,    ! (input) a solver session
         row,              ! (input) a scalar reference
         [local],          ! (optional, default 0) a scalar binary expression
         [purgeable]       ! (optional, default 0) a scalar binary expression
         )

Arguments
---------

    *solverSession*
        An element in the set :aimms:set:`AllSolverSessions`.

    *row*
        A scalar reference to a row in the model.

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

    -  This procedure can only be called from within a ``CallbackAddCut`` or
       ``CallbackAddlazyConstraint`` callback procedure.

    -  A ``CallbackAddCut`` callback procedure will only be called when
       solving mixed integer programs with CPLEX, Gurobi or ODH-CPLEX. In
       case of Gurobi the cuts are always local even if argument *local* has
       value 0.

    -  A ``CallbackAddLazyConstraint`` callback procedure will only be
       called when solving mixed integer programs with CPLEX or Gurobi.

    -  Argument *purgeable* can only be used with CPLEX. If the cut is local
       then the cut will not be purgeable even if argument *purgeable* has
       value 1.

    -  This procedure can also be used for MIQP and MIQCP problems.

Example
-------

    We have a math program, with variables ``x(v1)`` and ``y(v1,v2)``,for which we
    want add certain cuts, namely triangle cut
    and triangle clique constraints, during the solve. For that we use a callback
    procedure that is called whenever the MIP solver finds a new fractional solution
    (typically after solving a subproblem in the branch-and-bound algorithm).
    The cut callback procedure can be implemented as follows.

    .. code-block:: aimms
    
               ! Get fractional solution from solver and pass it to the AIMMS identifiers.
               
               myGMP := GMP::SolverSession::GetInstance( solvSess );
               
               GMP::Solution::RetrieveFromSolverSession( solvSess, 1 );
               GMP::Solution::SendToModel( myGMP, 1 );
               
               ! Find violated triangle cut and triangle clique constraints and pass them
               ! as cuts to the MIP solver.
               
               for ( (v1,v2,v3) | v1 < v2 and v2 < v3 ) do
                   ! Triangle Cut.
               
                   if ( x(v1) + x(v2) + x(v3) - y(v1,v2) - y(v1,v3) - y(v2,v3) > 1 ) then
                       GMP::SolverSession::GenerateCut( solvSess, Triangle_Cut(v1,v2,v3) );
                   endif;
               
                   ! Triangle Clique.
               
                   if ( y(v1,v2) + y(v1,v3) - x(v1) - y(v2,v3) > 0 ) then
                       GMP::SolverSession::GenerateCut( solvSess, Triangle_Clique(v1,v2,v3) );
                   endif;
               endfor;
               
               return 1;

    Here 'solvSess' is an input argument of the callback procedure and a
    scalar element parameter into the set :aimms:set:`AllSolverSessions`.
    And 'myGMP' is a scalar element parameter into the set
    :aimms:set:`AllGeneratedMathematicalPrograms`,
    defined as a local parameter of the callback procedure.

.. seealso::

    The procedures :aimms:func:`GMP::Instance::SetCallbackAddCut` and :aimms:func:`GMP::Instance::SetCallbackAddLazyConstraint`. See :doc:`optimization-modeling-components/implementing-advanced-algorithms-for-mathematical-programs/managing-generated-mathematical-program-instances` of the Language
    Reference for more details on how to install a callback procedure to add
    cuts.
