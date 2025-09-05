.. aimms:procedure:: CaseDialogSelectForLoad(url)

.. _CaseDialogSelectForLoad:

CaseDialogSelectForLoad
=======================

The procedure :aimms:func:`CaseDialogSelectForLoad` shows the case file selection
dialog box. This dialog box allows the user to select an existing case
file. The procedure only results in the url of the selected case file,
it does not actually load any data from the case file.

.. code-block:: aimms

    CaseDialogSelectForLoad(
        url       ! (input/output) a scalar string parameter
        )

Arguments
---------

    *url*
        A string representing the case file to be loaded. On entry, the string
        is used to initialize the dialog box to the correct folder location. On
        return, the string will contain the reference to the selected case file.

Return Value
------------

    The procedure returns 1 if the user selected an existing url, and 0 if
    the user cancelled the dialog box.

    .. note::

        -   This function is only applicable if the project option
            ``Data_Management_style`` is set to ``Disk_files_and_folders``.

        -   This function returns 0 if the IDE is not loaded, for example when
            running the component version of AIMMS, or when running with the
            command line option ``--as-server``.

.. seealso::

    - The procedures :aimms:func:`CaseDialogSelectForSave`, :aimms:func:`CaseFileLoad`.
