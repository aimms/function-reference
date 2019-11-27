.. aimms:procedure:: PivotTableDeleteState(statename, statesource)

.. _PivotTableDeleteState:

PivotTableDeleteState
=====================

With the procedure :aimms:func:`PivotTableDeleteState` you can delete a specific
state in either the Developer or End User state file.

.. code-block:: aimms

    PivotTableDeleteState(
                statename,  ! (input) scalar string expression
                statesource ! (input) scalar string expression
            )

Arguments
---------

    *statename*
        A string expression representing the name of the state to be deleted.

    *statesource*
        A string expression representing the type of state to be deleted.
        Possible values are:

        -  DeveloperState: Delete the specified state from the *developer* state
           file.

        -  UserState: Delete the specified state from the *user* state file.

        -  Both: Delete the state from both the *developer* and *user* state
           file

Return Value
------------

    The procedure returns 1 on success. If it fails to delete the specified
    state, then the return value is 0 and :aimms:set:`CurrentErrorMessage` will contain a proper
    error message.

.. note::

    -  When running in End User mode, you cannot delete states from the
       developer state file.

.. seealso::

    -  The Pivot Table example that comes with the AIMMS installation
       includes a library that uses this new function. It includes a
       right-mouse menu that can be assigned to a Pivot Table, after which
       the user can save, load, or delete states for that Pivot Table. You
       can include this library in your own project as well.

    -  The functions :aimms:func:`PivotTableReloadState`, :aimms:func:`PivotTableSaveState`.
