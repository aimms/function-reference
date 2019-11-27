Outer Approximation Functions
=============================

The AIMMS Outer Approximation functions allow you to solve MINLP
problems through a sequence of MIP and NLP solves. The following Outer
Approximation functions are available.

Master MIP Functions
''''''''''''''''''''

AIMMS supports the following Outer Approximation functions for solving
and managing the master MIP problem:

-  :aimms:func:`MasterMIPAddLinearizations`

-  :aimms:func:`MasterMIPDeleteIntegerEliminationCut`

-  :aimms:func:`MasterMIPDeleteLinearizations`

-  :aimms:func:`MasterMIPEliminateIntegerSolution`

-  :aimms:func:`MasterMIPGetCPUTime`

-  :aimms:func:`MasterMIPGetIterationCount`

-  :aimms:func:`MasterMIPGetNumberOfColumns`

-  :aimms:func:`MasterMIPGetNumberOfNonZeros`

-  :aimms:func:`MasterMIPGetNumberOfRows`

-  :aimms:func:`MasterMIPGetObjectiveValue`

-  :aimms:func:`MasterMIPGetProgramStatus`

-  :aimms:func:`MasterMIPGetSolverStatus`

-  :aimms:func:`MasterMIPGetSumOfPenalties`

-  :aimms:func:`MasterMIPIsFeasible`

-  :aimms:func:`MasterMIPLinearizationCommand`

-  :aimms:func:`MasterMIPSetCallback`

-  :aimms:func:`MasterMIPSolve`

MINLP Functions
'''''''''''''''

AIMMS supports the following Outer Approximation functions for managing
the global MINLP problem:

-  :aimms:func:`MINLPGetIncumbentObjectiveValue`

-  :aimms:func:`MINLPGetOptimizationDirection`

-  :aimms:func:`MINLPIncumbentIsFeasible`

-  :aimms:func:`MINLPIncumbentSolutionHasBeenFound`

-  :aimms:func:`MINLPSetIncumbentSolution`

-  :aimms:func:`MINLPSetIterationCount`

-  :aimms:func:`MINLPSetProgramStatus`

-  :aimms:func:`MINLPSolutionDelete`

-  :aimms:func:`MINLPSolutionRetrieve`

-  :aimms:func:`MINLPSolutionSave`

NLP Functions
'''''''''''''

AIMMS supports the following Outer Approximation functions for managing
and solving the NLP problem:

-  :aimms:func:`NLPGetCPUTime`

-  :aimms:func:`NLPGetIterationCount`

-  :aimms:func:`NLPGetNumberOfColumns`

-  :aimms:func:`NLPGetNumberOfNonZeros`

-  :aimms:func:`NLPGetNumberOfRows`

-  :aimms:func:`NLPGetObjectiveValue`

-  :aimms:func:`NLPGetProgramStatus`

-  :aimms:func:`NLPGetSolverStatus`

-  :aimms:func:`NLPIsFeasible`

-  :aimms:func:`NLPLinearizationPointHasBeenFound`

-  :aimms:func:`NLPSolutionIsInteger`

-  :aimms:func:`NLPSolve`

.. toctree::
   :hidden:

   mastermipaddlinearizations
   mastermipdeleteintegereliminationcut
   mastermipdeletelinearizations
   mastermipeliminateintegersolution
   mastermipgetcputime
   mastermipgetiterationcount
   mastermipgetnumberofcolumns
   mastermipgetnumberofnonzeros
   mastermipgetnumberofrows
   mastermipgetobjectivevalue
   mastermipgetprogramstatus
   mastermipgetsolverstatus
   mastermipgetsumofpenalties
   mastermipisfeasible
   mastermiplinearizationcommand
   mastermipsetcallback
   mastermipsolve
   minlpgetincumbentobjectivevalue
   minlpgetoptimizationdirection
   minlpincumbentisfeasible
   minlpincumbentsolutionhasbeenfound
   minlpsetincumbentsolution
   minlpsetiterationcount
   minlpsetprogramstatus
   minlpsolutiondelete
   minlpsolutionretrieve
   minlpsolutionsave
   nlpgetcputime
   nlpgetiterationcount
   nlpgetnumberofcolumns
   nlpgetnumberofnonzeros
   nlpgetnumberofrows
   nlpgetobjectivevalue
   nlpgetprogramstatus
   nlpgetsolverstatus
   nlpisfeasible
   nlplinearizationpointhasbeenfound
   nlpsolutionisinteger
   nlpsolve
