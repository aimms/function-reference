.. aimms:procedure:: MatrixRestoreState(MP, state)

.. _MatrixRestoreState:

MatrixRestoreState
==================

With procedure :aimms:func:`MatrixRestoreState` you can restore the state of your
mathematical program as it was on the moment that you called
``MatrixSaveState``.

.. code-block:: aimms

    MatrixRestoreState(
         MP,             ! (input) a mathematical program
         state           ! (input) an integer scalar parameter
         )

Arguments
---------

    *MP*
        A mathematical program that was previously solved. The mathematical
        program should be a linear or mixed-integer linear programming model.

    *state*
        The value corresponding to a state that you want to restore.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    As of AIMMS release 3.5, the matrix manipulation procedures have become
    deprecated. New projects should use the GMP library instead. Please
    refer to :numref:`table:matrix.procedures` for a mapping of the
    matrix manipulation procedures to corresponding GMP procedures.

.. seealso::

    The procedure :aimms:func:`MatrixSaveState`. Matrix manipulation routines are discussed in
    more detail in :doc:`optimization-modeling-components/implementing-advanced-algorithms-for-mathematical-programs/index` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
