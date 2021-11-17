.. aimms:procedure:: GMP::Row::DeleteRaw(GMP, rowSet)

.. _GMP::Row::DeleteRaw:

GMP::Row::DeleteRaw
===================

The procedure :aimms:func:`GMP::Row::DeleteRaw` marks a group of rows
in a generated mathematical program as deleted.

.. code-block:: aimms

    GMP::Row::DeleteRaw(
         GMP,            ! (input) a generated mathematical program
         rowSet          ! (input) a subset of Integers
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *rowSet*
        A subset of the set :aimms:set:`Integers`, representing a set of row
        numbers.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  Deleted rows remain present in the generated mathematical
       program but their content will not be copied to a solver session.

    -  The rows will not be printed in the constraint listing, nor be
       visible in the Math Program Inspector and they will be removed from any
       solver maintained copies.

Example
-------

    Assume that 'MP' is a mathematical program. To use
    :aimms:func:`GMP::Row::DeleteRaw` we declare the following identifiers
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

    To delete the constraint ``c(i)`` we can use:

    .. code-block:: aimms

               myGMP := GMP::Instance::Generate( MP );
               
               ConstraintSet := { 'c' };
               RowSet := GMP::Instance::GetRowNumbers( myGMP, ConstraintSet );
               
               GMP::Row::DeleteRaw( myGMP, RowSet );

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::GetRowNumbers`, :aimms:func:`GMP::Row::Add` and :aimms:func:`GMP::Row::Delete`.
