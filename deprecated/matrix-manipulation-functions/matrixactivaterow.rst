.. aimms:procedure:: MatrixActivateRow(MP, row)

.. _MatrixActivateRow:

MatrixActivateRow
=================

The procedure :aimms:func:`MatrixActivateRow` activates a row in the matrix that
was previously deactivated.

.. code-block:: aimms

    MatrixActivateRow(
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

    As of AIMMS release 3.5, the matrix manipulation procedures have become
    deprecated. New projects should use the GMP library instead. Please
    refer to :numref:`table:matrix.procedures` for a mapping of the
    matrix manipulation procedures to corresponding GMP procedures.

.. seealso::

    The procedure :aimms:func:`MatrixDeactivateRow`. Matrix manipulation routines are discussed in
    more detail in :doc:`optimization-modeling-components/implementing-advanced-algorithms-for-mathematical-programs/index` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
