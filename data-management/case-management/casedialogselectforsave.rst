.. aimms:procedure:: CaseDialogSelectForSave(url, contentType)

.. _CaseDialogSelectForSave:

CaseDialogSelectForSave
=======================

The procedure :aimms:func:`CaseDialogSelectForSave` shows the case file selection
dialog box. This dialog box allows the user to select an existing or a
new case file. If the selected file already exists, an overwrite
confirmation dialog box is displayed. The procedure only results in the
url of the selected case file, it does not actually create the file or
replace the existing contents. If the predefined set
``AllCaseFileContentTypes`` contains multiple elements, then the dialog
box also allows the user to select the specific contents that he wants
to save.

.. code-block:: aimms

    CaseDialogSelectForSave(
        url,          ! (input/output) a scalar string parameter
        contentType   ! (input/output) an element in AllCaseFileContentTypes
        )

Arguments
---------

    *url*
        A string representing the case file to be saved. On entry, the string is
        used to initialize the dialog box to the correct folder location. On
        return, the string will contain the reference to the selected case file.

    *contentType*
        An element parameter in ``AllCaseFileContentTypes``. On return, this
        element parameter will contain the element that the user selected.

Return Value
------------

    The procedure returns 1 if the user selected an existing or new url, and
    0 if the user cancelled the dialog box.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Disk_files_and_folders``.

    -  This function returns 0 if the IDE is not loaded, for example when
       running the component version of AIMMS, or when running with the
       command line option ``--as-server``.

.. seealso::

    The procedures :aimms:func:`CaseDialogSelectForLoad`, :aimms:func:`CaseFileSave`
