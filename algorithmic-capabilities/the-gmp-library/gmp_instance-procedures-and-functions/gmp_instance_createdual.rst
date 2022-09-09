.. aimms:function:: GMP::Instance::CreateDual(GMP, name)

.. _GMP::Instance::CreateDual:

GMP::Instance::CreateDual
=========================

The function :aimms:func:`GMP::Instance::CreateDual` generates a mathematical
program that is the dual representation of the specified generated
mathematical program. The generated mathematical program should have
model type LP.

.. code-block:: aimms

    GMP::Instance::CreateDual(
         GMP,            ! (input) a generated mathematical program
         name            ! (input) a string expression
    )

Arguments
---------

    *GMP*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

    *name*
        A string that holds the name for the dual of the generated mathematical
        program.

Return Value
------------

    A new element in the set :aimms:set:`AllGeneratedMathematicalPrograms` with the name as specified by the
    *name* argument.

.. note::

    -  The *name* argument should be different from the name of the original
       generated mathematical program.

    -  If an element with name specified by the *name* argument is already
       present in the set :aimms:set:`AllGeneratedMathematicalPrograms` the corresponding generated mathematical
       program will be replaced (or updated in case the same symbolic
       mathematical program is involved).

    -  The solution of a dual variable can be accessed through the ``.ShadowPrice``
       suffix of the corresponding (primal) constraint.

    -  Before a generated mathematical program is dualized, AIMMS first
       transforms it temporary into a standard form using the following
       rules:

       -  Each column :math:`x_i` that is frozen to 0 is deleted.

       -  For each column :math:`x_i` with upper bound :math:`u_i`,
          :math:`u_i \neq 0` and :math:`u_i < \infty`, an extra row
          :math:`x_i \leq u_i` is added.

       -  For each column :math:`x_i` with lower bound :math:`l_i`,
          :math:`l_i \neq 0` and :math:`l_i > -\infty`, an extra row
          :math:`x_i \geq l_i` is added.

       -  Each ranged row :math:`l_j \leq a^T x \leq u_j`
          (:math:`l_j > -\infty` and :math:`u_j < \infty`) is replaced by
          two rows :math:`l_j \leq a^T x` and :math:`a^T x \leq u_j`.

    -  By using the suffix ``.ExtendedConstraint`` it is possible to refer
       to the rows that are added to create the standard form:

       -  The constraint ``v.ExtendedConstraint('DualUpperBound',i)`` is
          added for a variable ``v(i)`` with an upper bound unequal to 0 and
          inf.

       -  The constraint ``v.ExtendedConstraint('DualLowerBound',i)`` is
          added for a variable ``v(i)`` with a lower bound unequal to 0 and
          -inf.

       -  The constraints ``c.ExtendedConstraint('DualLowerBound',j)`` and
          ``c.ExtendedConstraint('DualUpperBound',j)`` replace a ranged
          constraint ``c(j)``.

       The solution of these constraints can be accessed through the ``.ShadowPrice``
       suffix, e.g., ``v.ExtendedConstraint('DualUpperBound',i).ShadowPrice``.

    -  The objective variable for the dual mathematical program will become
       ``mp.ExtendedConstraint(DualObjective)`` and the objective constraint
       will be ``mp.ExtendedVariable(DualDefinition)``, where ``mp`` denotes
       the symbolic mathematical program.

Example
-------

    Assume that 'PrimalModel' is a mathematical program with the following
    declaration (in ams format): 

    .. code-block:: aimms

               Variable x1 {
                   Range: [0, 5];
               }
               Variable x2 {
                   Range: nonnegative;
               }
               Variable obj {
                   Definition: - 7 * x1 - 2 * x2;
               }
               Constraint c1 {
                   Definition: - x1 + 2 * x2 <= 4;
               }
               MathematicalProgram PrimalModel {
                   Objective: obj;
                   Direction: minimize;
                   Type: LP;
               }

    Then
    :aimms:func:`GMP::Instance::CreateDual` will create a dual mathematical program
    with variables 

    .. code-block:: aimms

               name                                             lower  upper
               c1                                                -inf      0
               obj_definition                                    -inf    inf
               x1.ExtendedConstraint('DualUpperBound')           -inf      0
               PrimalModel.ExtendedConstraint('DualObjective')   -inf    inf

    and constraints 

    .. code-block:: aimms

               x1:
                  - c1 + 7 * obj_definition + x1.ExtendedConstraint('DualUpperBound') >= 0 ;

               x2:
                  + 2 * c1 + 2 * obj_definition >= 0 ;

               obj:
                  obj_definition = 1 ;

               PrimalModel.ExtendedVariable('DualDefinition'):
                  - 4 * c1 - 5 * x1.ExtendedConstraint('DualUpperBound')
                  + PrimalModel.ExtendedConstraint('DualObjective') = 0 ;

.. seealso::

    The function :aimms:func:`GMP::Instance::Generate`. See :ref:`sec:matrix.extended` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__ for
    more details on extended suffixes.
