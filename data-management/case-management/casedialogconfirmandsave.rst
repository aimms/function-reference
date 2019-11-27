.. aimms:procedure:: CaseDialogConfirmAndSave()

.. _CaseDialogConfirmAndSave:

CaseDialogConfirmAndSave
========================

The procedure :aimms:func:`CaseDialogConfirmAndSave` shows and handles the
standard confirmation dialog box, in which the user is asked whether he
wants to save the currently active data before continuing.

.. code-block:: aimms

    CaseDialogConfirmAndSave

Return Value
------------

    The procedure returns 1 if the user chooses not to save the data, or if
    the user chooses to save the data and the save was executed
    successfully. It returns 0 if the user cancelled any of the dialog
    boxes. If any other error occurs, the procedure returns :math:`-1` and
    ``CurrentErrorMessage`` will contain a proper error message.

.. note::

    -  This procedure is only applicable if the project option
       ``Data_Management_style`` is set to ``Disk_files_and_folders``.

    -  This procedure returns 0 if the IDE is not loaded, for example when
       running the component version of AIMMS, or when running with the
       command line option ``--as-server``.

    -  This procedure does not check whether the data needs to be saved;
       that check should be made by the calling code, prior to calling this
       procedure.

    -  If the user confirms to save the data, the function
       ``CaseDialogSave`` is called. If no active case file exists, this
       implies that the ``CaseDialogSaveAs`` is called instead.

.. seealso::

    The procedure :aimms:func:`DataChangeMonitorAnyChange`
