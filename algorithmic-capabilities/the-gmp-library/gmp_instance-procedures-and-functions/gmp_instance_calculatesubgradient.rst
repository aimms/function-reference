.. aimms:procedure:: GMP::Instance::CalculateSubGradient(GMP, variableSet, constraintSet, session)

.. _GMP::Instance::CalculateSubGradient:

GMP::Instance::CalculateSubGradient
===================================

The procedure :aimms:func:`GMP::Instance::CalculateSubGradient` can be used to
solve *By* = *x* for a given vector *x*, where *B* is the basis matrix
of a linear program. This procedure can only be called after the linear
program has been solved to optimality.

.. code-block:: aimms

    GMP::Instance::CalculateSubGradient(
         GMP,           ! (input) a generated mathematical program
         variableSet,   ! (input) a set of variables
         constraintSet, ! (input) a set of constraints
         [session]      ! (input, optional) a solver session
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`. The mathematical program should have model type
        LP or RMIP.

    *variableSet*
        A subset of :aimms:set:`AllVariables`.

    *constraintSet*
        A subset of :aimms:set:`AllConstraints`.

    *session*
        An element in the set :aimms:set:`AllSolverSessions`.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  Use the ``.ExtendedConstraint('RhsChange',*)`` suffix of the
       constraints in *constraintSet* to assign values to the vector *x*.

    -  The suffix ``.ExtendedVariable('RhsChange',*)`` of the variables in
       *variableSet* will be used to store the subgradient *y*.

    -  The suffixes ``.ExtendedConstraint`` and ``.ExtendedVariable`` have
       no unit and are not scaled.

    -  This procedure should be called after a normal solve statement or
       after a successful call to procedure :aimms:func:`GMP::Instance::Solve`.

    -  This procedure can also be called after a successful call to the
       procedure :aimms:func:`GMP::SolverSession::Execute` or the procedure
       :aimms:func:`GMP::SolverSession::AsynchronousExecute`. In that case the solver
       session should be passed using the *session* argument.

    -  A column corresponding to a variable in *variableSet* that is not
       part of *GMP* will be ignored. A row corresponding to a constraint in
       *constraintSet* that is not part of *GMP* will also be ignored.

    -  This procedure is only supported by CPLEX and Gurobi.

    -  This procedure cannot be used if the *GMP* is created by
       :aimms:func:`GMP::Instance::CreateDual`.

Example
-------

    Assume that 'MP' is a linear mathematical program and ``c(i)`` is a
    constraint and ``v(j)`` is a variable in this mathematical program. The
    following example shows how to calculate a subgradient after a normal
    solve statement. 

    .. code-block:: aimms

               solve MP;

               ! The next statement needs to be called once.
               AllGMPExtensions += { 'RhsChange' };

               c.ExtendedConstraint('RhsChange',i) := 1.0;

               GMP::Instance::CalculateSubGradient('MP',AllVariables,AllConstraints);

               display v.ExtendedVariable('RhsChange',j);

.. seealso::

    The functions :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::Solve`, :aimms:func:`GMP::SolverSession::Execute` and :aimms:func:`GMP::SolverSession::AsynchronousExecute`. See 
    :ref:`sec:matrix.extended` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__ for more details on extended suffixes.
