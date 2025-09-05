.. aimms:procedure:: GMP::Instance::SetCallbackIncumbent(GMP, callback)

.. _GMP::Instance::SetCallbackIncumbent:

GMP::Instance::SetCallbackIncumbent
===================================

The procedure :aimms:func:`GMP::Instance::SetCallbackIncumbent` installs a
callback procedure that is called every time a new incumbent solution is
found during the solution process of a MIP model.

.. code-block:: aimms

    GMP::Instance::SetCallbackIncumbent(
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

    -  The ``CallbackIncumbent`` callback procedure should have a return
       value of

       -  0, if you want the solution process to stop, or

       -  1, if you want the solution process to continue.

    -  To remove the callback the empty element should be used as the
       *callback* argument.

    -  This procedure is not supported by COPT.

    -  The functionality of the procedure
       :aimms:func:`GMP::Instance::SetCallbackIncumbent` has been changed between
       AIMMS versions 4.68 and 4.69. In AIMMS version 4.68 and older this
       procedure was named ``GMP::Instance::SetCallbackNewIncumbent``. That
       procedure has become deprecated. AIMMS version 4.68 and older already
       contained a procedure that was named
       ``GMP::Instance::SetCallbackIncumbent`` but that procedure has been
       renamed to :aimms:func:`GMP::Instance::SetCallbackCandidate`.

.. seealso::

    - The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::SetCallbackAddCut`, :aimms:func:`GMP::Instance::SetCallbackAddLazyConstraint`, :aimms:func:`GMP::Instance::SetCallbackBranch`, :aimms:func:`GMP::Instance::SetCallbackCandidate`, :aimms:func:`GMP::Instance::SetCallbackHeuristic`, :aimms:func:`GMP::Instance::SetCallbackIterations`, :aimms:func:`GMP::Instance::SetCallbackStatusChange` and :aimms:func:`GMP::Instance::SetCallbackTime`.
