.. aimms:procedure:: MatrixSolve(MP)

.. _MatrixSolve:

MatrixSolve
===========

The procedure :aimms:func:`MatrixSolve` instructs the solver to solve a
mathematical program in its current state after being modified by using
several matrix manipulation procedures.

.. code-block:: aimms

    MatrixSolve(
         MP              ! (input) a mathematical program
         )

Arguments
---------

    *MP*
        A mathematical program that was previously solved or generated. The
        mathematical program should be a linear, mixed-integer linear or
        quadratic programming model.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  After a call to :aimms:func:`MatrixSolve` AIMMS will first check if all
       modifications performed by calling matrix manipulation procedures are
       all valid, before actually calling the solver. Most errors, however,
       will be filtered out by the matrix manipulation procedures
       themselves.

    -  As of AIMMS release 3.5, the matrix manipulation procedures have
       become deprecated. New projects should use the GMP library instead.
       Please refer to :numref:`table:matrix.procedures` for a mapping
       of the matrix manipulation procedures to corresponding GMP
       procedures.

.. seealso::

    The procedure :aimms:func:`MatrixGenerate`. Matrix manipulation routines are discussed in
    more detail in :doc:`optimization-modeling-components/implementing-advanced-algorithms-for-mathematical-programs/index` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
