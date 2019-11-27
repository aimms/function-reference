.. aimms:function:: MasterMIPSolve(None)

.. _MasterMIPSolve:

MasterMIPSolve
==============

The procedure :aimms:func:`MasterMIPSolve` calls the MIP solver to solve the
master MIP problem. Any modifications that have been made since the last
call to :aimms:func:`MasterMIPSolve` will be added to the master MIP prior to
solving. Examples of such modifications are additions of linearizations
and cuts that eliminate integer solutions.

.. code-block:: aimms

    MasterMIPSolve 

Arguments
---------

    *None*

Return Value
------------

    ``MasterMIPSolve()`` has no return value.
