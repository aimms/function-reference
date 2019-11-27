.. aimms:procedure:: CaseSaveAll([confirm])

.. _CaseSaveAll:

CaseSaveAll
===========

With the procedure :aimms:func:`CaseSaveAll` you can save (via a single call) the
current case and all active datasets that need saving.

.. code-block:: aimms

    CaseSaveAll(
            [confirm]      ! (optional) integer value (0, 1 or 2)
            )

Arguments
---------

    *confirm (optional)*
        If 0, then cases and datasets are saved without confirmation. If 2, then
        AIMMS will display a dialog box for the cases and datasets that are
        about to be saved and ask for confirmation. If 1 (default), then AIMMS
        will use the properties of the case type and data categories to
        determine whether a confirmation dialog box should be displayed.

Return Value
------------

    The procedure returns 1 if the user chooses not to save the data or if
    the user chooses to save the data and the save was executed
    successfully. It returns 0 if the user cancelled any of the dialog
    boxes. If any other error occurs then the procedure returns :math:`-1`
    and ``CurrentErrorMessage`` will contain a proper error message.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

    -  This function always returns 1 if the IDE is not loaded, for example
       when running the component version of AIMMS or when running with the
       command line option ``--as-server``.

    -  If the option ``Data_Management_style`` is set to
       ``disk_files_and_folders``, please use the function :aimms:func:`CaseDialogConfirmAndSave` and
       :aimms:func:`CaseCommandSave` instead.

.. seealso::

    The procedures :aimms:func:`CaseSave`, :aimms:func:`DatasetSave`.
