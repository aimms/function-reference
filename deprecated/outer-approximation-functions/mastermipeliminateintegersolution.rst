.. aimms:function:: MasterMIPEliminateIntegerSolution(n)

.. _MasterMIPEliminateIntegerSolution:

MasterMIPEliminateIntegerSolution
=================================

The procedure :aimms:func:`MasterMIPEliminateIntegerSolution` adds a set of cuts
and variables to the master MIP model instance which eliminates the
current integer solution inside the AIMMS Outer Approximation solver
interface.

.. code-block:: aimms

    MasterMIPEliminateIntegerSolution(
         n       ! (output) integer scalar parameter
         )

Arguments
---------

    *n*
        The updated cut counter.

Return Value
------------

    :aimms:func:`MasterMIPEliminateIntegerSolution` has no return value.

.. note::

    To eliminate the current integer solution, 3 variables (2 continuous, 1
    binary) and 3 constraints are added for each integer variable whose
    level value is between its bounds. Also one main cut constraint is
    added. In case all integer variables are binary, only this main cut
    constraint is added.
