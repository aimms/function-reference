.. aimms:procedure:: MatrixSaveState(MP, state)

.. _MatrixSaveState:

MatrixSaveState
===============

With the procedure :aimms:func:`MatrixSaveState` you can save the current state of
a mathematical program. Later on, after manipulating the mathematical
program, you can restore this state by calling ``MatrixRestoreState``.

.. code-block:: aimms

    MatrixSaveState(
         MP,             ! (input)  a mathematical program
         state           ! (output) an integer scalar parameter
         )

Arguments
---------

    *MP*
        A mathematical program that was previously solved. The mathematical
        program should be a linear or mixed-integer linear programming model.

    *state*
        On return, contains a positive integer value assigned to the state.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  States are numbered from 1 upwards by AIMMS.

    -  As of AIMMS release 3.5, the matrix manipulation procedures have
       become deprecated. New projects should use the GMP library instead.
       Please refer to :numref:`table:matrix.procedures` for a mapping
       of the matrix manipulation procedures to corresponding GMP
       procedures.

.. seealso::

    The procedure :aimms:func:`MatrixRestoreState`. Matrix manipulation routines are discussed in
    more detail in :doc:`optimization-modeling-components/implementing-advanced-algorithms-for-mathematical-programs/index` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
