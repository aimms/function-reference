.. aimms:procedure:: GMP::Solution::SendToModel(GMP, solution)

.. _GMP::Solution::SendToModel:

GMP::Solution::SendToModel
==========================

The procedure :aimms:func:`GMP::Solution::SendToModel` initializes the model
identifiers with the values in the solution from the solution repository
of a generated mathematical program.

.. code-block:: aimms

    GMP::Solution::SendToModel(
         GMP,            ! (input) a generated mathematical program
         solution        ! (input) a solution
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *solution*
        An integer scalar reference to a solution.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    A solution vector in the solution repository only contains solution data
    for the generated columns and rows of the GMP. Hence, no solution data
    is stored in the solution repository for columns and rows that were not
    generated.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Solution::RetrieveFromModel`, :aimms:func:`GMP::Solution::RetrieveFromSolverSession` and :aimms:func:`GMP::Solution::SendToSolverSession`.
