.. aimms:procedure:: MatrixModifyCoefficient(MP, row, column, value)

.. _MatrixModifyCoefficient:

MatrixModifyCoefficient
=======================

The procedure :aimms:func:`MatrixModifyCoefficient` changes a coefficient in the
matrix. This procedure can also be used to modify a coefficient in the
objective row. The value for the coefficient can be equal to 0.0 prior
to calling this procedure.

.. code-block:: aimms

    MatrixModifyCoefficient(
         MP,             ! (input) a mathematical program
         row,            ! (input) a scalar value
         column,         ! (input) a scalar value
         value           ! (input) a numerical expression
         )

Arguments
---------

    *MP*
        A mathematical program that was previously solved. The mathematical
        program should be a linear or mixed-integer linear programming model.

    *row*
        A scalar reference to an existing row in the matrix; this might be the
        objective row.

    *column*
        A scalar reference to an existing column in the matrix.

    *value*
        The new value that should be assigned to the coefficient corresponding
        to *row* and *column* in the matrix. This value should be unequal to
        ``NA``, ``INF``, ``-INF`` and ``UNDF``.

Return Value
------------

    The procedure returns 1 on success, and 0 otherwise.

.. note::

    As of AIMMS release 3.5, the matrix manipulation procedures have become
    deprecated. New projects should use the GMP library instead. Please
    refer to :numref:`table:matrix.procedures` for a mapping of the
    matrix manipulation procedures to corresponding GMP procedures.

.. seealso::

    Matrix manipulation routines are discussed in more detail in Chapter 16
    of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
