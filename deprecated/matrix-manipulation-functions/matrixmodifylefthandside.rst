.. aimms:function:: MatrixModifyLeftHandSide(MP, row, value)

.. _MatrixModifyLeftHandSide:

MatrixModifyLeftHandSide
========================

The procedure :aimms:func:`MatrixModifyLeftHandSide` changes the left-hand-side of
a row in the matrix.

.. code-block:: aimms

    MatrixModifyLeftHandSide(
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
        A scalar reference to an existing ranged row in the matrix.

    *value*
        The new value that should be assigned to the left-hand-side of the row.
        This value should be unequal to ``NA``, ``UNDF`` and ``INF`` (but might
        be ``-INF``).

.. note::

    -  After a call to ``MatrixSolve`` AIMMS checks for each modified ranged
       row whether or not the left-hand-side value is valid, that is, the
       left-hand-side value should be unequal to ``INF``.

    -  As of AIMMS release 3.5, the matrix manipulation procedures have
       become deprecated. New projects should use the GMP library instead.
       Please refer to :numref:`table:matrix.procedures` for a mapping
       of the matrix manipulation procedures to corresponding GMP
       procedures.

.. seealso::

    The procedures :aimms:func:`MatrixModifyRightHandSide`, :aimms:func:`MatrixSolve`. Matrix manipulation routines are
    discussed in more detail in Chapter 16 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
