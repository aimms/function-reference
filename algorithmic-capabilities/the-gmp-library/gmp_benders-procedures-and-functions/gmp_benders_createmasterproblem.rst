.. aimms:function:: GMP::Benders::CreateMasterProblem(GMP, Variables, Variables, name, feasibilityOnly, addConstraints)

.. _GMP::Benders::CreateMasterProblem:

GMP::Benders::CreateMasterProblem
=================================

The function :aimms:func:`GMP::Benders::CreateMasterProblem` creates a Benders'
master problem for a generated mathematical program. This master problem
is typically used in a Benders' decomposition algorithm.

.. code-block:: aimms

    GMP::Benders::CreateMasterProblem(
         GMP,                ! (input) a generated mathematical program
         Variables,          ! (input) a set of variables
         name,               ! (input) a string expression
         [feasibilityOnly],  ! (optional, default 0) a scalar value
         [addConstraints]    ! (optional, default 0) a scalar value
    )

Arguments
---------

    *GMP*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

    *Variables*
        A subset of :aimms:set:`AllVariables`.

    *name*
        A string that holds the name for the Benders' master problem.

    *feasibilityOnly*
        A scalar binary value to indicate whether this function should
        (temporary) reformulate the original problem such that the Benders'
        subproblem becomes a pure feasibility problem.

    *addConstraints*
        A scalar binary value to indicate whether this function should try to
        automatically add tightening constraints to the Benders' master problem.

Return Value
------------

    A new element in the set :aimms:set:`AllGeneratedMathematicalPrograms` with the name as specified by the
    *name* argument.

.. note::

    -  A call to :aimms:func:`GMP::Benders::CreateMasterProblem` is typically followed
       by a call to the function :aimms:func:`GMP::Benders::CreateSubProblem`.

    -  The *GMP* must have type LP, MIP or RMIP.

    -  This function cannot be used if the *GMP* is created by the function
       :aimms:func:`GMP::Instance::GenerateStochasticProgram`.

    -  The *Variables* argument specifies the variables that become part of
       the Benders' master problem. All other variables will become part of
       the Benders' subproblem. The objective variable should be part of the
       set of master problem variables; if the objective variable is not
       included in the set *Variables* then this procedure will
       automatically add it.

    -  If the *GMP* contains integer variables then they all must be
       included in the set *Variables*.

    -  The *feasibilityOnly* argument is discussed in more detail in :ref:`sec:benders.feas.prob` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.

    -  The *addConstraints* argument is discussed in more detail in :ref:`sec:benders.feas.prob` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.

Example
-------

    If the math program has type MIP then often the set of master problem
    variables equals the set :aimms:set:`AllIntegerVariables`. 

    .. code-block:: aimms

               myGMP := GMP::Instance::Generated( MP );

               gmpM := GMP::Benders::CreateMasterProblem( myGMP, AllIntegerVariables,
                                                          'BendersMasterProblem', 0, 0 );

.. seealso::

    The routines :aimms:func:`GMP::Benders::CreateSubProblem`, :aimms:func:`GMP::Benders::AddFeasibilityCut` and :aimms:func:`GMP::Benders::AddOptimalityCut`.
