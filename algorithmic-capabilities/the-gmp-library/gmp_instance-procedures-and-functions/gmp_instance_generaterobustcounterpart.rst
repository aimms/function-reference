.. aimms:function:: GMP::Instance::GenerateRobustCounterpart(MP, UncertainParameters, UncertaintyConstraints, Name)

.. _GMP::Instance::GenerateRobustCounterpart:

GMP::Instance::GenerateRobustCounterpart
========================================

| The function :aimms:func:`GMP::Instance::GenerateRobustCounterpart` generates
  the robust counterpart of a (linear) mathematical program.
| If the deterministic model is a linear program (LP) then the robust
  counterpart will be a LP if the uncertainty constraints are linear, or
  a second-order cone program (SOCP) if some of the uncertainty
  constraints are ellipsoidal.
| If the deterministic model is a mixed-integer program (MIP) then the
  robust counterpart will be a MIP if the uncertainty constraints are
  linear, or a mixed-integer second-order cone program (MISOCP) if some
  of the uncertainty constraints are ellipsoidal.
| SOCP and MISOCP problems can be solved by using CPLEX or GUROBI.

.. code-block:: aimms

    GMP::Instance::GenerateRobustCounterpart(
         MP,                      ! (input) a symbolic mathematical program
         UncertainParameters,     ! (input) a set of uncertain parameters
         UncertaintyConstraints,  ! (input) a set of uncertainty constraints
         [Name]                   ! (optional) a string expression
    )

Arguments
---------

    *MP*
        A symbolic mathematical program in the set :aimms:set:`AllMathematicalPrograms`. The mathematical
        program should have model type LP or MIP.

    *UncertainParameters*
        A subset of :aimms:set:`AllUncertainParameters`.

    *UncertaintyConstraints*
        A subset of :aimms:set:`AllUncertaintyConstraints`.

    *Name*
        A string that holds the name for the generated robust counterpart.

Return Value
------------

    A new element in the set :aimms:set:`AllGeneratedMathematicalPrograms` with the name as specified by the
    *name* argument.

.. note::

    -  If the *Name* argument is not specified, or if it is the empty
       string, then the name of the symbolic mathematical program followed
       by 'robust counterpart' is used to create a new element in the set
       :aimms:set:`AllGeneratedMathematicalPrograms`.

    -  If AIMMS detects that the robust counterpart is infeasible during the
       generation, AIMMS will issue a warning and the robust counterpart
       will not be generated.

    -  As part of the generation, AIMMS will check whether the uncertainty
       set satisfies the Slater condition (controlled by the option
       ``Slater_condition_check``). To do so, AIMMS will solve a linear
       program (LP) or a second-order cone program (SOCP).

    -  The created GMP cannot be modified, e.g., it is not allowed to change
       row or columns in the robust counterpart.

.. seealso::

    The procedure :aimms:func:`GMP::Instance::Solve`.
