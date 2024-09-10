.. aimms:procedure:: CaseFileSave(url, contents)

.. _CaseFileSave:

CaseFileSave
============

The function :aimms:func:`CaseFileSave` saves a specific subset of identifiers to
a case file. If the file already exists, it is completely overwritten.

.. code-block:: aimms

    CaseFileSave(
        url,                          ! (input) a scalar string expression
        contents                      ! (input) a subset of AllIdentifiers
        )

Arguments
---------
 
    *url*
        A string referencing the url of the case file in which you want to save
        the data. This url can point to a file on your local file system, or to
        a network location.

    *contents*
        A subset of :aimms:set:`AllIdentifiers` containing all the identifiers that must
        be saved. Preferrably, this set is an element of :aimms:set:`AllCaseFileContentTypes` such that,
        when reading back the case file, the content type can be determined
        correctly.

Return Value
------------

    The procedure returns 1 on success. If any other error occurs, the
    procedure returns 0 and ``CurrentErrorMessage`` will contain a proper
    error message.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Disk_files_and_folders``.

    -  This function will only save the data to the specified file. It does
       not change the value of ``CurrentCase`` or
       ``CurrentCaseFileContentType``, nor does it mark the current data as
       being saved.

    -  If your application is linked to the AIMMS PRO server, the url can
       also point to a case file stored at the server.

    -  When you save using :aimms:func:`CaseFileSave` to an existing ``.data`` file
       with sections, the sections are removed.


Example
----------

The code:

.. code-block:: aimms
    :linenos:

	read from file "caseFileInputData/caseC.txt" ;
	CaseFileSave( "data/caseC.data", s_CaseManagementData );

Reads data from a text file, and then saves it in binary format to ``data/caseC.data``.

.. seealso::

    The functions :aimms:set:`CaseFileSectionSave` and :aimms:set:`CaseFileLoad`
