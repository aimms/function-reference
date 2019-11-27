.. aimms:procedure:: GMP::Linearization::Add(GMP1, GMP2, solution, constraintSet, deviationsPermitted, penaltyMultipliers, linNo, jacTol)

.. _GMP::Linearization::Add:

GMP::Linearization::Add
=======================

The procedure :aimms:func:`GMP::Linearization::Add` adds a linearization row to a
generated mathematical program (*GMP1*) with respect to a solution
(column level values and row marginals) of a second generated
mathematical program (*GMP2*) for each row in a set of nonlinear
constraints of that second generated mathematical program.

.. code-block:: aimms

    GMP::Linearization::Add(
         GMP1,                  ! (input) a generated mathematical program
         GMP2,                  ! (input) a generated mathematical program
         solution,              ! (input) a solution
         constraintSet,         ! (input) a set of nonlinear constraints
         deviationsPermitted,   ! (input) a binary parameter
         penaltyMultipliers,    ! (input) a double parameter
         linNo,                 ! (input) a linearization number
         [jacTol]               ! (optional) the Jacobian tolerance
         )

Arguments
---------

    *GMP1*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *GMP2*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *solution*
        An integer scalar reference to a solution in the solution repository of
        *GMP2*.

    *constraintSet*
        A subset of :aimms:set:`AllNonLinearConstraints`.

    *deviationsPermitted*
        A binary parameter over :aimms:set:`AllNonLinearConstraints` indicating whether deviations are
        permitted for these linearizations. If yes, a new column will also be
        added to *GMP1* with an objective coefficient equal to the double value
        given in *penaltyMultiplier* multiplied with the row marginal of the row
        in *solution*.

    *penaltyMultipliers*
        A double parameter over :aimms:set:`AllNonLinearConstraints` representing the penalty multiplier
        that will be used if *deviationsPermitted* indicates that a deviation is
        permitted for the linearization.

    *linNo*
        An integer scalar reference to the rows and columns of the
        linearization.

    *jacTol*
        The Jacobian tolerance; if the Jacobian value (in absolute sense) of a
        column in a nonlinear row is smaller than this value, the column will
        not be added to the linearization of that row. The default is 1e-5.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  This procedure fails if one of the constraints is ranged.

    -  Rows and columns added before for *linNo* will be deleted first.

    -  This procedure will fail if *GMP2* contains a column that is not part
       of *GMP1*. A column that is part of *GMP1* but not of *GMP2* will be
       ignored, i.e., no coefficient for that column will be added to the
       linearizations.

    -  The formula for the linearization of a scalar nonlinear inequality
       :math:`g(x,y) \leq b_j` around the point :math:`(x,y) = (x^0,y^0)` is
       as follows.

       .. math:: g(x^0,y^0) + \bigtriangledown g(x^0,y^0)^T \begin{bmatrix} x - x^0 \\ y - y^0 \end{bmatrix} - z_j \leq b_j

       \ where :math:`z_j \geq 0` is the extra column that is added if a
       deviation is permitted.

    -  For a scalar nonlinear equality :math:`g(x,y) = b_j` the sense of the
       linearization depends on the shadow price of the equality in the
       *solution*. The sense will be '\ :math:`\leq`\ ' if the shadow price
       is negative and the optimization direction is minimization, or if the
       shadow price is positive and the optimization direction is
       maximization. The sense will be '\ :math:`\geq`\ ' if the shadow
       price is positive and the optimization direction is minimization, or
       if the shadow price is negative and the optimization direction is
       maximization.

    -  By using the suffixes ``.ExtendedConstraint`` and
       ``.ExtendedVariable`` it is possible to refer to the rows and columns
       that are added by :aimms:func:`GMP::Linearization::Add`:

       -  Constraint ``c.ExtendedConstraint('Linearization``\ *k*\ ``',j)``
          is added for each nonlinear constraint ``c(j)``.

       -  Variable ``c.ExtendedVariable('Linearization``\ *k*\ ``',j)`` is
          added for each nonlinear constraint ``c(j)`` if a deviation is
          permitted for constraint ``c(j)``.

       Here :math:`k` denotes the value of the argument *linNo*.

.. seealso::

    The routines :aimms:func:`GMP::Linearization::AddSingle` and :aimms:func:`GMP::Linearization::Delete`. See Section 16.3.6 of the Language
    Reference for more details on extended suffixes.
