.. aimms:procedure:: MatrixAddRow(MP, row)

.. _MatrixAddRow:

MatrixAddRow
============

The procedure :aimms:func:`MatrixAddRow` adds a row to the matrix.

.. code-block:: aimms

    MatrixAddRow(
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

    -  Initially, the row will added with zero coefficients, regardless of
       whether the symbolic AIMMS constraint has a definition or not.
       Regeneration of all of the coefficients of the row according to its
       definition can be achieved through the procedure
       ``MatrixRegenerateRow``. Individual coefficients of the row can be
       added by calling the procedure ``MatrixModifyCoefficient``.

    -  After calling :aimms:func:`MatrixAddRow` the type of the row is set to ``'<='``
       and the right-hand-side value to ``INF`` (the left-hand-side value is
       set to ``-INF``). By using the procedures ``MatrixModifyRowType`` and
       ``MatrixModifyRightHandSide`` the row type and right-hand-side value
       can be changed.

    -  After a call to :aimms:func:`MatrixAddRow` or ``MatrixRegenerateRow`` for a
       certain row it is not allowed to do another call to :aimms:func:`MatrixAddRow`
       for that row.

    -  As of AIMMS release 3.5, the matrix manipulation procedures have
       become deprecated. New projects should use the GMP library instead.
       Please refer to :numref:`table:matrix.procedures` for a mapping
       of the matrix manipulation procedures to corresponding GMP
       procedures.

.. seealso::

    The procedures :aimms:func:`MatrixModifyCoefficient`, :aimms:func:`MatrixModifyLeftHandSide`, :aimms:func:`MatrixModifyRightHandSide`, :aimms:func:`MatrixModifyRowType`, :aimms:func:`MatrixRegenerateRow`.
    Matrix manipulation routines are discussed in more detail in :doc:`optimization-modeling-components/implementing-advanced-algorithms-for-mathematical-programs/index`
    of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
