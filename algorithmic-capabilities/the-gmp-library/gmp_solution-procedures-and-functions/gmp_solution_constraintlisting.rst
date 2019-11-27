.. aimms:procedure:: GMP::Solution::ConstraintListing(GMP, solution, Filename, AppendMode)

.. _GMP::Solution::ConstraintListing:

GMP::Solution::ConstraintListing
================================

The procedure :aimms:func:`GMP::Solution::ConstraintListing` outputs a detailed
description of a generated mathematical program to file. It uses the
solution to provide feasibility, left hand side and derivative
information.

.. code-block:: aimms

    GMP::Solution::ConstraintListing(
         GMP,            ! (input) a generated mathematical program
         solution,       ! (input) a solution
         Filename,       ! (input) a string
         [AppendMode]    ! (input/optional) integer, default 0
         )

Arguments
---------

    *GMP*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

    *solution*
        An integer that is a reference to a solution.

    *Filename*
        The name of the file to which the output is written.

    *AppendMode*
        If non-zero, the output will be appended to the file, instead of
        overwritten.

This function allows one to inspect a generated mathematical program
after it is generated, modified, or solved.

Usage example
~~~~~~~~~~~~~

Given the following declarations: 

.. code-block:: aimms

        MathematicalProgram sched;
        ElementParameter cp_gmp {
            Range        :  AllGeneratedMathematicalPrograms;
        }
        Parameter vars_in_cl {
            Range        :  binary;
            InitialData  :  0;
            Comment      : {
                "When 1 the variables and bounds are printed 
               in the constraint listing"
            }
        }

The use of the function
:aimms:func:`GMP::Solution::ConstraintListing` is illustrated in the following
code fragment. 

.. code-block:: aimms

          cp_gmp := gmp::Instance::Generate( sched );
          if cp_gmp then 
              GMP::Solution::RetrieveFromModel( cp_gmp, 1 );
              block where constraint_listing_variable_values := vars_in_cl ;
                  GMP::Solution::ConstraintListing( cp_gmp, 1, "sched.constraintlisting" );
              endblock; 
          endif ;

The following remarks apply to this code
fragment:

-  Directly after generation, the generated mathematical program
   referenced by ``cp_gmp`` does not contain a solution. The current
   values in the model can be used to obtain such a solution using
   :aimms:func:`GMP::Solution::RetrieveFromModel`.

-  The actual call to :aimms:func:`GMP::Solution::ConstraintListing` is placed in
   a block statement, to permit the programmatic control of output
   steering options. The available output steering options are in the
   option category ``Solvers General`` - ``Standard Reports`` - ``Constraints``.

Output
~~~~~~

The description that is output by the function
:aimms:func:`GMP::Solution::ConstraintListing` is split into a header, a body, and
a footer.

The header of a constraint listing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The brief header contains the solve ``number`` (the suffix ``.number``)
of the mathematical program and the name of the generated mathematical
program. Whenever this suffix is less than or equal to twenty, it is
written as a word. When the generated mathematical program is a
scheduling problem, containing activities as documented in Section
22.2.1, the problem schedule domain is also printed, as illustrated in
the following example: 

.. code-block:: aimms

        This is the first constraint listing of mySched.

        The schedule domain of mySched is the calendar "TimeLine" containing 61 elements 
                                                in the range { '2011-03-31' .. '2011-05-30' }.

This is a constraint listing whereby
the scheduling problem ``mySched`` is solved once. In addition, the
problem schedule domain is detailed.

The body of a constraint listing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The body of the constraint listing contains all details in the rows of
the generated mathematical program. The information detailed depends
both on option settings and the type of row. Lets begin with a linear
row.

An LP row
~~~~~~~~~

From AIMMS example Transportation model: 

.. code-block:: aimms

    ----  MeetDemand  The amount transported to customer c should meet its demand

    MeetDemand(Alkmaar) .. [ 1 | 2 | Optimal ]

        + 1 * Transport(Eindhoven ,Alkmaar) + 1 * Transport(Haarlem   ,Alkmaar) 
        + 1 * Transport(Heerenveen,Alkmaar) + 1 * Transport(Middelburg,Alkmaar) 
        + 1 * Transport(Zutphen   ,Alkmaar) >= 793 ; (lhs=793, scale=0.001)

        name                              lower    level    upper    scale
        Transport(Eindhoven,Alkmaar)          0        0      inf    0.001
        Transport(Haarlem,Alkmaar)            0      793      inf    0.001
        Transport(Heerenveen,Alkmaar)         0        0      inf    0.001
        Transport(Middelburg,Alkmaar)         0        0      inf    0.001
        Transport(Zutphen,Alkmaar)            0        0      inf    0.001

For each group of
constraints, the name of that constraint and its text are printed. Next
comes each row of that group, whereby the number of rows per symbolic
constraint can be limited by the option
``Number_of_Rows_per_Constraint_in_Listing``. A row starts with its name
and then, within square brackets, the solve number, the row number, and
the solution status of the solution. For that row, it is followed by its
contents, whereby all terms containing variables are moved to the left
and all terms without variables to the right and summed to mimic the LP
form :math:`Ax \leq b`. Between parentheses the ``lhs`` is computed by
filling in the values of the variables. In this version of the model the
base unit for weight is ``ton``, but the constraint uses the unit ``kg``
which is ``0.001 * ton``. AIMMS computes the LP matrix with respect to
the base units and subsequently scales to the units of the variables and
constraints. Thus we have a scaling factor of ``0.001`` for both the
constraint and the variables. The coefficients presented are the
coefficients after this scaling and as such passed to the solver. The
last part of this example shows the variable values, their bounds, and,
when relevant, the scaling factor. This last part is obtained by setting
the option ``constraint listing variable values`` to ``on``.

An NLP row
~~~~~~~~~~

Consider the arbitrary objective definition 

.. code-block:: aimms

        Variable o {
            Range      :  free;
            Definition :  x^3 - y^4 + x / y;
        }

Filling in the
definition attribute of variable ``o`` will let AIMMS construct the
constraint ``o_definition`` with the same index domain, empty here, and
unit, empty here. This constraint is presented as follows in the
constraint listing. 

.. code-block:: aimms

        ----  o_definition

        o_definition .. [ 0 | 2 | not solved yet ]

            + [-4] * x + [5] * y + 1 * o = 0 ; (lhs=-1) ****

            name  lower level upper
            x         1     1     4
            y         1     1     5
            o      -inf     0   inf

        Hessian:
                                                 x                     y
                              --------------------  --------------------
                           x                    -6                     1
                           y                     1                    10

This example is similar to the example
of the linear row, but with some extras. First, the coefficients -4 and
5 are denoted between brackets to indicate that they are not fixed
coefficients, but first order derivative values taken at the level
values of the variables. We say that the variables ``x`` and ``y``
appear non-linear in the constraint ``o_definition``. The coefficient
``1`` before the variable ``o`` is also a first order derivative, but
the value of this coefficient does not depend on the values of the
variables and is therefore not denoted between brackets. We say that the
variable ``o`` appears linearly in the constraint ``o_definition``.
Next, to indicate that the constraint is infeasible, it is postfixed by
``****``. Finally, the Hessian containing the second order derivative
values is presented, by switching the option
``constraint_listing_Hessian`` to on. The Hessian is only presented for
those variables that appear non-linear in the constraint presented. A
typical question concerns the accuracy of these first and second order
derivative values. These derivative values are exact when the non-linear
expressions in the constraint only reference differentiable AIMMS
intrinsic functions. The first order derivative values are approximated
using differencing, when there is a non-linear expression in the
constraint referencing an external function. The second order derivative
values are not available when a non-linear expression references an
external function.

A COP row
~~~~~~~~~

Consider the artificial constraint: 

.. code-block:: aimms

        Constraint element_constraint {
            Definition   :  P(eV) = 7;
        }

This constraint will
lead to the following in the constraint listing. 

.. code-block:: aimms

        ----  element_constraint

        element_constraint .. [ 0 | 2 | not solved yet ]

            [1,4,7,10,13,..., 28 (size=10)][eV]
            = 7 ****

            name     lower    level    upper
            eV       'a01'    'a01'    'a10'

The main
difference between this example and the previous examples is that the
presentation is an instantiated symbolic form of the constraints as the
presentation of the first and second order derivatives is meaningless in
the context of constraint programming.

The footer of a constraint listing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The footer of the constraint listing contains statistics regarding the
size of the problem to give an impression of the relative difficulty of
the instance presented to other instances with the same structure. It
should be noted, that the structure of an instance may have more
influence on the difficulty to a solver than sheer size. The structure
of an instance depends on how it is modeled.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    A ``SOLVE`` statement may produce this constraint listing, depending on
    the option ``constraint_listing``, in the listing file.

.. seealso::

    -  The Mathematical Program Inspector is an interactive alternative to
       constraint listings and has additional facilities such as searching
       for an irreducible infeasibility set for linear program.

    -  The routine :aimms:func:`GMP::Instance::Generate`.
