.. aimms:function:: CaseFileSectionRemove(url, sectionName)

.. _CaseFileSectionRemove:

CaseFileSectionRemove
=====================

The function :aimms:func:`CaseFileSectionRemove` can remove a user section from a
specified existing case file.

.. code-block:: aimms

    CaseFileSectionRemove(
        url,                          ! (input) a scalar string expression
        sectionName                   ! (input) a scalar string expression
    )

Arguments
---------

    *url*
        A string referencing the url of an existing case file. This url can
        point to a file on your local file system, or to a network location.

    *sectionName*
        The name of the user section to remove. Any leading or trailing spaces
        in the name are ignored, and an empty string is not allowed. The length
        of the name is limited to 27 characters.

Return Value
------------

    The function returns 1 if the section was successfully removed or did
    not exist at all. It returns 0 if the section exists, but could not be
    removed. In case of any other error, the function returns :math:`-1` and
    ``CurrentErrorMessage`` will contain a proper error message.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Disk_files_and_folders``.

    -  If your application is linked to the AIMMS PRO server, the url can
       also point to a case file stored at the server.

.. seealso::

    The functions :aimms:func:`CaseFileSectionSave`, :aimms:func:`CaseFileSectionLoad`, :aimms:func:`CaseFileSectionMerge`, :aimms:func:`CaseFileSectionExists`
