.. aimms:procedure:: GMP::Row::SetRightHandSideRaw(GMP, rowSet, value)

.. _GMP::Row::SetRightHandSideMulti:

GMP::Row::SetRightHandSideRaw
=============================

The procedure :aimms:func:`GMP::Row::SetRightHandSideRaw` changes the
right-hand-sides of a group of rows in a generated mathematical program.

.. code-block:: aimms

    GMP::Row::SetRightHandSideRaw(
         GMP,            ! (input) a generated mathematical program
         rowSet,         ! (input) a subset of Integers
         value           ! (input) a parameter
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *rowSet*
        A subset of the set :aimms:set:`Integers`, representing a set of row
        numbers.

    *value*
        A parameter defining a new right-hand-side for each row in *rowSet*.

Return Value
------------

    The procedure returns 1 on success, and 0 otherwise.

.. note::

    If the constraint has a unit then *value* should have the same unit. If
    *value* has no unit then you should multiply it by the row scale, as
    returned by the function :aimms:func:`GMP::Row::GetScale`. See
    :aimms:func:`GMP::Row::SetRightHandSide` for an example with units.

Example
-------

    Assume that 'MP' is a mathematical program. To use
    :aimms:func:`GMP::Row::SetRightHandSideRaw` we declare the following identifiers
    (in ams format):
    
    .. code-block:: aimms

               ElementParameter myGMP {
                   Range: AllGeneratedMathematicalPrograms;
               }
               Set ConstraintSet {
                   SubsetOf: AllConstraints;
               }
               Set RowSet {
                   SubsetOf: Integers;
                   Index: rr;
               }
               Parameter RHS {
                   IndexDomain: rr;
               }

    To change the right-hand-side values of the constraint ``c(i)`` we can use:

    .. code-block:: aimms

               myGMP := GMP::Instance::Generate( MP );
               
               ConstraintSet := { 'c' };
               RowSet := GMP::Instance::GetRowNumbers( myGMP, ConstraintSet );
               
               RHS(rr) := 5.0;
               
               GMP::Row::SetRightHandSideRaw( myGMP, RowSet, RHS );

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Row::SetRightHandSide`, :aimms:func:`GMP::Row::SetLeftHandSide`, :aimms:func:`GMP::Row::GetRightHandSide` and :aimms:func:`GMP::Row::GetScale`.
