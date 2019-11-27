.. aimms:procedure:: CaseSelectNew(case[, title])

.. _CaseSelectNew:

CaseSelectNew
=============

The procedure :aimms:func:`CaseSelectNew` shows a dialog box in which the user can
select a new case.

.. code-block:: aimms

    CaseSelect(
            case,       ! (output) element parameter in AllCases
            [title]     ! (optional) string expression
            )

Arguments
---------

    *case*
        An element parameter in ``AllCases``. On return the case will refer to
        the selected case.

    *title (optional)*
        A string expression that is used as the title for the dialog box. If
        this argument is omitted, then a default title is used.

Return Value
------------

    The procedure returns 1 if the user did select a case. If the user
    pressed **Cancel**, then the procedure returns 0.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

    -  If via this procedure the user creates a new case (i.e. a new case
       node in the data management tree), then this case does not yet
       contain any data. The case will only contain data after you
       explicitly save data to the case.

    -  If the option ``Data_Management_style`` is set to
       ``disk_files_and_folders``, please use the function :aimms:func:`CaseDialogSelectForLoad` or
       :aimms:func:`CaseDialogSelectForSave` instead.

.. seealso::

    The procedures :aimms:func:`CaseSelect`, :aimms:func:`CaseSetCurrent`, :aimms:func:`CaseSave`.
