.. aimms:procedure:: GMP::Instance::SetCallbackTime(GMP, callback)

.. _GMP::Instance::SetCallbackTime:

GMP::Instance::SetCallbackTime
==============================

The procedure :aimms:func:`GMP::Instance::SetCallbackTime` installs a callback
procedure that is called after a specified number of (elapsed) seconds.
By default this callback procedure is called every two seconds.

.. code-block:: aimms

    GMP::Instance::SetCallbackTime(
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

    -  The ``CallbackTime`` callback procedure should have a return value of

       -  0, if you want the solution process to stop, or

       -  1, if you want the solution process to continue.

    -  To remove the callback the empty element should be used as the
       *callback* argument.

    -  The ``CallbackTime`` callback procedure is supported by CPLEX,
       Gurobi, CBC, ODH-CPLEX, XA, CP Optimizer, CONOPT, Knitro, SNOPT and
       IPOPT.

    -  The number of (elapsed) seconds is determined by the general solvers
       option ``Progress Time Interval``. This option also specifies the
       interval for updating the Progress Window during a solve. As a
       consequence, the information passed to this callback procedure will
       be the same as the information displayed in the Progress Window
       (except for small differences for the solving time).

    -  The time callback will be called less often if CPLEX uses dynamic
       search as the MIP Search Strategy instead of branch-and-cut. In that
       case the interval between two successive calls might sometimes be
       larger than the interval as specified by the option
       ``Progress Time Interval``.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::SetCallbackAddCut`, :aimms:func:`GMP::Instance::SetCallbackAddLazyConstraint`, :aimms:func:`GMP::Instance::SetCallbackBranch`, :aimms:func:`GMP::Instance::SetCallbackCandidate`,
    :aimms:func:`GMP::Instance::SetCallbackHeuristic`, :aimms:func:`GMP::Instance::SetCallbackIncumbent` and :aimms:func:`GMP::Instance::SetCallbackStatusChange`.
