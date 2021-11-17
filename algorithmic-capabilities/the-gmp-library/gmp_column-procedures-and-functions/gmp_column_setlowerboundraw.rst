.. aimms:procedure:: GMP::Column::SetLowerBoundRaw(GMP, colSet, value)

.. _GMP::Column::SetLowerBoundRaw:

GMP::Column::SetLowerBoundRaw
=============================

The procedure :aimms:func:`GMP::Column::SetLowerBoundRaw` changes the lower
bounds of a group of columns in a generated mathematical program.

.. code-block:: aimms

    GMP::Column::SetLowerBoundRaw(
         GMP,            ! (input) a generated mathematical program
         colSet,         ! (input) a subset of Integers
         value           ! (input) a parameter
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *colSet*
        A subset of the set :aimms:set:`Integers`, representing a set of column
        numbers.

    *value*
        A parameter defining a new lower bound for each column in *colSet*.

Return Value
------------

    The procedure returns 1 on success, and 0 otherwise.

.. note::

    If the variable has a unit then *value* should have the same unit. If
    *value* has no unit then you should multiply it by the column scale, as
    returned by the function :aimms:func:`GMP::Column::GetScale`. See
    :aimms:func:`GMP::Column::SetLowerBound` for an example with units.

Example
-------

    Assume that 'MP' is a mathematical program. To use
    :aimms:func:`GMP::Column::SetLowerBoundRaw` we declare the following identifiers
    (in ams format):
    
    .. code-block:: aimms

               ElementParameter myGMP {
                   Range: AllGeneratedMathematicalPrograms;
               }
               Set VariableSet {
                   SubsetOf: AllVariables;
               }
               Set ColumnSet {
                   SubsetOf: Integers;
                   Index: cc;
               }
               Parameter LB {
                   IndexDomain: cc;
               }

    To set the lower bounds of the variable ``x(i)`` we can use:

    .. code-block:: aimms

               myGMP := GMP::Instance::Generate( MP );
               
               VariableSet := { 'x' };
               ColumnSet := GMP::Instance::GetColumnNumbers( myGMP, VariableSet );
               
               LB(cc) := 0.0;
               
               GMP::Column::SetLowerBoundRaw( myGMP, ColumnSet, LB );

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::GetColumnNumbers`, :aimms:func:`GMP::Column::SetLowerBound`, :aimms:func:`GMP::Column::SetUpperBound`, :aimms:func:`GMP::Column::GetLowerBound` and :aimms:func:`GMP::Column::GetScale`.
