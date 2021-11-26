.. aimms:procedure:: GMP::Instance::FindApproximatelyFeasibleSolution(GMP, solution1, solution2, nrIter, maxIter, feasTol, moveTol, imprTol, maxTime, useSum, augIter, useBest)

.. _GMP::Instance::FindApproximatelyFeasibleSolution:

GMP::Instance::FindApproximatelyFeasibleSolution
================================================

| The procedure :aimms:func:`GMP::Instance::FindApproximatelyFeasibleSolution`
  tries to find an approximately feasible solution of a generated
  mathematical program. It uses the column level values of the first
  solution as a starting point. The approximately feasible solution is
  stored in the second solution.
|
| The algorithm used to find the approximately feasible solution is
  based on the constraint consensus method as developed by John W.
  Chinneck. The constraint consensus method is an iterative projection
  algorithm. In each iteration a new point (i.e., a vector of column
  values) is constructed in such a way that it is likely that it is
  closer to the feasible region (as defined by the generated
  mathematical program) then the previous point.

.. code-block:: aimms

    GMP::Instance::FindApproximatelyFeasibleSolution(
         GMP,            ! (input) a generated mathematical program
         solution1,      ! (input) a solution
         solution2,      ! (input) a solution
         nrIter,         ! (output) a scalar numerical parameter
         [maxIter],      ! (optional) a scalar value
         [feasTol],      ! (optional) a scalar value
         [moveTol],      ! (optional) a scalar value
         [imprTol],      ! (optional) a scalar value,
         [maxTime],      ! (optional) a scalar value
         [useSum],       ! (optional) a scalar value
         [augIter],      ! (optional) a scalar value
         [useBest]       ! (optional) a scalar value
    )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *solution1*
        An integer scalar reference to a solution.

    *solution2*
        An integer scalar reference to a solution.

    *nrIter*
        The number of iterations used by the algorithm.

    *maxIter*
        The maximal number of iterations that can be used by the algorithm. If
        its value is 0 (the default) then there is no iteration limit.

    *feasTol*
        The feasibility distance tolerance. The default is 1e-5.

    *moveTol*
        The movement tolerance. The default is 1e-5.

    *imprTol*
        The improvement tolerance. The default is 0.01.

    *maxTime*
        The maximum time (in seconds) that can be used by the algorithm. If its
        value is 0 (the default) then there is no time limit.

    *useSum*
        A scalar binary value to indicate whether the SUM constraint consensus
        method should be used (value 1) or not (value 0; the default).

    *augIter*
        An integer scalar reference that specifies the frequency of iterations
        in which augumentation should be applied. At the default value of 0 no
        augumentation is applied.

    *useBest*
        A scalar binary value to indicate whether the best point found (value 1)
        or the last point found should be returnd (value 0; the default).

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  The (basic) constraint consensus method is described in: John W.
       Chinneck, The Constraint Consensus Method for Finding Approximately
       Feasible Points in Nonlinear Programs, INFORMS Journal on Computing
       16(3) (2004), pp. 255-265.

    -  The SUM constraint consensus method and a constraint consensus method
       using augumentation are described in: Laurence Smith, John Chinneck,
       Victor Aitken, Improved constraint consensus methods for seeking
       feasibility in nonlinear programs, Computational Optimization and
       Applications 54(3) (2013), pp. 555-578.

    -  The algorithm terminates if:

       -  The iteration limit *maxIter* is exceeded.

       -  The time limit *maxTime* is exceeded.

       -  The feasibility distance of each row is smaller than the
          feasibility distance tolerance *feasTol*. The feasibility distance
          of a row at a point is defined as the row violation normalized by
          the length of the gradient of the row at that point.

       -  The length of the movement vector is smaller than the movement
          tolerance *moveTol*. The movement vector is the vector along which
          the point moves from one iteration to another.

       -  The relative improvement was smaller than the improvement
          tolerance *imprTol* for 10 successive iterations. The improvement
          is defined as the difference between the length of the movement
          vector of the current iteration and that of the previous
          iteration.

    -  The procedure :aimms:func:`GMP::Solution::Check` can be used to get the sum and
       number of infeasibilies before and after calling the procedure
       :aimms:func:`GMP::Instance::FindApproximatelyFeasibleSolution`.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::Solve` and :aimms:func:`GMP::Solution::Check`.
