.. aimms:procedure:: MatrixModifyUpperBound(MP, column, value)

.. _MatrixModifyUpperBound:

MatrixModifyUpperBound
======================

The procedure :aimms:func:`MatrixModifyUpperBound` changes the upper bound of a
column in the matrix.

.. code-block:: aimms

    MatrixModifyUpperBound(
         MP,             ! (input) a mathematical program
         column,         ! (input) a scalar value
         value           ! (input) a numerical expression
         )

Arguments
---------

    *MP*
        A mathematical program that was previously solved. The mathematical
        program should be a linear or mixed-integer linear programming model.

    *column*
        A scalar reference to an existing column in the matrix.

    *value*
        The new value that should be assigned to the upper bound of the column.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    As of AIMMS release 3.5, the matrix manipulation procedures have become
    deprecated. New projects should use the GMP library instead. Please
    refer to :numref:`table:matrix.procedures` for a mapping of the
    matrix manipulation procedures to corresponding GMP procedures.

.. seealso::

    The procedure :aimms:func:`MatrixModifyLowerBound`. Matrix manipulation routines are discussed in
    more detail in :doc:`optimization-modeling-components/implementing-advanced-algorithms-for-mathematical-programs/index` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
