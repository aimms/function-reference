.. aimms:procedure:: CaseSaveAs(case)

.. _CaseSaveAs:

CaseSaveAs
==========

The procedure :aimms:func:`CaseSaveAs` shows a dialog box in which the user can
specify a (new) case to which the data is saved. If the case has active
references to datasets that contain changed data, then these datasets
are saved as well. When saving these datasets the procedure will simply
overwrite the current datasets, thus with :aimms:func:`CaseSaveAs` you can only
change the current case and not any of the current datasets.

.. code-block:: aimms

    CaseSaveAs(
            case        ! (output) element parameter in AllCases
            )

Arguments
---------

    *case*
        An element parameter in :aimms:set:`AllCases`. On return this parameter will
        refer to the case that the user selected.

Return Value
------------

    The procedure returns 1 if the case is saved successfully. It returns 0
    if the user canceled the save operation. If any other error occurs, then
    the procedure returns :math:`-1` and :aimms:set:`CurrentErrorMessage` will contain an error
    message.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

    -  If the option ``Data_Management_style`` is set to
       ``disk_files_and_folders``, please use the function :aimms:func:`CaseCommandSaveAs`
       instead.

.. seealso::

    The procedures :aimms:func:`CaseSave`, :aimms:func:`CaseSaveAll`, :aimms:func:`CaseLoadCurrent`, :aimms:func:`CaseGetChangedStatus`.
