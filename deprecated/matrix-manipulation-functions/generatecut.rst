.. aimms:procedure:: GenerateCut(Arow, local)

.. _GenerateCut:

GenerateCut
===========

The procedure :aimms:func:`GenerateCut` adds a row to the matrix during the
solution process of a mixed integer proghram.

.. code-block:: aimms

    GenerateCut(
         Arow,        ! (input) a scalar value
         [local]      ! (optional, default 1) a scalar binary expression
         )

Arguments
---------

    *Arow*
        A scalar reference to an existing row name in the model.

    *local*
        A scalar binary value to indicate whether the cut is valid for the local
        problem (i.e. the problem corresponding to the current node in the
        solution process and all its descendant nodes) only (value 1) or for the
        global problem (value 0).

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  This procedure can only be called from within a ``CallbackAddCut``
       callback procedure.

    -  A ``CallbackAddCut`` callback procedure will only be called when
       solving mixed integer programs with CPLEX, GUROBI or ODH-CPLEX.

.. seealso::

    See Section 15.2 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__ for more details on how to
    install a callback procedure to add cuts.
