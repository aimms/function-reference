.. aimms:procedure:: CaseFileSectionSave(url, sectionName, contents)

.. _CaseFileSectionSave:

CaseFileSectionSave
===================

Beside the main data area in a case file, which is written using the
function ``CaseFileSave``, you can store additional data in user defined
sections of the case file. To save data in a user section, you call the
function :aimms:func:`CaseFileSectionSave`.

.. code-block:: aimms

    CaseFileSectionSave(
        url,                          ! (input) a scalar string expression
        sectionName,                  ! (input) a scalar string expression
        contents                      ! (input) a subset of AllIdentifiers
    )

Arguments
---------

    *url*
        A string referencing the url of an existing case file in which you want
        to save the additional data. This url can point to a file on your local
        file system, or to a network location.

    *sectionName*
        The name of the section in which you want to write additional data. If
        the section does not yet exist, it is created. Otherwise, the existing
        contents of the section is replaced by the newly saved data. Any leading
        or trailing spaces in the name are ignored, and an empty string is not
        allowed. The length of the name is limited to 27 characters.

    *contents*
        A subset of ``AllIdentifiers`` containing all the identifiers that must
        be saved.

Return Value
------------

    The procedure returns 1 on success. If any other error occurs, the
    procedure returns :math:`0` and ``CurrentErrorMessage`` will contain a
    proper error message.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Disk_files_and_folders``.

    -  If your application is linked to the AIMMS PRO server, the url can
       also point to a case file stored at the server.

    -  You cannot use this function to create a new case file. A new case
       file can only be created using ``CaseFileSave``.

.. seealso::

    The functions :aimms:func:`CaseFileSave`, :aimms:func:`CaseFileSectionLoad`, :aimms:func:`CaseFileSectionMerge`, :aimms:func:`CaseFileSectionExists`, :aimms:func:`CaseFileSectionRemove`
