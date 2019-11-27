.. aimms:function:: NLPGetSolverStatus(None)

.. _NLPGetSolverStatus:

NLPGetSolverStatus
==================

The function :aimms:func:`NLPGetSolverStatus` returns the solver status associated
with the last NLP subproblem solved.

.. code-block:: aimms

    NLPGetSolverStatus

Arguments
---------

    *None*

Return Value
------------

    The function :aimms:func:`NLPGetSolverStatus` returns the solver status associated
    with the last NLP subproblem solved. The return value will be an element
    in the set :aimms:set:`AllSolutionStates`.
