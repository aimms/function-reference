.. aimms:procedure:: CaseLoadIntoCurrent(case[, dialog][, keepUnreferencedRuntimeLibs])

.. _CaseLoadIntoCurrent:

CaseLoadIntoCurrent
===================

The procedure :aimms:func:`CaseLoadIntoCurrent` loads the data of an existing case
into the current case. You can use it to load either a case that is
passed as argument to the procedure, or a case that the user can select
via a dialog box. The data that is stored in the case will overwrite any
data of the currently active case, and thus this current case is set to
have changed data.

.. code-block:: aimms

    CaseLoadIntoCurrent(
        case,   ! (input/output) An element parameter into AllCases
        [dialog]                      ! (optional) 0 or 1
        [keepUnreferencedRuntimeLibs  ! (optional) 0 or 1
    )

Arguments
---------

    *case*
        An element parameter into the pre-defined set ``AllCases``. If the
        argument *dialog* is set to 0, then no dialog is shown and the case to
        which the element parameter currently refers is loaded. If the argument
        *dialog* is set to 1, then the value of the element parameter is used to
        initialize the dialog box. The case that the user has selected and is
        loaded successfully is returned through this argument.

    *dialog (optional)*
        An integer value indicating whether or not the user gets a dialog box in
        which he can select the case to load. The default value is 1, thus if
        this argument is omitted the dialog box will be shown.

    *keepUnreferencedRuntimeLibs (optional)*
        An integer value indicating whether or not any runtime libraries in
        existence before the case is loaded, but not referenced in the case,
        should be kept in memory or destroyed during the case load. The default
        is 0 indicating that the runtime libraries not referenced in the case
        should be destroyed during the case load.

Return Value
------------

    The procedure returns 1 on success. If the user cancelled the operation,
    then the procedure returns 0. If any other error occurs then the
    procedure returns :math:`-1` and :aimms:set:`CurrentErrorMessage` will contain a proper error
    message.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

    -  If the option ``Data_Management_style`` is set to
       ``disk_files_and_folders``, please use the function :aimms:func:`CaseCommandLoadIntoActive`
       instead.

.. seealso::

    The procedures :aimms:func:`CaseLoadCurrent`, :aimms:func:`CaseMerge`, :aimms:func:`CaseSave`, :aimms:func:`CaseSetChangedStatus`.
