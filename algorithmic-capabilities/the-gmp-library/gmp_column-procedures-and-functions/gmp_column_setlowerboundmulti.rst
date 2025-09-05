.. aimms:procedure:: GMP::Column::SetLowerBoundMulti(GMP, binding, column, value)

.. _GMP::Column::SetLowerBoundMulti:

GMP::Column::SetLowerBoundMulti
===============================

The procedure :aimms:func:`GMP::Column::SetLowerBoundMulti` changes the lower
bounds of a group of columns, belonging to a variable, in a generated
mathematical program.

.. code-block:: aimms

    GMP::Column::SetLowerBoundMulti(
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
        The new lower bound for each column, defined over the *binding* domain.

Return Value
------------

    The procedure returns 1 on success, and 0 otherwise.

.. note::

    If the variable has a unit then *value* should have the same unit. If
    *value* has no unit then you should multiply it by the column scale, as
    returned by the function :aimms:func:`GMP::Column::GetScale`. See
    :aimms:func:`GMP::Column::SetLowerBound` for an example with units.

Example
-------

To set the lower bounds of variable ``x(i)`` to ``lb(i)`` we can use:

.. code-block:: aimms

    for (i) do
        GMP::Column::SetLowerBound( myGMP, x(i), lb(i) );
    endfor;

It is more efficient to use: 

.. code-block:: aimms

    GMP::Column::SetLowerBoundMulti( myGMP, i, x(i), lb(i) );

If we only want to
set the lower bounds of those ``x(i)`` for which ``dom(i)`` is unequal
to zero, then we use: 

.. code-block:: aimms

    GMP::Column::SetLowerBoundMulti( myGMP, i | dom(i), x(i), lb(i) );

.. seealso::

    - The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Column::SetLowerBound`, :aimms:func:`GMP::Column::SetUpperBound`, :aimms:func:`GMP::Column::GetLowerBound` and :aimms:func:`GMP::Column::GetScale`.
