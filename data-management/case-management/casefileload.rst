.. aimms:procedure:: CaseFileLoad(url[, keepUnreferencedRuntimeLibs])

.. _CaseFileLoad:

CaseFileLoad
============

With the function :aimms:func:`CaseFileLoad`, you can load the data of an existing
case file into memory. All identifiers read from the case file will
replace the corresponding data of the identifier in the current model.

.. code-block:: aimms

    CaseFileLoad(
        url,                          ! (input) a scalar string expression
        [keepUnreferencedRuntimeLibs] ! (optional) 0 or 1
        )

Arguments
---------

    *url*
        A string referencing the url of the case file that should be loaded.
        This url can point to a file on your local file system, or to a network
        location.

    *keepUnreferencedRuntimeLibs (optional)*
        An integer value indicating whether or not any runtime libraries in
        existence before the data is loaded, but not referenced in the case
        file, should be kept in memory or destroyed during the data load. The
        default is 0, indicating that the runtime libraries not referenced in
        the case file should be destroyed during the case load.

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

    -  Data stored in user sections of the case file, will not be read by
       :aimms:func:`CaseFileLoad`.

Example
----------

Given two cases ``data/caseA.data`` and ``data/caseB.data`` containing:

+-----------+-----------------+--------------+------------------------+
|           | caseA           | caseB        | caseB merged to caseA  |
+===========+=================+==============+========================+
| p_num     | 77              | 88           | 88                     |
+-----------+-----------------+--------------+------------------------+
| p_dat(a)  | 11              | 11           | 11                     |
+-----------+-----------------+--------------+------------------------+
| p_dat(b)  | 22              | 20           | 20                     |
+-----------+-----------------+--------------+------------------------+
| p_dat(c)  | 33              |              | 33                     |
+-----------+-----------------+--------------+------------------------+
| p_dat(d)  |                 | 44           | 44                     |
+-----------+-----------------+--------------+------------------------+

Then the code:

.. code-block:: aimms
    :linenos:

    CaseFileLoad(
        url                         :  "data/caseA.data", 
        keepUnreferencedRuntimeLibs :  0);
    block where single_column_display := 1 ;
        display p_num, p_dat ;
    endblock ;

produces in the listing file:

.. code-block:: aimms

    chapterData::sectionCaseManagement::p_num := 77 ;


    chapterData::sectionCaseManagement::p_dat := data 
    { a : 11,
      b : 22,
      c : 33 } ;



.. seealso::

    The procedure :aimms:func:`CaseFileMerge`.
