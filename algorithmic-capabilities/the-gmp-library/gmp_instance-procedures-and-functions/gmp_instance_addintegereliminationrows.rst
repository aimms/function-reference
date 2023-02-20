.. aimms:procedure:: GMP::Instance::AddIntegerEliminationRows(GMP, solution, elimNo)

.. _GMP::Instance::AddIntegerEliminationRows:

GMP::Instance::AddIntegerEliminationRows
========================================

The procedure :aimms:func:`GMP::Instance::AddIntegerEliminationRows` adds integer
elimination rows to the generated mathematical program which will
eliminate an integer solution.

.. code-block:: aimms

    GMP::Instance::AddIntegerEliminationRows(
         GMP,          ! (input) a generated mathematical program
         solution,     ! (input) a solution
         elimNo        ! (input) an elimination number
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *solution*
        An integer scalar reference to a solution.

    *elimNo*
        An integer scalar reference to an elimination number.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  If the GMP is not integer then this procedure will fail.

    -  Rows and columns added before for *elimNo* will be deleted first.

    -  If the GMP contains only binary variables then only one row will be
       added; if the GMP contains general integer variables then several
       rows and columns will be added.

    -  The exact definitions of the rows and columns that are added are as
       follows. Let :math:`x_i` be an integer column whose level value
       :math:`lev_i` is between its lower bound :math:`lb_i` and upper bound
       :math:`ub_i`, i.e., :math:`lb_i < lev_i < ub_i`. Then columns
       :math:`l_i \geq 0` and :math:`u_i \geq 0` are added together with a
       binary column :math:`z_i`. Also the following three constraints are
       added:

       .. math:: l_i + (lev_i - lb_i)z_i \leq (lev_i - lb_i) 
          :label: eq:aier1

       \ 

       .. math:: u_i + (lev_i - ub_i) z_i \leq 0 
          :label: eq:aier2

       .. math:: x_i - u_i + l_i = lev_i 
          :label: eq:aier3

       Every call to :aimms:func:`GMP::Instance::AddIntegerEliminationRows` also adds
       the following constraint:

       .. math::
          :label: eq:aier4

          \begin{aligned}
           \sum_{i\in S_{lo}} x_i - \sum_{i\in S_{up}} x_i + \sum_{i\in S_{in}} (l_i + u_i) \geq 1 + \sum_{i\in S_{lo}} lev_i - \sum_{i\in S_{up}} lev_i  \end{aligned}

       where :math:`S_{lo}` defines the set of integer columns whose level
       values equal their lower bounds, :math:`S_{up}` the set of integer
       columns whose level values equal their upper bounds, and
       :math:`S_{in}` the set of integer columns whose level values are
       between their bounds.

    -  By using the suffixes ``.ExtendedConstraint`` and
       ``.ExtendedVariable`` it is possible to refer to the rows and columns
       respectively that are added by
       :aimms:func:`GMP::Instance::AddIntegerEliminationRows`:

       -  Variables
          ``v.ExtendedVariable('EliminationLowerBound``\ *k*\ ``',i)``,
          ``v.ExtendedVariable('EliminationUpperBound``\ *k*\ ``',i)`` and
          ``v.ExtendedVariable('Elimination``\ *k*\ ``',i)`` are added for
          each integer variable ``v(i)`` with the level value between its
          bounds. (These variables correspond to :math:`l_i`, :math:`u_i`
          and :math:`z_i` respectively.)

       -  Constraints
          ``v.ExtendedConstraint('EliminationLowerBound``\ *k*\ ``',i)``,
          ``v.ExtendedConstraint('EliminationUpperBound``\ *k*\ ``',i)`` and
          ``v.ExtendedConstraint('Elimination``\ *k*\ ``',i)`` are added for
          each integer variable ``v(i)`` with the level value between its
          bounds. (These constraints correspond to :eq:`eq:aier1`, :eq:`eq:aier2` and
          :eq:`eq:aier3` respectively.)

       -  Constraint ``mp.ExtendedConstraint('Elimination``\ *k*\ ``')``,
          where ``mp`` denotes the symbolic mathematical program, is added
          for every call to :aimms:func:`GMP::Instance::AddIntegerEliminationRows`.
          (This constraint corresponds to :eq:`eq:aier4`.)

       Here :math:`k` denotes the value of the argument *elimNo*.

Example
-------

    The procedure :aimms:func:`GMP::Instance::AddIntegerEliminationRows` can be used
    to find the five best integer solutions for some MIP model: 

    .. code-block:: aimms

               gmp_mip := GMP::Instance::Generate(MIP_Model);

               cnt := 1;

               while ( cnt <= 5 ) do
                   GMP::Instance::Solve(gmp_mip);

                   ! Eliminate previous found integer solution.
                   GMP::Instance::AddIntegerEliminationRows(gmp_mip,1,cnt);

                   cnt += 1;

                   ! Copy solution at position 1 to solution at position cnt
                   ! in solution repository.
                   GMP::Solution::Copy(gmp_mip,1,cnt);
               endwhile;
    
    After executing this code, the five best integer solutions will be
    stored at positions 2 - 6 in the solution repository, with the best
    solution at position 2 and the 5th best at position 6.

.. seealso::

    The routines :aimms:func:`GMP::Instance::DeleteIntegerEliminationRows` and :aimms:func:`GMP::Solution::IsInteger`. See :ref:`sec:matrix.extended` of the Language
    Reference for more details on extended suffixes.
