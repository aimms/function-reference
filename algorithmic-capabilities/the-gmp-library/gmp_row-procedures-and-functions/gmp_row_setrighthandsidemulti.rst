.. aimms:procedure:: GMP::Row::SetRightHandSideMulti(GMP, binding, row, value)

.. _GMP::Row::SetRightHandSideMulti:

GMP::Row::SetRightHandSideMulti
===============================

The procedure :aimms:func:`GMP::Row::SetRightHandSideMulti` changes the
right-hand-side of a group of row, belonging to a constraint, in a
generated mathematical program.

.. code-block:: aimms

    GMP::Row::SetRightHandSideMulti(
         GMP,            ! (input) a generated mathematical program
         binding,        ! (input) an index binding
         row,            ! (input) a constraint expression
         value           ! (input) a numerical expression
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *binding*
        An index binding that specifies and possibly limits the scope of
        indices.

    *row*
        A constraint that, combined with the ``binding`` domain, specifies the
        rows.

    *value*
        The new right-hand-side for each row, defined over the binding domain
        ``binding``.

Return Value
------------

    The procedure returns 1 on success, and 0 otherwise.

.. note::

    If the constraint has a unit then *value* should have the same unit. If
    *value* has no unit then you should multiply it by the row scale, as
    returned by the function ``GMP::Row::GetScale``. See
    ``GMP::Row::SetRightHandSide`` for an example with units.

Example
-------

    To set the right-hand-side values of constraint ``c(i)`` to ``rhs(i)``
    we can use: 

    .. code-block:: aimms

               for (i) do
                   GMP::Row::SetRightHandSide( myGMP, c(i), rhs(i) );
               endfor;

    It is more efficient to use: 

    .. code-block:: aimms

               GMP::Row::SetRightHandSideMulti( myGMP, i, c(i), rhs(i) );

    If we
    only want to set the right-hand-side values of those ``c(i)`` for which
    ``dom(i)`` is unequal to zero, then we use: 

    .. code-block:: aimms

               GMP::Row::SetRightHandSideMulti( myGMP, i | dom(i), c(i), rhs(i) );

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Row::SetRightHandSide`, :aimms:func:`GMP::Row::SetLeftHandSide`, :aimms:func:`GMP::Row::GetRightHandSide` and :aimms:func:`GMP::Row::GetScale`.
