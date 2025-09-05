.. aimms:procedure:: GMP::Column::SetUpperBoundMulti(GMP, binding, column, value)

.. _GMP::Column::SetUpperBoundMulti:

GMP::Column::SetUpperBoundMulti
===============================

The procedure :aimms:func:`GMP::Column::SetUpperBoundMulti` changes the upper
bounds of a group of columns, belonging to a variable, in the generated
mathematical program.

.. code-block:: aimms

    GMP::Column::SetUpperBoundMulti(
         GMP,            ! (input) a generated mathematical program
         binding,        ! (input) an index binding
         column,         ! (input) a variable expression
         value           ! (input) a numerical expression
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *binding*
        An index binding that specifies and possibly limits the scope of
        indices.

    *column*
        A variable that, combined with the *binding* domain, specifies the
        columns.

    *value*
        The new upper bound for each column, defined over the *binding* domain.

Return Value
------------

    The procedure returns 1 on success, and 0 otherwise.

.. note::

    If the variable has a unit then *value* should have the same unit. If
    *value* has no unit then you should multiply it by the column scale, as
    returned by the function :aimms:func:`GMP::Column::GetScale`. See
    :aimms:func:`GMP::Column::SetUpperBound` for an example with units.

Example
-------

To set the upper bounds of variable ``x(i)`` to ``ub(i)`` we can use:

.. code-block:: aimms

    for (i) do
        GMP::Column::SetUpperBound( myGMP, x(i), ub(i) );
    endfor;

It is more efficient to use: 

.. code-block:: aimms

    GMP::Column::SetUpperBoundMulti( myGMP, i, x(i), ub(i) );

If we only want to
set the upper bounds of those ``x(i)`` for which ``dom(i)`` is unequal
to zero, then we use: 

.. code-block:: aimms

    GMP::Column::SetUpperBoundMulti( myGMP, i | dom(i), x(i), ub(i) );

.. seealso::

    - The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Column::SetUpperBound`, :aimms:func:`GMP::Column::SetLowerBound`, :aimms:func:`GMP::Column::GetUpperBound` and :aimms:func:`GMP::Column::GetScale`.
