.. aimms:function:: MasterMIPDeleteIntegerEliminationCut(n)

.. _MasterMIPDeleteIntegerEliminationCut:

MasterMIPDeleteIntegerEliminationCut
====================================

The procedure :aimms:func:`MasterMIPDeleteIntegerEliminationCut` deletes a set of
integer solution elimination cuts and variables that was previously
added by the ``MasterMIPEliminateIntegerSolution`` procedure.

.. code-block:: aimms

    MasterMIPDeleteIntegerEliminationCut(
         n       ! (input) integer scalar value
         )

Arguments
---------

    *n*
        The cut counter for the set of cuts and variables that has to be
        deleted. It was returned by ``MasterMIPEliminateIntegerSolution`` when
        these cuts and variables were added.

Return Value
------------

    :aimms:func:`MasterMIPDeleteIntegerEliminationCut` has no return value.
