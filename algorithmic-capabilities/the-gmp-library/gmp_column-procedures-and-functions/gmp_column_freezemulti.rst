.. aimms:procedure:: GMP::Column::FreezeMulti(GMP, binding, column, value)

.. _GMP::Column::FreezeMulti:

GMP::Column::FreezeMulti
========================

The procedure :aimms:func:`GMP::Column::FreezeMulti` freezes a group of columns,
belonging to a variable, in a generated mathematical program.

.. code-block:: aimms

    GMP::Column::FreezeMulti(
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
        The new value for each column, defined over the *binding* domain,
        that should be used to freeze the column value.

Return Value
------------

    The procedure returns 1 on success, and 0 otherwise.

.. note::

    -  The columns remain visible in the constraint listing and math program
       inspector. In addition, it will be retained in solver maintained
       copies of the generated math program.

    -  Use :aimms:func:`GMP::Column::UnfreezeMulti` to undo the freezing.

    -  During a call to procedure :aimms:func:`GMP::Column::FreezeMulti` AIMMS stores
       the upper and lower bound of the columns before the procedure was
       called. This information is used when procedure
       :aimms:func:`GMP::Column::UnfreezeMulti` is called thereafter. This information
       is not copied by the function :aimms:func:`GMP::Instance::Copy`.

Example
-------

    To freeze variable ``x(i)`` to ``demand(i)`` we can use: 

    .. code-block:: aimms

               for (i) do
                   GMP::Column::Freeze( myGMP, x(i), demand(i) );
               endfor;

    It
    is more efficient to use: 

    .. code-block:: aimms

               GMP::Column::FreezeMulti( myGMP, i, x(i), demand(i) );

    If we only want to freeze those
    ``x(i)`` for which ``dom(i)`` is unequal to zero, then we use:

    .. code-block:: aimms

               GMP::Column::FreezeMulti( myGMP, i | dom(i), x(i), demand(i) );

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Column::Freeze`, :aimms:func:`GMP::Column::UnfreezeMulti` and :aimms:func:`GMP::Instance::Copy`.
