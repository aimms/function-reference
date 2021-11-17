.. aimms:procedure:: GMP::Instance::SetCallbackCandidate(GMP, callback)

.. _GMP::Instance::SetCallbackCandidate:

GMP::Instance::SetCallbackCandidate
===================================

The procedure :aimms:func:`GMP::Instance::SetCallbackCandidate` installs a
callback procedure that is called every time an incumbent solution is
found during the solution process of a MIP model. By using the procedure
:aimms:func:`GMP::SolverSession::RejectIncumbent` the incumbent solution can be
rejected. If :aimms:func:`GMP::SolverSession::RejectIncumbent` is not called
inside the ``CallbackCandidate`` callback procedure then the incumbent
solution will be accepted and replace the best incumbent solution found
by so far.

.. code-block:: aimms

    GMP::Instance::SetCallbackCandidate(
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

    -  The callback procedure should have exactly one argument; a scalar
       input element parameter into the set :aimms:set:`AllSolverSessions`.

    -  The ``CallbackCandidate`` callback procedure should have a return
       value of

       -  0, if you want the solution process to stop, or

       -  1, if you want the solution process to continue.

       If the return value is 0 (i.e., interrupt the solution process) then
       the incumbent solution will not be accepted!

    -  To remove the callback the empty element should be used as the
       *callback* argument.

    -  If an **incumbent** callback procedure is installed by using the
       procedure :aimms:func:`GMP::Instance::SetCallbackIncumbent`, then that callback
       will be called after the **candidate** callback procedure if the
       incumbent solution is not rejected inside the **candidate** callback.

    -  A ``CallbackCandidate`` callback procedure will only be called when
       solving mixed integer programs with CPLEX.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::SetCallbackAddCut`, :aimms:func:`GMP::Instance::SetCallbackAddLazyConstraint`, :aimms:func:`GMP::Instance::SetCallbackBranch`, :aimms:func:`GMP::Instance::SetCallbackHeuristic`,
    :aimms:func:`GMP::Instance::SetCallbackIncumbent` and :aimms:func:`GMP::SolverSession::RejectIncumbent`.
