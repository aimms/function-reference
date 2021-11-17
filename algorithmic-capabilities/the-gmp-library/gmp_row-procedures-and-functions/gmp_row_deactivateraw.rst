.. aimms:procedure:: GMP::Row::DeactivateRaw(GMP, rowSet)

.. _GMP::Row::DeactivateRaw:

GMP::Row::DeactivateRaw
=======================

The procedure :aimms:func:`GMP::Row::DeactivateRaw` deactivates a group of rows
in a generated mathematical program.

.. code-block:: aimms

    GMP::Row::DeactivateRaw(
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

    The procedure returns 1 on success, and 0 otherwise.

Example
-------

    Assume that 'MP' is a mathematical program. To use
    :aimms:func:`GMP::Row::DeactivateRaw` we declare the following identifiers
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

    To deactivate the constraint ``c(i)`` we can use:

    .. code-block:: aimms

               myGMP := GMP::Instance::Generate( MP );
               
               ConstraintSet := { 'c' };
               RowSet := GMP::Instance::GetRowNumbers( myGMP, ConstraintSet );
               
               GMP::Row::DeactivateRaw( myGMP, RowSet );

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::GetRowNumbers`, :aimms:func:`GMP::Row::ActivateRaw` and :aimms:func:`GMP::Row::Deactivate`.
