.. aimms:procedure:: GMP::Instance::SetCallbackAddCut(GMP, callback)

.. _GMP::Instance::SetCallbackAddCut:

GMP::Instance::SetCallbackAddCut
================================

The procedure :aimms:func:`GMP::Instance::SetCallbackAddCut` installs a callback
procedure adding cuts during the solution process of a MIP model.

.. code-block:: aimms

    GMP::Instance::SetCallbackAddCut(
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

    -  The procedure ``GMP::SolverSession::GenerateCut`` can be used inside
       a ``CallbackAddCut`` callback procedure to add cuts during the MIP
       branch & cut process.

    -  The callback procedure should have exactly one argument; a scalar
       input element parameter into the set :aimms:set:`AllSolverSessions`.

    -  The ``CallbackAddCut`` callback procedure should have a return value
       of

       -  0, if you want the solution process to stop, or

       -  1, if you want the solution process to continue.

    -  To remove the callback the empty element should be used as the
       *callback* argument.

    -  A ``CallbackAddCut`` callback procedure will only be called when
       solving mixed integer programs with CPLEX, Gurobi or ODH-CPLEX.

    -  This procedure can also be used for MIQP and MIQCP problems.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::SetCallbackAddLazyConstraint`, :aimms:func:`GMP::Instance::SetCallbackBranch`, :aimms:func:`GMP::Instance::SetCallbackCandidate`, :aimms:func:`GMP::Instance::SetCallbackHeuristic`,
    :aimms:func:`GMP::Instance::SetCallbackIncumbent`, :aimms:func:`GMP::SolverSession::GenerateBinaryEliminationRow` and :aimms:func:`GMP::SolverSession::GenerateCut`.
