.. aimms:function:: MasterMIPGetSolverStatus(None)

.. _MasterMIPGetSolverStatus:

MasterMIPGetSolverStatus
========================

The function :aimms:func:`MasterMIPGetSolverStatus` returns the solver status
associated with the last master MIP problem solved.

.. code-block:: aimms

    MasterMIPGetSolverStatus

Arguments
---------

    *None*

Return Value
------------

    The function :aimms:func:`MasterMIPGetSolverStatus` returns the solver status
    associated with the last master MIP problem solved. The return value
    will be an element in the set :aimms:set:`AllSolutionStates`.
