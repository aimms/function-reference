.. aimms:procedure:: PivotTableSaveState(page, tag, statesource)

.. _PivotTableSaveState:

PivotTableSaveState
===================

With the procedure :aimms:func:`PivotTableSaveState` you can save the state of a
specific pivot table to either the developer or user state file.

.. code-block:: aimms

    PivotTableSaveState(
                page,       ! (input) scalar string expression
                tag,        ! (input) scalar string expression
                statesource ! (input) scalar string expression
            )

Arguments
---------

    *page*
        A string expression representing the name of the page that contains the
        pivot table.

    *tag*
        A string expression representing the tag that identifies the pivot
        table.

    *statesource*
        A string expression representing the type of state to be saved. Possible
        values are:

        -  DeveloperState: Save the specified state to the *developer* state
           file.

        -  UserState: Save the specified state to the *user* state file.

Return Value
------------

    The procedure returns 1 on success. If it fails to save the state for
    the specified object, then the return value is 0 and :aimms:set:`CurrentErrorMessage` will
    contain a proper error message.

.. note::

    -  When running in end-user mode, it is not possible to save a
       *developer* state.

    -  You can specify a unique tag name for each page object on the
       **Misc** tab of the object properties dialog box.

    -  The name of the state is specified by the *Specific State Name*
       property on the **General** tab of the pivot table properties dialog
       box.

    -  This procedure will only save the state when the **Save Layout/State
       - By Developer** property (or **Save Layout/State - By End User**
       when running in end-user mode) on the **general** tab of the pivot
       table properties dialog box, has been set to a value other than *No*.

.. seealso::

    -  The Pivot Table example that comes with the AIMMS installation
       includes a library that uses this new function. It includes a
       right-mouse menu that can be assigned to a Pivot Table, after which
       the user can save, load, or delete states for that Pivot Table. You
       can include this library in your own project as well.

    -  The functions :aimms:func:`PivotTableDeleteState`, :aimms:func:`PivotTableReloadState`.
