.. aimms:procedure:: CaseFileSectionLoad(url, sectionName[, keepUnreferencedRuntimeLibs])

.. _CaseFileSectionLoad:

CaseFileSectionLoad
===================

With the function :aimms:func:`CaseFileSectionLoad`, you can load the data of a
user section in an existing case file into memory. All identifiers
stored in the case file section will replace the corresponding data of
the identifier in the current model.

.. code-block:: aimms

    CaseFileSectionLoad(
        url,                          ! (input) a scalar string expression
        sectionName,                  ! (input) a scalar string expression
        [keepUnreferencedRuntimeLibs] ! (optional) 0 or 1
    )

Arguments
---------

    *url*
        A string referencing the url of the case file that should be loaded.
        This url can point to a file on your local file system, or to a network
        location.

    *sectionName*
        The name of the user section from which you want to load the data. Any
        leading or trailing spaces in the name are ignored, and an empty string
        is not allowed. The length of the name is limited to 27 characters.

    *keepUnreferencedRuntimeLibs (optional)*
        An integer value indicating whether or not any runtime libraries in
        existence before the data is loaded, but not referenced in the case
        file, should be kept in memory or destroyed during the data load. The
        default is 0, indicating that the runtime libraries not referenced in
        the case file should be destroyed during the case load.

Return Value
------------

    The procedure returns 1 on success. If any other error occur, the
    procedure returns 0 and ``CurrentErrorMessage`` will contain a proper
    error message.

    .. note::

        -   This function is only applicable if the project option
            ``Data_Management_style`` is set to ``Disk_files_and_folders``.

        -   If your application is linked to the AIMMS PRO server, the url can
            also point to a case file stored at the server.

.. seealso::

    - The functions :aimms:func:`CaseFileLoad`, :aimms:func:`CaseFileSectionSave`, :aimms:func:`CaseFileSectionMerge`, :aimms:func:`CaseFileSectionExists`, :aimms:func:`CaseFileSectionRemove`.
