.. aimms:procedure:: GMP::Solution::Check(GMP, solution, numInfeas, sumInfeas, maxInfeas, skipObj)

.. _GMP::Solution::Check:

GMP::Solution::Check
====================

The procedure :aimms:func:`GMP::Solution::Check` checks the validity of a solution
for a generated mathematical program.

.. code-block:: aimms

    GMP::Solution::Check(
         GMP,            ! (input) a generated mathematical program
         solution,       ! (input) a solution
         numInfeas,      ! (output) number of infeasibilities
         sumInfeas,      ! (output) sum of infeasibilities
         maxInfeas,      ! (output) maximum infeasibility
         [skipObj],      ! (optional, default 0) a scalar value
		 [feasTol]       ! (optional, default -1) a scalar value
         )

Arguments
---------

    *GMP*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

    *solution*
        An integer scalar reference to a solution.

    *numInfeas*
        Number of infeasibilities for the solution.

    *sumInfeas*
        Sum of all infeasibilities for the solution.

    *maxInfeas*
        Maximum infeasibility for the solution.

    *skipObj*
        A scalar binary value to indicate whether constraints containing the
        objective variable should be skipped (value 1) or not (value 0).

	*feasTol*
		Feasibility tolerance in checking the constraints violations. If this
		argument is negative, the value of the option ``Constraint Listing
		Feasibility Tolerance`` is used.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    The optional argument feasTol determines the feasibility tolerance used by
	this procedure. If a constraint violation is smaller than this tolerance
	then it will be ignored. If this argument is not passed, or if it is set
	to a negative value, the option ``Constraint Listing Feasibility Tolerance``
	is used as the feasibility tolerance.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Solution::RetrieveFromModel` and :aimms:func:`GMP::Solution::RetrieveFromSolverSession`.
