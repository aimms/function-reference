.. aimms:procedure:: GMP::SolverSession::GetIIS(solverSession, rowSet, colSet)

.. _GMP::SolverSession::GetIIS:

GMP::SolverSession::GetIIS
==========================

The procedure :aimms:func:`GMP::SolverSession::GetIIS` returns an
irreducible infeasible set (IIS) for an infeasible math program, by
returning the numbers of the rows and columns that are part of the IIS.

.. code-block:: aimms

    GMP::SolverSession::GetIIS(
         solverSession,    ! (input) a solver session
         rowSet,           ! (output) a subset of Integers
         colSet            ! (output) a subset of Integers
         )

Arguments
---------

    *solverSession*
        An element in the set :aimms:set:`AllSolverSessions`.

    *rowSet*
        A subset of the set :aimms:set:`Integers`, representing a set of row
        numbers.

    *colSet*
        A subset of the set :aimms:set:`Integers`, representing a set of column
        numbers.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  This procedure is only supported by BARON, CPLEX and Gurobi. In case of BARON,
       the BARON option ``Compute IIS`` should be set to a non-default value.
    
    -  Calculating the IIS procedure can be time consuming, especially if the model
       contains binary or integer variables.

Example
-------

    To use
    :aimms:func:`GMP::SolverSession::GetIIS` we declare the following identifiers
    (in ams format):
    
    .. code-block:: aimms

               ElementParameter myGMP {
                   Range: AllGeneratedMathematicalPrograms;
               }
               ElementParameter session {
                   Range: AllSolverSessions;
               }
               ElementParameter ProgramStatus {
                   Range: AllSolutionStates;
               }
               Set RowSet {
                   SubsetOf: Integers;
                   Index: rr;
               }
               Set ColSet {
                   SubsetOf: Integers;
                   Index: cc;
               }
               StringParameter name;

    To retrieve the IIS, and print the rows and columns that are part of the IIS, we can use:

    .. code-block:: aimms

               myGMP := GMP::Instance::Generate( MP );
               session := GMP::Instance::CreateSolverSession( myGMP );
               
               GMP::SolverSession::Execute( session );
               
               ProgramStatus := GMP::SolverSession::GetProgramStatus( session );
               
               if ( ProgramStatus = 'Infeasible' or ProgramStatus = 'InfeasibleOrUnbounded' ) then
                   GMP::SolverSession::GetIIS( session, RowSet, ColSet );
               
                   for ( rr ) do
                       name := GMP::Row::GetName( myGMP, rr );
                       display name;
                   endfor;
               
                   for ( cc ) do
                       name := GMP::Column::GetName( myGMP, cc );
                       display name;
                   endfor;
               else
                   GMP::Solution::RetrieveFromSolverSession( session, 1 );
                   GMP::Solution::SendToModel( myGMP, 1 );
               endif;
               
               GMP::Instance::Delete( myGMP );

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::CreateSolverSession`, :aimms:func:`GMP::SolverSession::Execute`,
    :aimms:func:`GMP::SolverSession::GetProgramStatus`, :aimms:func:`GMP::Column::GetName` and :aimms:func:`GMP::Row::GetName`.
