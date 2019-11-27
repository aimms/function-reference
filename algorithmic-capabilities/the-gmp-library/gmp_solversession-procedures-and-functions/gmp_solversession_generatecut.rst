.. aimms:procedure:: GMP::SolverSession::GenerateCut(solverSession, row, local, purgeable)

.. _GMP::SolverSession::GenerateCut:

GMP::SolverSession::GenerateCut
===============================

The procedure :aimms:func:`GMP::SolverSession::GenerateCut` adds a cut to the LP
subproblem of the current node during MIP branch & cut. It can also be
used to add a lazy constraint inside a callback for adding lazy
constraints.

.. code-block:: aimms

    GMP::SolverSession::GenerateCut(
         solverSession,    ! (input) a solver session
         row,              ! (input) a scalar reference
         [local],          ! (optional, default 0) a scalar binary expression
         [purgeable]       ! (optional, default 0) a scalar binary expression
         )

Arguments
---------

    *solverSession*
        An element in the set :aimms:set:`AllSolverSessions`.

    *row*
        A scalar reference to an existing row in the model.

    *local*
        A scalar binary value to indicate whether the cut is valid for the local
        problem (i.e. the problem corresponding to the current node in the
        solution process and all its descendant nodes) only (value 1) or for the
        global problem (value 0).

    *purgeable*
        A scalar binary value to indicate whether the solver is allowed to purge
        the cut if it deems it ineffective. If the value is 1, then it is
        allowed.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  This procedure can only be called from within a ``CallbackAddCut`` or
       ``CallbackAddlazyConstraint`` callback procedure.

    -  A ``CallbackAddCut`` callback procedure will only be called when
       solving mixed integer programs with CPLEX, GUROBI or ODH-CPLEX. In
       case of GUROBI the cuts are always local even if argument *local* has
       value 0.

    -  A ``CallbackAddLazyConstraint`` callback procedure will only be
       called when solving mixed integer programs with CPLEX or GUROBI.

    -  Argument *purgeable* can only be used with CPLEX. If the cut is local
       then the cut will not be purgeable even if argument *purgeable* has
       value 1.

    -  This procedure can also be used for MIQP and MIQCP problems.

.. seealso::

    The procedures :aimms:func:`GMP::Instance::SetCallbackAddCut` and :aimms:func:`GMP::Instance::SetCallbackAddLazyConstraint`. See Section 16.2 of the Language
    Reference for more details on how to install a callback procedure to add
    cuts.
