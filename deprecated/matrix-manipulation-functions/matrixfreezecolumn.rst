.. aimms:procedure:: MatrixFreezeColumn(MP, row, value)

.. _MatrixFreezeColumn:

MatrixFreezeColumn
==================

The procedure :aimms:func:`MatrixFreezeColumn` fixes the value of a column in the
model. The column can be freed by using ``MatrixUnfreezeColumn``.

.. code-block:: aimms

    MatrixFreezeColumn(
         MP,             ! (input) a mathematical program
         column,         ! (input) a scalar value
         value           ! (input) a numerical expression
         )

Arguments
---------

    *MP*
        A mathematical program that was previously solved. The mathematical
        program should be a linear or mixed-integer linear programming model.

    *row*
        A scalar reference to an existing column in the matrix.

    *value*
        The value to which the column should be fixed.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  Fixing a column to a certain value has the same effect as changing
       the lower and upper bound into that value.

    -  As of AIMMS release 3.5, the matrix manipulation procedures have
       become deprecated. New projects should use the GMP library instead.
       Please refer to :numref:`table:matrix.procedures` for a mapping
       of the matrix manipulation procedures to corresponding GMP
       procedures.

.. seealso::

    The procedures :aimms:func:`MatrixModifyLowerBound`, :aimms:func:`MatrixModifyUpperBound`, :aimms:func:`MatrixUnfreezeColumn`. Matrix manipulation
    routines are discussed in more detail in Chapter 16 of the Language
    Reference.
