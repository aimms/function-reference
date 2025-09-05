.. aimms:function:: GMP::Instance::GetObjectiveColumnNumber(GMP)

.. _GMP::Instance::GetObjectiveColumnNumber:

GMP::Instance::GetObjectiveColumnNumber
=======================================

The function :aimms:func:`GMP::Instance::GetObjectiveColumnNumber` returns the
column number corresponding to the objective variable of a generated
mathematical program.

.. code-block:: aimms

    GMP::Instance::GetObjectiveColumnNumber(
         GMP             ! (input) a generated mathematical program
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

Return Value
------------

    The function returns the column number as an element of the set
    :aimms:set:`Integers`. If the generated mathematical program does not contain an
    objective then -1 is returned.

.. note::

    You should assign the return value of this function to an element
    parameter with range :aimms:set:`Integers` if you want to use it as (column)
    argument to call other GMP routines.

Example
-------

Let ``ColNo`` be an element parameter with range :aimms:set:`Integers`. 

.. code-block:: aimms

    ColNo := GMP::Instance::GetObjectiveColumnNumber( myGMP );

    value := GMP::Solution::GetColumnValue( myGMP, 1, ColNo );

.. seealso::

    - The functions :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::GetColumnNumbers`, :aimms:func:`GMP::Instance::GetObjectiveRowNumber` and :aimms:func:`GMP::Instance::GetRowNumbers`.
