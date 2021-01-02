.. aimms:procedure:: MatrixUnfreezeColumn(MP, column)

.. _MatrixUnfreezeColumn:

MatrixUnfreezeColumn
====================

The procedure :aimms:func:`MatrixUnfreezeColumn` frees a column that was fixed
with ``MatrixFreezeColumn``. After calling :aimms:func:`MatrixUnfreezeColumn` the
value of the column can vary again between its lower and upper bound.

.. code-block:: aimms

    MatrixUnfreezeColumn(
         MP,             ! (input) a mathematical program
         column          ! (input) a scalar value
         )

Arguments
---------

    *MP*
        A mathematical program that was previously solved. The mathematical
        program should be a linear or mixed-integer linear programming model.

    *column*
        A scalar reference to an existing fixed column in the matrix.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    As of AIMMS release 3.5, the matrix manipulation procedures have become
    deprecated. New projects should use the GMP library instead. Please
    refer to :numref:`table:matrix.procedures` for a mapping of the
    matrix manipulation procedures to corresponding GMP procedures.

.. seealso::

    The procedures :aimms:func:`MatrixFreezeColumn`, :aimms:func:`MatrixModifyLowerBound`, :aimms:func:`MatrixModifyUpperBound`. Matrix manipulation
    routines are discussed in more detail in :doc:`optimization-modeling-components/implementing-advanced-algorithms-for-mathematical-programs/index` of the Language
    Reference.
