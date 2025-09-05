.. aimms:procedure:: CaseFileSectionExists(url, sectionName)

.. _CaseFileSectionExists:

CaseFileSectionExists
=====================

The function :aimms:func:`CaseFileSectionExists` returns whether a user section
exists in a given case file.

.. code-block:: aimms

    CaseFileSectionExists(
        url,                          ! (input) a scalar string expression
        sectionName                   ! (input) a scalar string expression
        )

Arguments
---------

    *url*
        A string referencing the url an existing case file. This url can point
        to a file on your local file system, or to a network location.

    *sectionName*
        The name of the user section. Any leading or trailing spaces in the name
        are ignored, and an empty string is not allowed. The length of the name
        is limited to 27 characters.

Return Value
------------

    The procedure returns 1 if the section exists or 0 if the section does
    not exist. If any other error occurs, the procedure returns :math:`-1`
    and ``CurrentErrorMessage`` will contain a proper error message.

    .. note::

        -   This function is only applicable if the project option
            ``Data_Management_style`` is set to ``Disk_files_and_folders``.

        -   If your application is linked to the AIMMS PRO server, the url can
            also point to a case file stored at the server.

.. seealso::

    - The functions :aimms:func:`CaseFileSectionSave`, :aimms:func:`CaseFileSectionLoad`, :aimms:func:`CaseFileSectionMerge`, :aimms:func:`CaseFileSectionRemove`.
