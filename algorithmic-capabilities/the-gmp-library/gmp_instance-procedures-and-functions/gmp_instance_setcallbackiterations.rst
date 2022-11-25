.. aimms:procedure:: GMP::Instance::SetCallbackIterations(GMP, callback, value)

.. _GMP::Instance::SetCallbackIterations:

GMP::Instance::SetCallbackIterations
====================================

The procedure :aimms:func:`GMP::Instance::SetCallbackIterations` installs a
callback procedure that is called after a specified number of
iterations.

.. code-block:: aimms

    GMP::Instance::SetCallbackIterations(
         GMP,            ! (input) a generated mathematical program
         callback,       ! (input) an AIMMS procedure
         [value]         ! (optional) number of iterations
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *callback*
        A reference to a procedure in the set :aimms:set:`AllIdentifiers`.

    *value*
        A scalar value indicating after which number of iterations the callback
        procedure should be called. The default value is 0.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  The callback procedure should have exactly one argument; a scalar
       input element parameter into the set :aimms:set:`AllSolverSessions`.

    -  The ``CallbackIterations`` callback procedure should have a return
       value of

       -  0, if you want the solution process to stop, or

       -  1, if you want the solution process to continue.

    -  To remove the callback the empty element should be used as the
       *callback* argument.

    -  The number of iterations can also be set by the
       ``CallbackIterations`` suffix of the symbolic mathematical program,
       but will be overruled if the *value* is not equal to 0.

    -  During a MIP solve, the iterations callback will be called
       irregularly by CPLEX, Gurobi and ODH-CPLEX (especially during the MIP
       phase).

    -  The iterations callback will be called less often if CPLEX uses
       dynamic search as the MIP Search Strategy instead of branch-and-cut.

    -  This procedure is not supported by COPT.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::SetCallbackAddCut`, :aimms:func:`GMP::Instance::SetCallbackAddLazyConstraint`, :aimms:func:`GMP::Instance::SetCallbackBranch`, :aimms:func:`GMP::Instance::SetCallbackCandidate`,
    :aimms:func:`GMP::Instance::SetCallbackHeuristic`, :aimms:func:`GMP::Instance::SetCallbackIncumbent`, :aimms:func:`GMP::Instance::SetCallbackStatusChange` and :aimms:func:`GMP::Instance::SetCallbackTime`.
