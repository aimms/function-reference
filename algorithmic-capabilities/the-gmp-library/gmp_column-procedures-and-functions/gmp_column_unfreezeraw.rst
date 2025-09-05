.. aimms:procedure:: GMP::Column::UnfreezeRaw(GMP, colSet)

.. _GMP::Column::UnfreezeRaw:

GMP::Column::UnfreezeRaw
========================

The procedure :aimms:func:`GMP::Column::UnfreezeRaw` removes the frozen status
of a group of columns in a generated mathematical program.

.. code-block:: aimms

    GMP::Column::UnfreezeRaw(
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

    The procedure returns 1 on success, and 0 otherwise.

.. note::

    During a call to procedure :aimms:func:`GMP::Column::FreezeRaw` AIMMS stores the
    upper and lower bound of the columns before the procedure was called. This
    information is used when procedure :aimms:func:`GMP::Column::UnfreezeRaw` is
    called thereafter. This information is not copied by the function
    :aimms:func:`GMP::Instance::Copy`.

Example
-------

Assume that ``MP`` is a mathematical program. To use
:aimms:func:`GMP::Column::UnfreezeRaw` we declare the following identifiers
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

To unfreeze the variable ``x(i)`` we can use:

.. code-block:: aimms

    myGMP := GMP::Instance::Generate( MP );
    
    VariableSet := { 'x' };
    ColumnSet := GMP::Instance::GetColumnNumbers( myGMP, VariableSet );
    
    GMP::Column::Unfreeze( myGMP, ColumnSet );

.. seealso::

    - The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::GetColumnNumbers`, :aimms:func:`GMP::Column::Unfreeze`, :aimms:func:`GMP::Column::FreezeRaw` and :aimms:func:`GMP::Instance::Copy`.
