.. aimms:procedure:: CaseMerge(case[, dialog][, keepUnreferencedRuntimeLibs])

.. _CaseMerge:

CaseMerge
=========

The procedure :aimms:func:`CaseMerge` merges the data of an existing case with the
current data. You can use it to merge either a case that is passed as
argument to the procedure, or a case that the user can select via a
dialog box. Only the non-default data that is stored in the case will be
merged with the data of the currently active case. This current case is
set to have changed data.

.. code-block:: aimms

    CaseMerge(
        case,   ! (input/output) An element parameter into AllCases
        [dialog],                     ! (optional) 0 or 1
        [keepUnreferencedRuntimeLibs  ! (optional) 0 or 1
    )

Arguments
---------

    *case*
        An element parameter into the pre-defined set :aimms:set:`AllCases`. If the
        argument *dialog* is set to 0, then no dialog box is shown and the case
        to which the element parameter currently refers is merged. If the
        argument *dialog* is set to 1, then the value of the element parameter
        is used to initialize the dialog box. The case that the user has
        selected and is merged successfully is returned through this argument.

    *dialog (optional)*
        An integer value indicating whether or not the user gets a dialog box in
        which he can select the case to merge. The default value is 1, thus if
        this argument is omitted the dialog box will be shown.

    *keepUnreferencedRuntimeLibs (optional)*
        An integer value indicating whether or not any runtime libraries in
        existence before the case is merged, but not referenced in the case,
        should be kept in memory or destroyed during the case merge. The default
        is 1 indicating that the runtime libraries not referenced in the case
        will be retained during the case merge.

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
       ``disk_files_and_folders``, please use the function :aimms:func:`CaseCommandMergeIntoActive`
       instead.

.. seealso::

    The procedures :aimms:func:`CaseLoadCurrent`, :aimms:func:`CaseLoadIntoCurrent`, :aimms:func:`CaseSave`, :aimms:func:`CaseGetChangedStatus`.
