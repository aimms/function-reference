.. aimms:procedure:: GMP::Instance::FixColumns(GMP1, GMP2, solution, variableSet, round)

.. _GMP::Instance::FixColumns:

GMP::Instance::FixColumns
=========================

The procedure :aimms:func:`GMP::Instance::FixColumns` sets the lower and upper
bounds of a set of columns in a generated mathematical program (*GMP1*)
equal to the level values of the corresponding columns in a solution of
a second generated mathematical program (*GMP2*).

.. code-block:: aimms

    GMP::Instance::FixColumns(
         GMP1,         ! (input) a generated mathematical program
         GMP2,         ! (input) a generated mathematical program
         solution,     ! (input) a solution
         variableSet,  ! (input) a set of variables
         [round]       ! (optional) a binary scalar value
         )

Arguments
---------

    *GMP1*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *GMP2*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *solution*
        An integer scalar reference to a solution in the solution repository of
        *GMP2*.

    *variableSet*
        A subset of :aimms:set:`AllVariables`.

    *round*
        A binary scalar indicating whether the level values of the integer
        columns should be rounded to the nearest integer value before fixing the
        columns. The default is 0 (no rounding).

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  A column corresponding to a variable in *variableSet* that is not
       part of *GMP1* will be ignored. This procedure will fail if a column
       corresponding to a variable in *variableSet* is not part of *GMP2*.

    -  If the objective variable is part of the set *variableSet* then it
       will be ignored, i.e., the objective variable will not be fixed.

    -  The same generated mathematical program can be used for *GMP1* and
       *GMP2*.

.. seealso::

    - The functions :aimms:func:`GMP::Instance::CreateSolverSession` and :aimms:func:`GMP::SolverSession::GetInstance`.
