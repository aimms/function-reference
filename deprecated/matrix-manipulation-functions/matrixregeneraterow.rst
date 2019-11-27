.. aimms:procedure:: MatrixRegenerateRow(MP, row)

.. _MatrixRegenerateRow:

MatrixRegenerateRow
===================

The procedure :aimms:func:`MatrixRegenerateRow` regenerates the coefficients of a
row according to the definition of its associated symbolic constraint in
the model.

.. code-block:: aimms

    MatrixRegenerateRow(
         MP,             ! (input) a mathematical program
         row             ! (input) a scalar value
         )

Arguments
---------

    *MP*
        A mathematical program that was previously solved. The mathematical
        program should be a linear or mixed-integer linear programming model.

    *row*
        A scalar reference to an existing row name in the model.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  If the row does not exist yet, it will be automatically added to the
       matrix before generating its coefficients.

    -  Before regenerating the row, the procedure first removes all existing
       matrix coefficients.

    -  This procedure will automatically add columns that are not in the
       matrix.

    -  The row type and the right-hand-side value (and, if the row type is
       ``'ranged'``, the left-hand-side value) are set according to the
       constraint definition.

    -  As of AIMMS release 3.5, the matrix manipulation procedures have
       become deprecated. New projects should use the GMP library instead.
       Please refer to :numref:`table:matrix.procedures` for a mapping
       of the matrix manipulation procedures to corresponding GMP
       procedures.

.. seealso::

    The procedures :aimms:func:`MatrixAddRow`, :aimms:func:`MatrixModifyCoefficient`, :aimms:func:`MatrixModifyLeftHandSide`, :aimms:func:`MatrixModifyRightHandSide`, :aimms:func:`MatrixModifyRowType`.
    Matrix manipulation routines are discussed in more detail in Chapter 16
    of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
