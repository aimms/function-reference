.. aimms:function:: GMP::Instance::GetRowNumbers(GMP, constraintSet)

.. _GMP::Instance::GetRowNumbers:

GMP::Instance::GetRowNumbers
============================

The function :aimms:func:`GMP::Instance::GetRowNumbers` returns a subset of the
row numbers of a generated mathematical program. It returns the row
numbers that are generated for a set of constraints.

.. code-block:: aimms

    GMP::Instance::GetRowNumbers(
         GMP,                  ! (input) a generated mathematical program
         constraintSet        ! (input) a set of constraints
         )

Arguments
---------

    *GMP*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

    *constraintSet*
        A subset of the set :aimms:set:`AllConstraints`.

Return Value
------------

    The function returns a subset of the row numbers as a subset of the set
    :aimms:set:`Integers`.

Example
-------

    Assume we have generated a mathematical program and we want to change
    the right hand side of the constraints ``c1(i)`` and ``c2(j,k)`` into
    100. This can be done as follows: 

    .. code-block:: aimms

               myGMP := GMP::Instance::Generated( MP );

               for (i) do
                   GMP::Row::SetUpperBound( myGMP, c1(i), 100 );
               endfor;

               for (j,k) do
                   GMP::Row::SetRightHandSide( myGMP, c2(j,k), 100 );
               endfor;

    Using the function
    :aimms:func:`GMP::Instance::GetRowNumbers` this can also be coded as follows. Here
    ``RowNrs`` is a subset of :aimms:set:`Integers` with index ``r``, and ``Cons`` a
    subset of :aimms:set:`AllConstraints`. 

    .. code-block:: aimms

               myGMP := GMP::Instance::Generated( MP );

               Cons := { 'c1', 'c2' };

               RowNrs := GMP::Instance::GetRowNumbers( myGMP, Cons );

               for (r) do
                   GMP::Row::SetRightHandSide( myGMP, r, 100 );
               endfor;

.. seealso::

    The functions :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::GetColumnNumbers`, :aimms:func:`GMP::Instance::GetNumberOfRows`, :aimms:func:`GMP::Instance::GetObjectiveColumnNumber` and :aimms:func:`GMP::Instance::GetObjectiveRowNumber`.
