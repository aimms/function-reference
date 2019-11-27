.. aimms:procedure:: CaseSelect(case[, title])

.. _CaseSelect:

CaseSelect
==========

The procedure :aimms:func:`CaseSelect` shows a dialog box in which the user can
select an existing case.

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
    presses **Cancel**, then the procedure returns 0.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

    -  If the option ``Data_Management_style`` is set to
       ``disk_files_and_folders``, please use the function :aimms:func:`CaseDialogSelectForLoad` or
       :aimms:func:`CaseDialogSelectForSave` instead.

.. seealso::

    The procedure :aimms:func:`CaseSelectNew`.
