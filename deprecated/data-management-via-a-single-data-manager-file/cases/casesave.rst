.. aimms:procedure:: CaseSave([confirm])

.. _CaseSave:

CaseSave
========

The procedure :aimms:func:`CaseSave` saves the data to the current case. If there
is no current case, then the procedure behaves exactly as the
``CaseSaveAs`` procedure. If the case has active references to datasets
that contain changed data, then these datasets are saved as well.

.. code-block:: aimms

    CaseSave(
            [confirm]       ! (optional) 0, 1 or 2
            )

Arguments
---------

    *confirm (optional)*
        An integer to indicate whether or not the procedure should ask for
        confirmation before overwriting the existing case. If 0, then no
        confirmation dialog box is shown. If 1 (default), then whether the
        confirmation dialog box is shown depends on the case type properties. If
        2, then always a confirmation dialog box is shown.

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
       ``disk_files_and_folders``, please use the function :aimms:func:`CaseCommandSave` or
       :aimms:func:`CaseFileSave` instead.

.. seealso::

    The procedures :aimms:func:`CaseSaveAs`, :aimms:func:`CaseSaveAll`, :aimms:func:`CaseLoadCurrent`, :aimms:func:`CaseGetChangedStatus`.
