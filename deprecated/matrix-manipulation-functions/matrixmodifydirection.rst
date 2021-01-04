.. aimms:procedure:: MatrixModifyDirection(MP, direction)

.. _MatrixModifyDirection:

MatrixModifyDirection
=====================

The procedure :aimms:func:`MatrixModifyDirection` changes the direction of a
mathematical program to ``'maximize'``, ``'minimize'`` or ``'none'``.
The direction ``'none'`` is the instruction to the solver to find a
feasible solution. If the type of the mathematical program is ``'MIP'``
then the solver will try to find an integer feasible solution.

.. code-block:: aimms

    MatrixModifyDirection(
         MP,             ! (input) a mathematical program
         direction       ! (input) a direction
         )

Arguments
---------

    *MP*
        A mathematical program that was previously solved. The mathematical
        program should be a linear or mixed-integer linear programming model.

    *direction*
        One of the directions ``'maximize'``, ``'minimize'`` or ``'none'``.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    As of AIMMS release 3.5, the matrix manipulation procedures have become
    deprecated. New projects should use the GMP library instead. Please
    refer to :numref:`table:matrix.procedures` for a mapping of the
    matrix manipulation procedures to corresponding GMP procedures.

.. seealso::

    The set :aimms:set:`AllMatrixManipulationDirections`. Matrix manipulation routines are discussed in more
    detail in :doc:`optimization-modeling-components/implementing-advanced-algorithms-for-mathematical-programs/index` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
