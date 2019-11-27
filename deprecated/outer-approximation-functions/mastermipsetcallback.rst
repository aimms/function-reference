.. aimms:function:: MasterMIPSetCallback(ProcedureName, Iterations)

.. _MasterMIPSetCallback:

MasterMIPSetCallback
====================

The procedure :aimms:func:`MasterMIPSetCallback` allows the user to set a callback
procedure that will be called during the solve of the master MIP. It
will be called either for every new incumbent value found by the MIP
solver or after a certain number of iterations. This is determined by
the argument ``Iterations``.

.. code-block:: aimms

    MasterMIPSetCallback(
         ProcedureName,       ! (input) scalar string expression
         Iterations           ! (input) integer scalar value
         )

Arguments
---------

    *ProcedureName*
        The name of the AIMMS procedure that will be used as callback procedure.

    *Iterations*
        If Iterations :math:`\ge` 1 then the callback procedure will be called
        after this number of iterations; else it will be called for every new
        incumbent value found by the MIP solver.

Return Value
------------

    ``MasterMIPSetCallback()`` has no return value.
