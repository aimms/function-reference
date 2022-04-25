Mathematical Program Suffices
=============================

AIMMS mathematical programs support the following four collections of
suffices. The first group of suffices steers the solution process. These
suffices are specified in the model before the solve statement and are
used during the solution process.

-  :ref:`.bratio`

-  :ref:`.cutoff`

-  :ref:`.domlim`

-  :ref:`.iterlim`

-  :ref:`.limrow`

-  :ref:`.nodlim`

-  :ref:`.optca`

-  :ref:`.optcr`

-  :ref:`.reslim`

-  :ref:`.tolinfrep`

-  :ref:`.workspace`

The second group of suffixes contain information obtained during and at
the end of the solution process. these suffixes can be accessed after
the solve statement.

-  :ref:`.SolverStatus`

-  :ref:`.ProgramStatus`

-  :ref:`.SolverCalls`

-  :ref:`.objective`

-  :ref:`.incumbent`

-  :ref:`.BestBound`

-  :ref:`.GenTime`

-  :ref:`.SolutionTime`

-  :ref:`.Iterations`

-  :ref:`.NumberOfBranches`

-  :ref:`.NumberOfConstraints`

-  :ref:`.NumberOfFails`

-  :ref:`.NumberOfNonzeros`

-  :ref:`.NumberOfVariables`

-  :ref:`.NumberOfInfeasibilities`

-  :ref:`.SumOfInfeasibilities`

The third group of suffixes control which AIMMS procedure should be
called during the solution process and whether this calling should take
place.

-  :ref:`.CallbackProcedure`

-  :ref:`.CallbackIterations`

-  :ref:`.CallbackTime`

-  :ref:`.CallbackStatusChange`

-  :ref:`.CallbackIncumbent`

-  :ref:`.CallbackReturnStatus`

-  :ref:`.CallbackAddCut`

The fourth group of suffixes are obsolete ones. They are only retained
in order not to invalidate converted AIMMS 2 and ``GAMS`` models.

-  ``.solveopt``

-  ``.prioropt``

-  ``.scaleopt``

-  ``.optfile``

-  ``.solprint``

-  ``.sysout``

-  ``.numnlins``

-  ``.numnlnz``

-  ``.domusd``

-  ``.nodusd``

-  ``.integer1``

-  ``.integer2``

-  ``.integer3``

-  ``.integer4``

-  ``.integer5``

-  ``.real1``

-  ``.real2``

-  ``.real3``

-  ``.real4``

-  ``.real5``

-  ``.line``

-  ``.limcol``

.. toctree::
   :hidden:

   bratio
   cutoff
   domlim
   iterlim
   limrow
   nodlim
   optca
   optcr
   reslim
   tolinfrep
   workspace
   programstatus
   solvercalls
   solverstatus
   incumbent
   objective
   bestbound
   nodes
   gentime
   iterations
   solutiontime
   numberofbranches
   numberofconstraints
   numberoffails
   numberofinfeasibilities
   numberofnonzeros
   numberofvariables
   callbackiterations
   callbackprocedure
   sumofinfeasibilities
   callbackstatuschange
   callbacktime
   callbackincumbent
   callbackreturnstatus
   callbackaddcut
