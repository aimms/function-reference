.. aimms:procedure:: GMP::Instance::SetCallbackAddLazyConstraint(GMP, callback)

.. _GMP::Instance::SetCallbackAddLazyConstraint:

GMP::Instance::SetCallbackAddLazyConstraint
===========================================

The procedure :aimms:func:`GMP::Instance::SetCallbackAddLazyConstraint` installs a
callback procedure for adding lazy constraints during the solution
process of a MIP model.

.. code-block:: aimms

    GMP::Instance::SetCallbackAddLazyConstraint(
         GMP,            ! (input) a generated mathematical program
         callback        ! (input) an AIMMS procedure
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *callback*
        A reference to a procedure in the set :aimms:set:`AllIdentifiers`.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  The callback procedure is called by the solver in these situations

       -  when the solver compares an integer-feasible solution (including
          an integer-feasible solution provided by a MIP start before any
          nodes exist) to lazy constraints;

       -  when the LP at a node is unbounded, and a lazy constraint might
          cut off the primal ray.

    -  The procedure ``GMP::SolverSession::GenerateCut`` can be used inside
       a ``CallbackAddLazyConstraint`` callback procedure to add (globally
       or locally valid) lazy constraints during the MIP branch & cut
       process. Lazy constraints added to the problem are first put into a
       pool of lazy constraints, so they are not present in the subproblem
       LP until after the callback is finished.

    -  If lazy constraints have been added, the subproblem is re-solved and
       evaluated, and, if the LP solution is still integer feasible and not
       cut off, the lazy constraint callback is called again.

    -  The callback procedure should have exactly one argument; a scalar
       input element parameter into the set :aimms:set:`AllSolverSessions`.

    -  The ``CallbackAddLazyConstraint`` callback procedure should have a
       return value of

       -  0, if you want the solution process to stop, or

       -  1, if you want the solution process to continue.

    -  To remove the callback the empty element should be used as the
       *callback* argument.

    -  A ``CallbackAddLazyConstraint`` callback procedure will only be
       called when solving mixed integer programs with CPLEX or GUROBI.

    -  This procedure can also be used for MIQP and MIQCP problems.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::SetCallbackAddCut`, :aimms:func:`GMP::Instance::SetCallbackBranch`, :aimms:func:`GMP::Instance::SetCallbackCandidate`, :aimms:func:`GMP::Instance::SetCallbackHeuristic`,
    :aimms:func:`GMP::Instance::SetCallbackIncumbent` and :aimms:func:`GMP::SolverSession::GenerateCut`.
