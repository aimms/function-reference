.. aimms:procedure:: GMP::Column::Freeze(GMP, column, value)

.. _GMP::Column::Freeze:

GMP::Column::Freeze
===================

The procedure :aimms:func:`GMP::Column::Freeze` freezes a column in the matrix of
a generated mathematical program at the given value.

.. code-block:: aimms

    GMP::Column::Freeze(
         GMP,            ! (input) a generated mathematical program
         column,         ! (input) a scalar reference or column number
         value           ! (input) a numerical expression
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *column*
        A scalar reference to an existing column in the matrix or the number of
        that column in the range :math:`\{ 0 .. n-1 \}` where :math:`n` is the
        number of columns in the matrix.

    *value*
        The new value that should be used to freeze the column value.

Return Value
------------

    The procedure returns 1 on success, and 0 otherwise.

.. note::

    -  Use ``GMP::Column::FreezeMulti`` if many columns corresponding to
       some variable have to be frozen, because that will be more efficient.

    -  The column remains visible in the constraint listing and math program
       inspector. In addition, it will be retained in solver maintained
       copies of the generated math program.

    -  Use ``GMP::Column::Unfreeze`` to undo the freezing.

    -  During a call to function :aimms:func:`GMP::Column::Freeze` AIMMS stores the
       upper and lower bound of the column before the function was called.
       This information is used when function ``GMP::Column::Unfreeze`` is
       called thereafter. This information is not copied by the function
       ``GMP::Instance::Copy``.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Column::FreezeMulti`, :aimms:func:`GMP::Column::Unfreeze` and :aimms:func:`GMP::Instance::Copy`.
