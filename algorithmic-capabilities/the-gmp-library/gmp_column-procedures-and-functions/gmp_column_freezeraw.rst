.. aimms:procedure:: GMP::Column::FreezeRaw(GMP, colSet, value)

.. _GMP::Column::FreezeRaw:

GMP::Column::FreezeRaw
======================

The procedure :aimms:func:`GMP::Column::FreezeRaw` freezes a group of columns
in a generated mathematical program.

.. code-block:: aimms

    GMP::Column::FreezeRaw(
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
        A parameter over *colSet*, defining the value for each column to which
        it should be frozen.

Return Value
------------

    The procedure returns 1 on success, and 0 otherwise.

.. note::

    -  The columns remain visible in the constraint listing and math program
       inspector. In addition, it will be retained in solver maintained
       copies of the generated math program.

    -  Use :aimms:func:`GMP::Column::UnfreezeRaw` to undo the freezing.

    -  During a call to procedure :aimms:func:`GMP::Column::FreezeRaw` AIMMS stores
       the upper and lower bound of the columns before the procedure was
       called. This information is used when procedure
       :aimms:func:`GMP::Column::UnfreezeRaw` is called thereafter. This information
       is not copied by the function :aimms:func:`GMP::Instance::Copy`.

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
               Parameter FixVal {
                   IndexDomain: cc;
               }

    To freeze the variable ``x(i)`` we can use:

    .. code-block:: aimms

               myGMP := GMP::Instance::Generate( MP );
               
               VariableSet := { 'x' };
               ColumnSet := GMP::Instance::GetColumnNumbers( myGMP, VariableSet );
               
               FixVal(cc) := 20.0;
               
               GMP::Column::FreezeRaw( myGMP, ColumnSet, FixVal );

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::GetColumnNumbers`, :aimms:func:`GMP::Column::Freeze`, :aimms:func:`GMP::Column::UnfreezeRaw` and :aimms:func:`GMP::Instance::Copy`.
