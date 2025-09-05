.. aimms:procedure:: CaseCommandNew()

.. _CaseCommandNew:

CaseCommandNew
==============

The procedure :aimms:func:`CaseCommandNew` executes the same code that is behind
the menu command **Data-New Case** in the IDE by default (please note
that you can override items in the **Data** menu using the options
listed under
``Project - Data manager - Using disk files and folders - Data menu overrides``).
If the data of the currently active case needs to be saved, a
confirmation dialog box will be displayed first. Afterwards, the active
case will not refer to any case file.

.. code-block:: aimms

    CaseCommandNew

Return Value
------------

    The procedure returns 1 on success, or 0 if the user cancelled the
    operation in one of the dialog boxes. If any other error occurs, the
    procedure returns :math:`-1` and ``CurrentErrorMessage`` will contain a
    proper error message.

    .. note::

        -   This function is only applicable if the project option
            ``Data_Management_style`` is set to ``Disk_files_and_folders``.

        -   This function returns 0 if the IDE is not loaded, for example when
            running the component version of AIMMS, or when running with the
            command line option ``--as-server``.

        -   An alternative for calling :aimms:func:`CaseCommandNew` is calling :aimms:func:`CaseFileSetCurrent`
            with an empty string. The latter will not check whether the current
            case should be saved first.

.. seealso::

    - The procedures :aimms:func:`CaseCommandLoadAsActive`, :aimms:func:`CaseCommandLoadIntoActive`, :aimms:func:`CaseCommandMergeIntoActive`, :aimms:func:`CaseCommandSave`, :aimms:func:`CaseCommandSaveAs`.
