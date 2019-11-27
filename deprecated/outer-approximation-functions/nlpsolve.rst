.. aimms:function:: NLPSolve(FrozenVariables)

.. _NLPSolve:

NLPSolve
========

The procedure :aimms:func:`NLPSolve` calls the NLP solver to solve the NLP
subproblem in which the (symbolic) integer variables in the set
FrozenVariables remain frozen during the solve, and all other integer
variables are considered to be continuous between their bounds.

.. code-block:: aimms

    NLPSolve(
         FrozenVariables      ! (input) subset of the set AllIntegerVariables
         )

Arguments
---------

    *FrozenVariables*
        The set of (symbolic) integer variables that remain frozen during the
        solve of the NLP. This is a subset of :aimms:set:`AllIntegerVariables`.

Return Value
------------

    ``NLPSolve()`` has no return value.
