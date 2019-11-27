.. aimms:function:: MatrixModifyRowType(MP, row, type)

.. _MatrixModifyRowType:

MatrixModifyRowType
===================

The procedure :aimms:func:`MatrixModifyRowType` changes the type of a row in the
matrix.

.. code-block:: aimms

    MatrixModifyRowType(
         MP,             ! (input) a mathematical program
         row,            ! (input) a scalar value
         type            ! (input) a row type
         )

Arguments
---------

    *MP*
        A mathematical program that was previously solved. The mathematical
        program should be a linear or mixed-integer linear programming model.

    *row*
        A scalar reference to an existing row in the matrix; this can not be the
        objective row.

    *type*
        One of the row types ``'<='``, ``'='``, ``'>='`` or ``'ranged'`` that
        should be assigned to the row.

.. note::

    -  | The following examples show what happens if we change the row type
         into ``'ranged'``:
       | ``a(x) <= 3`` modified into ``'ranged'`` results in
         ``-inf <= a(x) <= 3``
       | ``a(x) >= 3`` modified into ``'ranged'`` results in
         ``   3 <= a(x) <= inf``
       | ``a(x)  = 3`` modified into ``'ranged'`` results in
         ``   3 <= a(x) <= 3``
       | The next examples show what happens if we change the row type of a
         ``'ranged'`` row:
       | ``2 <= a(x) <= 4`` modified into ``'<='`` results in ``a(x) <= 4``
       | ``2 <= a(x) <= 4`` modified into ``'>='`` results in ``a(x) >= 2``
       | ``2 <= a(x) <= 4`` modified into `` '='`` results in ``a(x)  = 4``

    -  As of AIMMS release 3.5, the matrix manipulation procedures have
       become deprecated. New projects should use the GMP library instead.
       Please refer to :numref:`table:matrix.procedures` for a mapping
       of the matrix manipulation procedures to corresponding GMP
       procedures.

.. seealso::

    Matrix manipulation routines are discussed in more detail in Chapter 16
    of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
