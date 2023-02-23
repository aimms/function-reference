.. aimms:function:: GMP::Instance::GetColumnNumbers(GMP, variableSet)

.. _GMP::Instance::GetColumnNumbers:

GMP::Instance::GetColumnNumbers
===============================

The function :aimms:func:`GMP::Instance::GetColumnNumbers` returns a subset of the
column numbers of a generated mathematical program. It returns the
column numbers that are generated for a set of variables.

.. code-block:: aimms

    GMP::Instance::GetColumnNumbers(
         GMP,                ! (input) a generated mathematical program
         variableSet         ! (input) a set of variables
         )

Arguments
---------

    *GMP*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

    *variableSet*
        A subset of the set :aimms:set:`AllVariables`.

Return Value
------------

    The function returns a subset of the column numbers as a subset of the
    set :aimms:set:`Integers`.

Example
-------

    Assume we have generated a mathematical program and we want to change
    the upper bound of the variables ``demand(i)`` and ``supply(j,k)`` into
    100. This can be done as follows: 

    .. code-block:: aimms

               myGMP := GMP::Instance::Generated( MP );

               for (i) do
                   GMP::Column::SetUpperBound( myGMP, demand(i), 100 );
               endfor;

               for (j,k) do
                   GMP::Column::SetUpperBound( myGMP, supply(j,k), 100 );
               endfor;

    Using the function
    :aimms:func:`GMP::Instance::GetColumnNumbers` this can also be coded as follows.
    Here ``ColNrs`` is a subset of :aimms:set:`Integers` with index ``c``, and ``Vars``
    a subset of :aimms:set:`AllVariables`. 

    .. code-block:: aimms

               myGMP := GMP::Instance::Generated( MP );

               Vars := { 'demand', 'supply' };

               ColNrs := GMP::Instance::GetColumnNumbers( myGMP, Vars );

               for (c) do
                   GMP::Column::SetUpperBound( myGMP, c, 100 );
               endfor;

.. seealso::

    The functions :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::GetNumberOfColumns`, :aimms:func:`GMP::Instance::GetRowNumbers`, :aimms:func:`GMP::Instance::GetObjectiveColumnNumber` and :aimms:func:`GMP::Instance::GetObjectiveRowNumber`.
