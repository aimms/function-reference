.. aimms:function:: GMP::Instance::CreateFeasibility(GMP, name, useMinMax)

.. _GMP::Instance::CreateFeasibility:

GMP::Instance::CreateFeasibility
================================

| The function :aimms:func:`GMP::Instance::CreateFeasibility` creates a
  mathematical program that is the feasibility problem of a generated
  mathematical program. Its main purpose is to identify infeasibilities
  in an infeasible problem. The feasibility problem can be used to
  minimize the sum of infeasibilities, or to minimize the maximum
  infeasibility.
| This function can be used for both linear and nonlinear problems but
  not for constraint programming problems.

.. code-block:: aimms

    GMP::Instance::CreateFeasibility(
         GMP,            ! (input) a generated mathematical program
         [name],         ! (input, optional) a string expression
         [useMinMax]     ! (input, optional) integer, default 0
         )

Arguments
---------

    *GMP*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

    *name*
        A string that contains the name for the feasibility problem.

    *useMinMax*
        If 0, the sum of infeasibilities will be minimized, else the maximum
        infeasibility will be minimized.

Mathematical formulation
~~~~~~~~~~~~~~~~~~~~~~~~

| In this section we show how the feasibility problem is constructed. To
  simplify the explanation we use a linear problem but the same
  construction applies to a nonlinear problem.
| Consider the following problem where :math:`J` denotes the set of
  variables, :math:`I_1` the set of :math:`\geq` inequalities,
  :math:`I_2` the set of :math:`\leq` inequalities, and :math:`I_3` the
  set of equalities.

  .. math::

     \begin{aligned}
      \max \quad & \sum_{j\in J} a_{j} x_j \\ \text{s.t.} \quad & \sum_{j\in J} a_{ij} x_j && \geq b_i \quad i \in I_1 \\ & \sum_{j\in J} a_{ij} x_j && \leq b_i \quad i \in I_2 \\ & \sum_{j\in J} a_{ij} x_j && = b_i \quad i \in I_3 \\ & x \geq 0 \end{aligned}

  \ Then if we minimize the sum of infeasibilities the feasibility
  problem becomes:

  .. math::

     \begin{aligned}
      \min \quad & \sum_{i \in I_1} z^p_i + \sum_{i \in I_2} z^n_i + \\ & \sum_{i \in I_3} (z^p_i + z^n_i) \\ \text{s.t.} \quad & \sum_{j\in J} a_{ij} x_j + z^p_i && \geq b_i \quad && i \in I_1 \\ & \sum_{j\in J} a_{ij} x_j - z^n_i && \leq b_i \quad && i \in I_2 \\ & \sum_{j\in J} a_{ij} x_j + z^p_i - z^n_i && = b_i \quad && i \in I_3 \\ & x, z^p, z^n \geq 0 \end{aligned}

  If we minimize the maximum infeasibility the feasibility problem
  becomes:

  .. math::

     \begin{aligned}
      \min \quad & z^m \\ \text{s.t.} \quad & \sum_{j\in J} a_{ij} x_j + z^m && \geq b_i \quad && i \in I_1 \\ & \sum_{j\in J} a_{ij} x_j - z^m && \leq b_i \quad && i \in I_2 \\ & \sum_{j\in J} a_{ij} x_j + z^p_i - z^n_i && = b_i \quad && i \in I_3 \\ & z^m - z^p_i - z^n_i && \geq 0 \quad && i \in I_3 \\ & x, z^p, z^n \geq 0 \end{aligned}

Return Value
------------

    A new element in the set :aimms:set:`AllGeneratedMathematicalPrograms` with the name as specified by the
    *name* argument.

.. note::

    -  The *name* argument should be different from the name of the original
       generated mathematical program.

    -  If the *name* argument is not specified then AIMMS will name the
       generated math program as "Feasibility problem of" followed by the
       name of the *GMP*.

    -  If an element with name specified by the *name* argument is already
       present in the set :aimms:set:`AllGeneratedMathematicalPrograms` the corresponding generated mathematical
       program will be replaced (or updated in case the same symbolic
       mathematical program is involved).

    -  By using the suffices ``.ExtendedVariable`` and
       ``.ExtendedConstraint`` it is possible to refer to the columns and
       rows that are added to create the feasibility problem. In case the
       sum of infeasibilities is minimized only variables are added:

       -  The variable ``c.ExtendedVariable('PositiveViolation',i)`` is
          added for a constraint ``c(i)`` with type :math:`\geq`.

       -  The variable ``c.ExtendedVariable('NegativeViolation',i)`` is
          added for a constraint ``c(i)`` with type :math:`\leq`.

       -  The variables ``c.ExtendedVariable('PositiveViolation',i)`` and
          ``c.ExtendedVariable('NegativeViolation',i)`` are added for an
          equality constraint ``c(i)``.

       In case the maximum infeasibility is minimized the following
       variables and constraints are added:

       -  The variable ``mp.ExtendedVariable('MaximumViolation')`` is added
          for math program ``mp``.

       -  The variables ``c.ExtendedVariable('PositiveViolation',i)`` and
          ``c.ExtendedVariable('NegativeViolation',i)`` are added for an
          equality constraint ``c(i)``.

       -  The constraint ``c.ExtendedConstraint('MaximumViolation',i)`` is
          added for an equality constraint ``c(i)``.

       In the above mathematical formulation,

       -  ``c.ExtendedVariable('PositiveViolation',i)`` corresponds to
          :math:`z^p_i`.

       -  ``c.ExtendedVariable('NegativeViolation',i)`` corresponds to
          :math:`z^n_i`.

       -  ``mp.ExtendedVariable('MaximumViolation')`` corresponds to
          :math:`z^m`.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate` and :aimms:func:`GMP::Instance::Solve`.
