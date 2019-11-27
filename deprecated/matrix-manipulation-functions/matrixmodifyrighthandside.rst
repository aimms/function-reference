.. aimms:function:: MatrixModifyRightHandSide(MP, row, value)

.. _MatrixModifyRightHandSide:

MatrixModifyRightHandSide
=========================

The procedure :aimms:func:`MatrixModifyRightHandSide` changes the right-hand-side
of a row in the matrix.

.. code-block:: aimms

    MatrixModifyRightHandSide(
         MP,             ! (input) a mathematical program
         row,            ! (input) a scalar value
         value           ! (input) a numerical expression
         )

Arguments
---------

    *MP*
        A mathematical program that was previously solved. The mathematical
        program should be a linear or mixed-integer linear programming model.

    *row*
        A scalar reference to an existing row in the matrix; this can not be the
        objective row.

    *value*
        The new value that should be assigned to the right-hand-side of the row.
        This value should be unequal to ``NA`` and ``UNDF`` (but might be
        ``INF`` or ``-INF``).

.. note::

    -  If you assign INF to the right-hand-side value of a row with type
       ``'='``, :aimms:func:`MatrixModifyRightHandSide` will not produce an error,
       since you might want to change the type of this row into ``'<='``
       (using ``MatrixModifyRowType``) immediately thereafter.

    -  After a call to ``MatrixSolve`` AIMMS checks for each modified row
       whether or not the right-hand-side value is valid for the current row
       type. If the row type is ``'='`` then the right-hand-side value
       should be unequal to ``INF`` and ``-INF``; if the row type is
       ``'<='`` or ``'ranged'`` then it should be unequal to ``-INF``.

    -  As of AIMMS release 3.5, the matrix manipulation procedures have
       become deprecated. New projects should use the GMP library instead.
       Please refer to :numref:`table:matrix.procedures` for a mapping
       of the matrix manipulation procedures to corresponding GMP
       procedures.

.. seealso::

    The procedures :aimms:func:`MatrixModifyLeftHandSide`, :aimms:func:`MatrixModifyRowType`, :aimms:func:`MatrixSolve`. Matrix manipulation
    routines are discussed in more detail in Chapter 16 of the Language
    Reference.
