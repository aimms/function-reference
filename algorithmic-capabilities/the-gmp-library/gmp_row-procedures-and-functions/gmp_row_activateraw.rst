.. aimms:procedure:: GMP::Row::ActivateRaw(GMP, rowSet)

.. _GMP::Row::ActivateRaw:

GMP::Row::ActivateRaw
=====================

The procedure :aimms:func:`GMP::Row::ActivateRaw` activates a group of deactivated rows
in a generated mathematical program.

.. code-block:: aimms

    GMP::Row::ActivateRaw(
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
    :aimms:func:`GMP::Row::ActivateRaw` we declare the following identifiers
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

    To activate the constraint ``c(i)`` we can use:

    .. code-block:: aimms

               myGMP := GMP::Instance::Generate( MP );
               
               ConstraintSet := { 'c' };
               RowSet := GMP::Instance::GetRowNumbers( myGMP, ConstraintSet );
               
               GMP::Row::ActivateRaw( myGMP, RowSet );

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::GetRowNumbers`, :aimms:func:`GMP::Row::Activate` and :aimms:func:`GMP::Row::DeactivateRaw`.
