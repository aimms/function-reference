.. aimms:procedure:: GMP::Solution::SendToModelSelection(GMP, solution, Identifiers, Suffices)

.. _GMP::Solution::SendToModelSelection:

GMP::Solution::SendToModelSelection
===================================

The procedure :aimms:func:`GMP::Solution::SendToModelSelection` initializes a part
of the model identifiers with the values in the solution from the
solution repository of a generated mathematical program.

.. code-block:: aimms

    GMP::Solution::SendToModelSelection(
         GMP,            ! (input) a generated mathematical program
         solution,       ! (input) a solution
         Identifiers,    ! (input) a set expression
         Suffices        ! (input) a set expression
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *solution*
        An integer scalar reference to a solution.

    *Identifiers*
        A subset of the predefined set :aimms:set:`AllVariablesConstraints`, containing the set of all
        variables and constraints for which the values have to be changed into
        those of *solution*.

    *Suffices*
        A subset of the predefined set :aimms:set:`AllSuffixNames`, containing the set of suffixes
        for which the values of *Identifiers* have to be changed into those of
        *solution*.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  If the subset *Identifiers* contains a variable or constraint that is
       not part of the generated mathematical program, then that variable or
       constaint will be ingnored and its data will not change.

    -  If the subset *Suffices* contains a suffix other than 'Level',
       'Basic', 'ReducedCost', 'ShadowPrice', 'SmallestCoefficient',
       'NominalCoefficient', 'LargestCoefficient', 'SmallestValue',
       'LargestValue', 'SmallestRightHandSide', 'NominalRightHandSide',
       'LargestRightHandSide', 'SmallestShadowPrice' and
       'LargestShadowPrice', then that suffix will be ingnored and its data
       will not change.

    -  A solution vector in the solution repository only contains solution
       data for the generated columns and rows of the GMP. Hence, no
       solution data is stored in the solution repository for columns and
       rows that were not generated.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Solution::RetrieveFromModel`, :aimms:func:`GMP::Solution::RetrieveFromSolverSession`, :aimms:func:`GMP::Solution::SendToSolverSession` and :aimms:func:`GMP::Solution::SendToModel`
