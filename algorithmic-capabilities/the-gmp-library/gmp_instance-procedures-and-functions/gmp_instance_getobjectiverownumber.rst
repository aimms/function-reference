.. aimms:function:: GMP::Instance::GetObjectiveRowNumber(GMP)

.. _GMP::Instance::GetObjectiveRowNumber:

GMP::Instance::GetObjectiveRowNumber
====================================

The function :aimms:func:`GMP::Instance::GetObjectiveRowNumber` returns the row
number corresponding to the constraint or variable definition that
defines the objective of a generated mathematical program.

.. code-block:: aimms

    GMP::Instance::GetObjectiveRowNumber(
         GMP             ! (input) a generated mathematical program
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

Return Value
------------

    The function returns the row number as an element of the set :aimms:set:`Integers`.
    If the generated mathematical program does not contain an objective then
    -1 is returned.

.. note::

    -  You should assign the return value of this function to an element
       parameter with range :aimms:set:`Integers` if you want to use it as (row)
       argument to call other GMP routines.

    -  If the objective variable appears in more than one constraint (or
       variable definition) then the row number of the first of those
       constraints will be returned.

Example
-------

Assume that we want to change the coefficients of all integer variables
in the objective to 10. This can be done as follows. 

.. code-block:: aimms

    RowNo := GMP::Instance::GetObjectiveRowNumber( myGMP );

    ColNrs := GMP::Instance::GetColumnNumbers( myGMP, AllIntegerVariables );

    for (c) do
        GMP::Coefficient::Set( myGMP, RowNo, c, 10 );
    endfor;

Here
``RowNo`` is an element parameter with range :aimms:set:`Integers` and ``ColNrs`` a
subset of :aimms:set:`Integers` with index ``c``.

.. seealso::

    - The functions :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::GetColumnNumbers`, :aimms:func:`GMP::Instance::GetObjectiveColumnNumber` and :aimms:func:`GMP::Instance::GetRowNumbers`.
