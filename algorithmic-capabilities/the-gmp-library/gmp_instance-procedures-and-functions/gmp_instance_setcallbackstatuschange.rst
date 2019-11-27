.. aimms:procedure:: GMP::Instance::SetCallbackStatusChange(GMP, callback)

.. _GMP::Instance::SetCallbackStatusChange:

GMP::Instance::SetCallbackStatusChange
======================================

The procedure :aimms:func:`GMP::Instance::SetCallbackStatusChange` installs a
callback procedure that is called every time the status changes during
the solution process.

.. code-block:: aimms

    GMP::Instance::SetCallbackStatusChange(
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

    -  The ``CallbackStatusChange`` callback procedure should have a return
       value of

       -  0, if you want the solution process to stop, or

       -  1, if you want the solution process to continue.

    -  To remove the callback the empty element should be used as the
       *callback* argument.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::SetCallbackAddCut`, :aimms:func:`GMP::Instance::SetCallbackAddLazyConstraint`, :aimms:func:`GMP::Instance::SetCallbackBranch`, :aimms:func:`GMP::Instance::SetCallbackCandidate`,
    :aimms:func:`GMP::Instance::SetCallbackHeuristic`, :aimms:func:`GMP::Instance::SetCallbackIncumbent`, :aimms:func:`GMP::Instance::SetCallbackIterations` and :aimms:func:`GMP::Instance::SetCallbackTime`.
