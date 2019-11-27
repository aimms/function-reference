.. aimms:function:: NLPGetProgramStatus(None)

.. _NLPGetProgramStatus:

NLPGetProgramStatus
===================

The function :aimms:func:`NLPGetProgramStatus` returns the program (or model)
status associated with the last NLP subproblem solved.

.. code-block:: aimms

    NLPGetProgramStatus

Arguments
---------

    *None*

Return Value
------------

    The function :aimms:func:`NLPGetProgramStatus` returns the program (or model)
    status associated with the last NLP subproblem solved. The return value
    will be an element in the set :aimms:set:`AllSolutionStates`.
