.. aimms:procedure:: MatrixModifyType(MP, type)

.. _MatrixModifyType:

MatrixModifyType
================

The procedure :aimms:func:`MatrixModifyType` changes the type of a mathematical
program from ``'MIP'`` into ``'RMIP'``, or vice versa.

.. code-block:: aimms

    MatrixModifyType(
         MP,             ! (input) a mathematical program
         type            ! (input) a mathematical programming type
         )

Arguments
---------

    *MP*
        A mathematical program that was previously solved. The mathematical
        program should be a linear or mixed-integer linear programming model.

    *type*
        One of the types ``'MIP'`` or ``'RMIP'``.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    As of AIMMS release 3.5, the matrix manipulation procedures have become
    deprecated. New projects should use the GMP library instead. Please
    refer to :numref:`table:matrix.procedures` for a mapping of the
    matrix manipulation procedures to corresponding GMP procedures.

.. seealso::

    Matrix manipulation routines are discussed in more detail in :doc:`optimization-modeling-components/implementing-advanced-algorithms-for-mathematical-programs/index`
    of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
