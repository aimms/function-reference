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
         solution,       ! (input) a solution
         [merge],        ! (optional, default 0) a scalar value
         [evalInline]    ! (optional, default 1) a scalar binary value
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *solution*
        An integer scalar reference to a solution.

    *merge*
        A scalar value to indicate whether the values of the variables and
        constraints in the mathematical program should be replaced by (value 0) or
        merged with (value 1 or 2) the solution.

    *evalInline*
        A scalar binary value to indicate whether the level values of inline variables
        (if any) in the mathematical program should be evaluated (value 1) or not (value 0).

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  A solution vector in the solution repository only contains solution data
       for the generated columns and rows of the GMP. Hence, no solution data
       is stored in the solution repository for columns and rows that were not
       generated.

    -  By default the values of the variables in the Variables set of the mathematical
       program will be emptied for all index tuples before sending the solution values
       to the variables. If the argument *merge* is set to 1 or 2 then only values of columns
       (i.e., individual variables) present in the *GMP* will be replaced. (The same holds
       for the constraints.)

    -  The difference between values 1 and 2 for argument *merge* only affects the objective variable.
       With value 1 the level value of the objective variable will be **increased** by the level value for
       the corresponding column in the *solution*. With value 2 the level value of the objective
       variable will be **replaced** by the level value for the corresponding column in the
       *solution*.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Solution::RetrieveFromModel`, :aimms:func:`GMP::Solution::RetrieveFromSolverSession`, :aimms:func:`GMP::Solution::SendToModelSelection` and :aimms:func:`GMP::Solution::SendToSolverSession`.
