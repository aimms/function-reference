.. aimms:procedure:: CaseCommandMergeIntoActive()

.. _CaseCommandMergeIntoActive:

CaseCommandMergeIntoActive
==========================

The procedure :aimms:func:`CaseCommandMergeIntoActive` executes the same code that
is behind the menu command **Data-Load Case-Merging into Active** in the
IDE by default (please note that you can override items in the **Data**
menu using the options listed under
``Project - Data manager - Using disk files and folders - Data menu overrides``).
It shows a dialog box in which the user can select a case file, and
subsequently tries to merge the data from that file. The command changes
the data for the active case. It does not set the active case to the
selected case, though.

.. code-block:: aimms

    CaseCommandMergeIntoActive

Return Value
------------

    The procedure returns 1 on success, or 0 if the user cancelled the
    operation in one of the dialog boxes. If any other error occurs, the
    procedure returns :math:`-1` and ``CurrentErrorMessage`` will contain a
    proper error message.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Disk_files_and_folders``.

    -  This function returns 0 if the IDE is not loaded, for example when
       running the component version of AIMMS, or when running with the
       command line option ``--as-server``.

.. seealso::

    The procedures :aimms:func:`CaseCommandLoadAsActive`, :aimms:func:`CaseCommandLoadIntoActive`, :aimms:func:`CaseCommandNew`, :aimms:func:`CaseCommandSave`, :aimms:func:`CaseCommandSaveAs`
