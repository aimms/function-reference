.. aimms:procedure:: GMP::Column::UnfreezeMulti(GMP, binding, column)

.. _GMP::Column::UnfreezeMulti:

GMP::Column::UnfreezeMulti
==========================

The procedure :aimms:func:`GMP::Column::UnfreezeMulti` removes the frozen status
of a group of columns, belonging to a variable, in a generated mathematical program.

.. code-block:: aimms

    GMP::Column::UnfreezeMulti(
         GMP,            ! (input) a generated mathematical program
         binding,        ! (input) an index binding
         column          ! (input) a variable expression
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

Return Value
------------

    The procedure returns 1 on success, and 0 otherwise.

.. note::

    During a call to procedure :aimms:func:`GMP::Column::FreezeMulti` AIMMS stores the
    upper and lower bound of the columns before the procedure was called. This
    information is used when procedure :aimms:func:`GMP::Column::UnfreezeMulti` is
    called thereafter. This information is not copied by the function
    :aimms:func:`GMP::Instance::Copy`.

Example
-------

To unfreeze variable ``x(i)`` we can use: 

.. code-block:: aimms

    for (i) do
        GMP::Column::Unfreeze( myGMP, x(i) );
    endfor;

It is more
efficient to use: 

.. code-block:: aimms

    GMP::Column::UnfreezeMulti( myGMP, i, x(i) );

If we only want to unfreeze those ``x(i)``
for which ``dom(i)`` is unequal to zero, then we use: 

.. code-block:: aimms

    GMP::Column::UnfreezeMulti( myGMP, i | dom(i), x(i) );

.. seealso::

    - The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Column::Unfreeze`, :aimms:func:`GMP::Column::FreezeMulti` and :aimms:func:`GMP::Instance::Copy`.
