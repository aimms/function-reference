.. aimms:procedure:: MatrixModifyQuadraticCoefficient(MP, col1, col2, value)

.. _MatrixModifyQuadraticCoefficient:

MatrixModifyQuadraticCoefficient
================================

The procedure :aimms:func:`MatrixModifyQuadraticCoefficient` changes a quadratic
coefficient in the objective row of a quadratic mathematical program.
The value for the coefficient can be equal to 0.0 prior to calling this
procedure.

.. code-block:: aimms

    MatrixModifyQuadraticCoefficient(
         MP,             ! (input) a mathematical program
         col1,           ! (input) a scalar value
         col2,           ! (input) a scalar value
         value           ! (input) a numerical expression
         )

Arguments
---------

    *MP*
        A mathematical program that was previously solved. The mathematical
        program should be a quadratic programming model.

    *col1*
        A scalar reference to an existing column.

    *col2*
        A scalar reference to an existing column.

    *value*
        The new value that should be assigned to the quadratic coefficient
        corresponding to *col1* and *col2* in the objective row. This value
        should be unequal to ``NA``, ``INF``, ``-INF`` and ``UNDF``.

Return Value
------------

    The procedure returns 1 on success, and 0 otherwise.

.. note::

    As of AIMMS release 3.5, the matrix manipulation procedures have become
    deprecated. New projects should use the GMP library instead. Please
    refer to :numref:`table:matrix.procedures` for a mapping of the
    matrix manipulation procedures to corresponding GMP procedures.

.. seealso::

    Matrix manipulation routines are discussed in more detail in :doc:`optimization-modeling-components/implementing-advanced-algorithms-for-mathematical-programs/index`
    of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
