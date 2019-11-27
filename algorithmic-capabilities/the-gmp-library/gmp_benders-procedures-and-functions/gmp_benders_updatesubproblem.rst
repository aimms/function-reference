.. aimms:procedure:: GMP::Benders::UpdateSubProblem(GMP1, GMP2, solution, round)

.. _GMP::Benders::UpdateSubProblem:

GMP::Benders::UpdateSubProblem
==============================

The procedure :aimms:func:`GMP::Benders::UpdateSubProblem` updates a Benders'
subproblem (or the corresponding feasibility problem) using the solution
of a Benders' master problem. This procedure is typically used in a
Benders' decomposition algorithm.

.. code-block:: aimms

    GMP::Benders::UpdateSubProblem(
         GMP1,             ! (input) a generated mathematical program
         GMP2,             ! (input) a generated mathematical program
         solution,         ! (input) a solution
         [round]           ! (optional, default 0) a scalar value
    )

Arguments
---------

    *GMP1*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms` representing a Benders' subproblem.

    *GMP2*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms` representing a Benders' master problem.

    *solution*
        An integer scalar reference to a solution of *GMP2*.

    *round*
        A binary scalar indicating whether the level values of the integer
        variables (if any) should be rounded to the nearest integer value in the
        solution used to update the subproblem.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  The *GMP1* should have been created using the function
       ``GMP::Benders::CreateSubProblem`` or the function
       ``GMP::Instance::CreateFeasibility``.

    -  The *GMP2* should have been created using the function
       ``GMP::Benders::CreateMasterProblem``.

    -  The *solution* of the Benders' master problem (represented by *GMP2*)
       is used to update the Benders' subproblem (represented by *GMP1*).
       That is, the right-hand-side values of the constraints in the
       subproblem are reevaluated using the level values of the variables in
       the solution of the Benders' master problem.

Example
-------

    Before solving the subproblem it should be updated using a solution of
    the master problem. In the example below we use the solution at position
    1 in the solution repository of the GMP belonging to the master problem.

    .. code-block:: aimms

               myGMP := GMP::Instance::Generated( MP );

               gmpM := GMP::Benders::CreateMasterProblem( myGMP, AllIntegerVariables,
                                                          'BendersMasterProblem', 0, 0 );

               gmpS := GMP::Benders::CreateSubProblem( myGMP, masterGMP, 'BendersSubProblem',
                                                       0, 0 );

               GMP::Instance::Solve( gmpM );

               GMP::Benders::UpdateSubProblem( gmpS, gmpM, 1, round : 1 );

               GMP::Instance::Solve( gmpS );

.. seealso::

    The functions :aimms:func:`GMP::Benders::CreateMasterProblem`, :aimms:func:`GMP::Benders::CreateSubProblem` and :aimms:func:`GMP::Instance::CreateFeasibility`.
