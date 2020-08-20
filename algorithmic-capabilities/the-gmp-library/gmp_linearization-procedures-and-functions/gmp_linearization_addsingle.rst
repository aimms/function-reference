.. aimms:procedure:: GMP::Linearization::AddSingle(GMP1, GMP2, solution, row, deviationPermitted, penaltyMultiplier, linNo, jacTol)

.. _GMP::Linearization::AddSingle:

GMP::Linearization::AddSingle
=============================

The procedure :aimms:func:`GMP::Linearization::AddSingle` adds a single
linearization row to a generated mathematical program (*GMP1*) with
respect to a solution (column level values and row marginals) of a
second generated mathematical program (*GMP2*).

.. code-block:: aimms

    GMP::Linearization::AddSingle(
         GMP1,                  ! (input) a generated mathematical program
         GMP2,                  ! (input) a generated mathematical program
         solution,              ! (input) a solution
         row,                   ! (input) a scalar reference or row number
         deviationPermitted,    ! (input) a binary scalar
         penaltyMultiplier,     ! (input) a double scalar
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

    *row*
        A scalar reference to an existing nonlinear row in the matrix of *GMP2* or the number of
        that row in the range :math:`\{ 0 .. m-1 \}` where :math:`m` is the
        number of rows in the matrix of *GMP2*.

    *deviationPermitted*
        A binary scalar indicating whether a deviation is permitted for this
        linearization. If yes, a new column will also be added to *GMP1* with an
        objective coefficient equal to the double value given in
        *penaltyMultiplier* multiplied with the row marginal of the row in
        *solution*.

    *penaltyMultiplier*
        A double value representing the penalty multiplier that will be used if
        *deviationPermitted* indicates that a deviation is permitted for the
        linearization.

    *linNo*
        An integer scalar reference to the rows and columns of the
        linearization.

    *jacTol*
        The Jacobian tolerance; if the Jacobian value (in absolute sense) of a
        column in *row* is smaller than this value, the column will not be added
        to the linearization. The default is 1e-5.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  This procedure fails if the row is ranged.

    -  Rows and columns added before for *linNo* will be deleted first.

    -  This procedure will fail if *GMP2* contains a column that is not part
       of *GMP1*. A column that is part of *GMP1* but not of *GMP2* will be
       ignored, i.e., no coefficient for that column will be added to the
       linearizations.

    -  The formula for the linearization of a scalar nonlinear inequality
       :math:`g(x,y) \leq b_j` around the point :math:`(x,y) = (x^0,y^0)` is
       as follows:

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
       ``.ExtendedVariable`` it is possible to refer to the row and column
       that are added by :aimms:func:`GMP::Linearization::AddSingle`:

       -  Constraint ``c.ExtendedConstraint('Linearization``\ *k*\ ``',j)``
          is added for row ``c(j)``.

       -  Variable ``c.ExtendedVariable('Linearization``\ *k*\ ``',j)`` is
          added for row ``c(j)`` if a deviation is permitted.

       Here :math:`k` denotes the value of the argument *linNo*.

Example
-------

    Assume that 'prod03' is a mathematical program with the following
    declaration (in aim format): 

    .. code-block:: aimms

               Variable i1 {
                   Range      :  {
                       {1..5}
                   }
               }
               Variable i2 {
                   Range      :  {
                       {1..5}
                   }
               }
               Variable objvar;
               Constraint e1 {
                   Definition :  - 3*i1 - 2*i2 + objvar = 0;
               }
               Constraint e2 {
                   Definition :  - i1*i2 <= -3.5;
               }
               MathematicalProgram prod03 {
                   Objective  :  objvar;
                   Direction  :  minimize;
                   Type       :  MINLP;
               }

    Assume that AIMMS has executed
    the following code in which a mathematical program instance 'gmp1' is
    generated from 'prod03', its integer variables are relaxed, and it is
    solved. 

    .. code-block:: aimms

               gmp1 := GMP::Instance::Generate(prod03);
               GMP::Instance::SetMathematicalProgrammingType(gmp1,'RMINLP');
               GMP::Instance::Solve(gmp1);

    The optimal solution is :math:`\verb|i1| = 1.528`
    and :math:`\verb|i2| = 2.291`, with Jacobian values :math:`-2.291` and
    :math:`-1.528` for :math:`\verb|i1|` and :math:`\verb|i2|` respectively.
    This solution is stored at position 1 in the solution repository of
    'gmp1'. If we have a second generated mathematical program 'gmp2' with
    the same variables as 'gmp1' then 

    .. code-block:: aimms

               GMP::Linearization::AddSingle(gmp2,gmp1,1,e2,0,0,1);

    will add a row 

    .. code-block:: aimms

               e2.ExtendedConstraint('Linearization1'):
                  - 2.291 * i1 - 1.528 * i2 <= -7 ;

        to 'gmp2'.

.. seealso::

    The routines :aimms:func:`GMP::Linearization::Add` and :aimms:func:`GMP::Linearization::Delete`. See Section 16.3.6 of the Language
    Reference for more details on extended suffixes.
