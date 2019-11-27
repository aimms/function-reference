.. aimms:function:: MasterMIPGetProgramStatus(None)

.. _MasterMIPGetProgramStatus:

MasterMIPGetProgramStatus
=========================

The function :aimms:func:`MasterMIPGetProgramStatus` returns the program (or
model) status associated with the last master MIP problem solved.

.. code-block:: aimms

    MasterMIPGetProgramStatus

Arguments
---------

    *None*

Return Value
------------

    The function :aimms:func:`MasterMIPGetProgramStatus` returns the program (or
    model) status associated with the last master MIP problem solved. The
    return value will be an element in the set :aimms:set:`AllSolutionStates`.
