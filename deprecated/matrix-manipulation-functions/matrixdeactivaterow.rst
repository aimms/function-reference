.. aimms:procedure:: MatrixDeactivateRow(MP, row)

.. _MatrixDeactivateRow:

MatrixDeactivateRow
===================

The procedure :aimms:func:`MatrixDeactivateRow` deactivates a row in the matrix.
The row will be ignored by the solver until it is activated again.

.. code-block:: aimms

    MatrixDeactivateRow(
         MP,             ! (input) a mathematical program
         row             ! (input) a scalar value
         )

Arguments
---------

    *MP*
        A mathematical program that was previously solved. The mathematical
        program should be a linear or mixed-integer linear programming model.

    *row*
        A scalar reference to an existing row in the matrix; this can not be the
        objective row.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  Deactivating a row results in changing the type of that row into
       ``'<'`` and the right hand side value into ``INF`` (the row
       coefficients do not change).

    -  As of AIMMS release 3.5, the matrix manipulation procedures have
       become deprecated. New projects should use the GMP library instead.
       Please refer to :numref:`table:matrix.procedures` for a mapping
       of the matrix manipulation procedures to corresponding GMP
       procedures.

.. seealso::

    The procedure :aimms:func:`MatrixActivateRow`. Matrix manipulation routines are discussed in
    more detail in Chapter 16 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
