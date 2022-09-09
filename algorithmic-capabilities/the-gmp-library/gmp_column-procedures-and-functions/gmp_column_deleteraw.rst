.. aimms:procedure:: GMP::Column::DeleteRaw(GMP, colSet)

.. _GMP::Column::DeleteRaw:

GMP::Column::DeleteRaw
======================

The procedure :aimms:func:`GMP::Column::DeleteRaw` marks a group of columns in
a generated mathematical program as deleted.

.. code-block:: aimms

    GMP::Column::DeleteRaw(
         GMP,            ! (input) a generated mathematical program
         colSet          ! (input) a subset of Integers
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *colSet*
        A subset of the set :aimms:set:`Integers`, representing a set of column
        numbers.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  The columns will not be printed in the constraint listing, nor be
       visible in the Math Program Inspector and they will be removed from any
       solver maintained copies.

Example
-------

    Assume that 'MP' is a mathematical program. To use
    :aimms:func:`GMP::Column::DeleteRaw` we declare the following identifiers
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

    To delete the variable ``x(i)`` we can use:

    .. code-block:: aimms

               myGMP := GMP::Instance::Generate( MP );
               
               VariableSet := { 'x' };
               ColumnSet := GMP::Instance::GetColumnNumbers( myGMP, VariableSet );
               
               GMP::Column::DeleteRaw( myGMP, ColumnSet );

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::GetColumnNumbers` and :aimms:func:`GMP::Column::Delete`.
