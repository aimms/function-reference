.. aimms:procedure:: MatrixGenerate(MP)

.. _MatrixGenerate:

MatrixGenerate
==============

The procedure :aimms:func:`MatrixGenerate` instructs AIMMS to generate a
mathematical program without actually solving it.

.. code-block:: aimms

    MatrixGenerate(
         MP              ! (input) a mathematical program
         )

Arguments
---------

    *MP*
        A mathematical program to be generated. The mathematical program should
        be a linear, mixed-integer linear or quadratic programming model.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  The procedure :aimms:func:`MatrixGenerate` can be used to generate a
       mathematical program, if your algorithm does not call the ``SOLVE``
       statement to solve it initially, prior using the matrix manipulation
       routines.

    -  As of AIMMS release 3.5, the matrix manipulation procedures have
       become deprecated. New projects should use the GMP library instead.
       Please refer to :numref:`table:matrix.procedures` for a mapping
       of the matrix manipulation procedures to corresponding GMP
       procedures.

.. seealso::

    Matrix manipulation routines are discussed in more detail in :doc:`optimization-modeling-components/implementing-advanced-algorithms-for-mathematical-programs/index`
    of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
