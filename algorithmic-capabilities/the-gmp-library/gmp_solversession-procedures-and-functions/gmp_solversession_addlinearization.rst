.. aimms:procedure:: GMP::SolverSession::AddLinearization(solverSession, GMP, solution, constraintSet, jacTol, local, purgeable)

.. _GMP::SolverSession::AddLinearization:

GMP::SolverSession::AddLinearization
====================================

The procedure :aimms:func:`GMP::SolverSession::AddLinearization` adds a
linearization row to a solver session with respect to a solution (column
level values and row marginals) of a generated mathematical program for
each row in a set of nonlinear constraints of that generated
mathematical program.

.. code-block:: aimms

    GMP::SolverSession::AddLinearization(
         solverSession,    ! (input) a solver session
         GMP,              ! (input) a generated mathematical program
         solution,         ! (input) a solution
         constraintSet,    ! (input) a set of nonlinear constraints
         [jacTol],         ! (optional) the Jacobian tolerance
         [local],          ! (optional, default 0) a scalar binary expression
         [purgeable]       ! (optional, default 0) a scalar binary expression
         )

Arguments
---------

    *solverSession*
        An element in the set :aimms:set:`AllSolverSessions`.

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *solution*
        An integer scalar reference to a solution in the solution repository of
        *GMP*.

    *constraintSet*
        A subset of :aimms:set:`AllNonLinearConstraints`.

    *jacTol*
        The Jacobian tolerance; if the Jacobian value (in absolute sense) of a
        column in a nonlinear row is smaller than this value, the column will
        not be added to the linearization of that row. The default is 1e-5.

    *local*
        A scalar binary value to indicate whether the linearization is valid for
        the local problem (i.e. the problem corresponding to the current node in
        the solution process and all its descendant nodes) only (value 1) or for
        the global problem (value 0).

    *purgeable*
        A scalar binary value to indicate whether the solver is allowed to purge
        the cut if it deems it ineffective. If the value is 1, then it is
        allowed.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  This procedure fails if one of the constraints is ranged.

    -  This procedure can only be called from within a ``CallbackAddCut`` or
       ``CallbackAddLazyConstraint`` callback procedure.

    -  A ``CallbackAddCut`` callback procedure will only be called when
       solving mixed integer programs with CPLEX or GUROBI. In case of
       GUROBI the cuts are always local even if argument *local* has value
       0.

    -  A ``CallbackAddLazyConstraint`` callback procedure will only be
       called when solving mixed integer programs with CPLEX or GUROBI.

    -  Argument *purgeable* can only be used with CPLEX. If the cut is local
       then the cut will not be purgeable even if argument *purgeable* has
       value 1.

    -  This procedure will fail if *GMP* contains a column that is not part
       of the generated mathematical program corresponding to
       *solverSession*. A column that is part of *GMP* but not of the
       generated mathematical program corresponding to *solverSession* will
       be ignored, i.e., no coefficient for that column will be added to the
       linearizations.

    -  The formula for the linearization of a scalar nonlinear inequality
       :math:`g(x,y) \leq b_j` around the point :math:`(x,y) = (x^0,y^0)` is
       as follows.

       .. math:: g(x^0,y^0) + \bigtriangledown g(x^0,y^0)^T \begin{bmatrix} x - x^0 \\ y - y^0 \end{bmatrix} \leq b_j

.. seealso::

    The routines :aimms:func:`GMP::Linearization::Add`, :aimms:func:`GMP::Instance::SetCallbackAddCut`, :aimms:func:`GMP::Instance::SetCallbackAddLazyConstraint` and :aimms:func:`GMP::SolverSession::GenerateCut`.
