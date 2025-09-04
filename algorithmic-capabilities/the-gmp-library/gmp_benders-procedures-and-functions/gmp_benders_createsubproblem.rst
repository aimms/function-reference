.. aimms:function:: GMP::Benders::CreateSubProblem(GMP1, GMP2, name, useDual, normalizationType)

.. _GMP::Benders::CreateSubProblem:

GMP::Benders::CreateSubProblem
==============================

The function :aimms:func:`GMP::Benders::CreateSubProblem` creates a Benders'
subproblem for a generated mathematical program. This subproblem is
typically used in a Benders' decomposition algorithm.

.. code-block:: aimms

    GMP::Benders::CreateSubProblem(
         GMP1,               ! (input) a generated mathematical program
         GMP2,               ! (input) a generated mathematical program
         name,               ! (input) a string expression
         [useDual],          ! (optional, default 0) a scalar value
         [normalizationType] ! (optional, default 0) a scalar value
    )

Arguments
---------

    *GMP1*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

    *GMP2*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms` representing a Benders' master problem.

    *name*
        A string that holds the name for the Benders' subproblem.

    *useDual*
        A scalar binary value to indicate whether this function should create
        the primal (value 0) or dual (value 1) of the subproblem.

    *normalizationType*
        A scalar value to indicate which kind of normalization this function
        should use. Value 0 implies that the standard normalization is used.
        Value 1 implies that the normalization condition introduced by
        Fischetti, Salvagnin and Zanette (2010) is used. The normalization
        condition is added as a constraint to the subproblem.

Return Value
------------

    A new element in the set :aimms:set:`AllGeneratedMathematicalPrograms` with the name as specified by the
    *name* argument.

    .. note::

        -   The *GMP1* must have type LP, MIP or RMIP.

        -   The *GMP2* should have been created using the function
            :aimms:func:`GMP::Benders::CreateMasterProblem`. Note that the call to that
            function specifies how the variables (and constraints) are divided
            among the master and subproblem.

        -   The *useDual* argument is discussed in more detail in :ref:`sec:benders.primaldual.sub`
            of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.

        -   The *normalizationType* argument is discussed in more detail in
            :ref:`sec:benders.primaldual.sub` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.

Example
-------

If the math program has type MIP then often the set of master problem
variables equals the set :aimms:set:`AllIntegerVariables`. All other variables automatically
become part of the subproblem. 

.. code-block:: aimms

    myGMP := GMP::Instance::Generated( MP );

    gmpM := GMP::Benders::CreateMasterProblem( myGMP, AllIntegerVariables,
                                                'BendersMasterProblem', 0, 0 );

    gmpS := GMP::Benders::CreateSubProblem( myGMP, masterGMP, 'BendersSubProblem',
                                            0, 0 );

.. seealso::

    - :aimms:func:`GMP::Benders::CreateMasterProblem`.
    - :aimms:func:`GMP::Benders::AddFeasibilityCut`.
    - :aimms:func:`GMP::Benders::AddOptimalityCut`.
    - :aimms:func:`GMP::Benders::UpdateSubProblem`.
    - :aimms:func:`GMP::Instance::CreateFeasibility`.
