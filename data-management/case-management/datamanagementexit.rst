.. aimms:procedure:: DataManagementExit()

.. _DataManagementExit:

DataManagementExit
==================

The function :aimms:func:`DataManagementExit` checks whether any data should be
saved according to the active data management style. If any of the data
needs saving, a dialog box is displayed, in which the user can select to
save the data, not to save the data, or to cancel the current operation.

.. code-block:: aimms

    DataManagementExit

Return Value
------------

    The procedure returns 1 if the current data does not need to be saved,
    or if the user explicitly decided to save or not to save the data. If
    the user cancelled the dialog box, or if the saving of the data resulted
    in an error, the return value is 0.

.. note::

    -  This function is applicable if the project option
       ``Data_Management_style`` is set to either ``Disk_files_and_folders``
       or ``Single_Data_Manager_file``.

    -  When the project option ``Data_Management_style`` is set to
       ``Disk_files_and_folders``, the "dirty" status can be cleared using
       the following statement:
       ``DataChangeMonitorReset(DataManagementMonitorID, AllIdentifiers)``

    -  This function is used as the default content of the procedure
       ``MainTermination``, such that upon project close the data management
       can check whether any data needs to be saved first.

    -  This function always returns 1 if the IDE is not loaded, for example
       when running the component version of AIMMS, or when running with the
       command line option ``--as-server``.

.. seealso::

    The predeclared identifier :aimms:set:`DataManagementMonitorID` and the intrinsic function
    :aimms:func:`DataChangeMonitorReset`
