.. aimms:procedure:: GMP::Coefficient::SetRaw(GMP, rowSet, colSet, coef, changeZero)

.. _GMP::Coefficient::SetRaw:

GMP::Coefficient::SetRaw
========================

The procedure :aimms:func:`GMP::Coefficient::SetRaw` sets the value of a range
of (linear) coefficients for a group of columns and rows in a generated
mathematical program.

.. code-block:: aimms

    GMP::Coefficient::SetRaw(
         GMP,            ! (input) a generated mathematical program
         rowSet,         ! (input) a subset of Integers
         colSet,         ! (input) a subset of Integers
         coef,           ! (input) a parameter
         changeZero      ! (input) a binary parameter
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *rowSet*
        A subset of the set :aimms:set:`Integers`, representing a set of row
        numbers.

    *colSet*
        A subset of the set :aimms:set:`Integers`, representing a set of column
        numbers.

    *coef*
        A parameter over (*rowSet*, *colSet*) containing the new coefficient for
        each (row,column) combination.

    *changeZero*
        A binary parameter over (*rowSet*, *colSet*) which can be used to mark
        coefficients with a value of 0 (zero) in *coef* that should be changed
        by this procedure.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  A coefficient with a value of 0 (zero) will be skipped by this procedure
       unless *changeZero* is set to 1 for the corresponding (row, column) combination.
    
    -  This procedure cannot be used if one of the columns refers to the objective
       variable.

    -  In case the generated mathematical program is nonlinear, this
       procedure will fail if one the columns is part of a nonlinear term in
       one of the rows. However, if the row is pure quadratic, then this
       procedure can be used to set the linear coefficient value for a
       quadratic column.

    -  GMP procedures operate on a generated mathematical program in which
       all variables are moved to the left-hand-side of each constraint.
       This can have an influence on the sign of the coeffients as
       demonstrated in the example of procedure :aimms:func:`GMP::Coefficient::Set`.

Example
-------

Assume that ``MP`` is a mathematical program with the following
declaration (in ams format): 

.. code-block:: aimms

            Variable x {
                IndexDomain: t;
                Range: nonnegative;
            }
            Variable y {
                IndexDomain: t;
                Range: nonnegative;
            }
            Constraint c1 {
                IndexDomain: t;
                Definition: - 2 * x(t) + y(t) <= 4;
            }
            MathematicalProgram MP {
                Objective: obj;
                Direction: minimize;
                Type: LP;
            }

To use
:aimms:func:`GMP::Coefficient::SetRaw` we declare the following identifiers
(in ams format):

.. code-block:: aimms

    ElementParameter myGMP {
        Range: AllGeneratedMathematicalPrograms;
    }
    Set ConstraintSet {
        SubsetOf: AllConstraints;
    }
    Set VariableSet {
        SubsetOf: AllVariables;
    }
    Set RowSet {
        SubsetOf: Integers;
        Index: rr;
    }
    Set ColumnSet {
        SubsetOf: Integers;
        Index: cc;
    }
    Parameter Coef {
        IndexDomain: (rr,cc);
    }
    Parameter ChangeZero {
        IndexDomain: (rr,cc);
    }

To set the coefficients of variables ``x(t)`` and ``y(t)`` in constraint ``c1(t)``
to 1 and 0, respectively, we can use:

.. code-block:: aimms

    myGMP := GMP::Instance::Generate( MP );
    
    ConstraintSet := { 'c1' };
    RowSet := GMP::Instance::GetRowNumbers( myGMP, ConstraintSet );
    
    VariableSet := { 'x' };
    ColumnSet := GMP::Instance::GetColumnNumbers( myGMP, VariableSet );
    
    Coef(rr,cc) := 1.0;
    ChangeZero(rr,cc) := 0;
    
    GMP::Coefficient::SetRaw( myGMP, RowSet, ColumnSet, Coef, ChangeZero );
    
    VariableSet := { 'y' };
    ColumnSet := GMP::Instance::GetColumnNumbers( myGMP, VariableSet );
    
    Coef(rr,cc) := 0.0;
    ChangeZero(rr,cc) := 1;
    
    GMP::Coefficient::SetRaw( myGMP, RowSet, ColumnSet, Coef, ChangeZero );

.. seealso::

    - The routines :aimms:func:`GMP::Coefficient::Get`, :aimms:func:`GMP::Instance::GetColumnNumbers` and :aimms:func:`GMP::Instance::GetRowNumbers`.
