.. aimms:procedure:: GMP::Row::SetTypeRaw(GMP, rowSet, type)

.. _GMP::Row::SetTypeRaw:

GMP::Row::SetTypeRaw
====================

The procedure :aimms:func:`GMP::Row::SetTypeRaw` changes the types of a group of rows
in a generated mathematical program.

.. code-block:: aimms

    GMP::Row::SetTypeRaw(
         GMP,            ! (input) a generated mathematical program
         rowSet,         ! (input) a subset of Integers
         type            ! (input) an element parameter in AllRowTypes
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *rowSet*
        A subset of the set :aimms:set:`Integers`, representing a set of row
        numbers.

    *type*
        An element parameter in :aimms:set:`AllRowTypes`, defined over the *binding* domain.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

Example
-------

Assume that ``MP`` is a mathematical program. To use
:aimms:func:`GMP::Row::SetTypeRaw` we declare the following identifiers
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
    ElementParameter RowType {
        IndexDomain: rr;
        Range: AllRowTypes;
    }

To change the constraint ``c(i)`` in a less-than-or-equal-to constraint we can use:

.. code-block:: aimms

    myGMP := GMP::Instance::Generate( MP );
    
    ConstraintSet := { 'c' };
    RowSet := GMP::Instance::GetRowNumbers( myGMP, ConstraintSet );
    
    RowType(rr) := '<=';
    
    GMP::Row::SetTypeRaw( myGMP, RowSet, RowType );

.. seealso::

    - The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Row::GetType` and :aimms:func:`GMP::Row::SetType`.
