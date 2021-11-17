.. aimms:procedure:: GMP::Column::SetTypeRaw(GMP, colSet, type)

.. _GMP::Column::SetTypeRaw:

GMP::Column::SetTypeRaw
=======================

The procedure :aimms:func:`GMP::Column::SetTypeRaw` changes the types of a
group of columns in a generated mathematical program.

.. code-block:: aimms

    GMP::Column::SetTypeRaw(
         GMP,            ! (input) a generated mathematical program
         colSet,         ! (input) a subset of Integers
         type            ! (input) an element parameter in AllColumnTypes
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *colSet*
        A subset of the set :aimms:set:`Integers`, representing a set of column
        numbers.

    *type*
        An element parameter in :aimms:set:`AllColumnTypes`, defined over *colSet*.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

Example
-------

    Assume that 'MP' is a mathematical program. To use
    :aimms:func:`GMP::Column::FreezeRaw` we declare the following identifiers
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
               ElementParameter ColType {
                   IndexDomain: cc;
                   Range: AllColumnTypes;
               }

    To change integer variable ``x(i)`` into a continuous variable we can use:

    .. code-block:: aimms

               myGMP := GMP::Instance::Generate( MP );
               
               VariableSet := { 'x' };
               ColumnSet := GMP::Instance::GetColumnNumbers( myGMP, VariableSet );
               
               ColType(cc) := 'continuous';
               
               GMP::Column::FreezeRaw( myGMP, ColumnSet, ColType );

.. seealso::

    The functions :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::GetColumnNumbers`, :aimms:func:`GMP::Column::GetType` and :aimms:func:`GMP::Column::SetType`.
