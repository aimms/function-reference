.. aimms:procedure:: CaseFileGetContentType(url, contents)

.. _CaseFileGetContentType:

CaseFileGetContentType
======================

The procedure :aimms:func:`CaseFileGetContentType` retrieves the subset reference
that was used when saving the case file.

.. code-block:: aimms

    CaseFileGetContentType(
             url,             ! (input) a scalar string expression
             contents         ! (output) a scalar element parameter into the
                              !          set AllSubsetsOfAllIdentifiers
        )

Arguments
---------

    *url*
        A string referencing the url of an existing case file from which you
        want to retrieve the contents information. This url can point to a file
        on your local file system, or to a network location.

    *contents*
        An element parameter in ``AllSubsetsOfAllIdentifiers``. On return it
        holds the reference to the subset that was used when saving the case
        file.

Return Value
------------

    The procedure returns 1 on success. If any other error occurs, the
    procedure returns 0 and ``CurrentErrorMessage`` will contain a proper
    error message.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Disk_files_and_folders``.

    -  If your application is linked to the AIMMS PRO server, the url can
       also point to a case file stored at the server.

.. seealso::

    The function :aimms:func:`CaseFileSave`.
