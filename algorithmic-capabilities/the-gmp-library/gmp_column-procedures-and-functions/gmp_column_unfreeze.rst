.. aimms:procedure:: GMP::Column::Unfreeze(GMP, column)

.. _GMP::Column::Unfreeze:

GMP::Column::Unfreeze
=====================

The procedure :aimms:func:`GMP::Column::Unfreeze` removes the frozen status of a
column in the matrix of a generated mathematical program.

.. code-block:: aimms

    GMP::Column::Unfreeze(
         GMP,            ! (input) a generated mathematical program
         column          ! (input) a scalar reference or column number
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *column*
        A scalar reference to an existing column in the matrix or the number of
        that column in the range :math:`\{ 0 .. n-1 \}` where :math:`n` is the
        number of columns in the matrix.

Return Value
------------

    The procedure returns 1 on success, and 0 otherwise.

.. note::

    -  Use ``GMP::Column::UnfreezeMulti`` if many columns corresponding to
       some variable have to be unfrozen, because that will be more
       efficient.

    -  During a call to function ``GMP::Column::Freeze`` AIMMS stores the
       upper and lower bound of the column before the function was called.
       This information is used when function :aimms:func:`GMP::Column::Unfreeze` is
       called thereafter. This information is not copied by the function
       ``GMP::Instance::Copy``. Therefore the call to
       :aimms:func:`GMP::Column::Unfreeze` in the following piece of code is useless:

       .. code-block:: aimms

                  GMP::Column::Freeze( gmp1, x1, 20 );
                  gmp2 := GMP::Instance::Copy( gmp1, "cpy" );
                  GMP::Column::Unfreeze( gmp2, x1 );

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Column::UnfreezeMulti`, :aimms:func:`GMP::Column::Freeze` and :aimms:func:`GMP::Instance::Copy`.
