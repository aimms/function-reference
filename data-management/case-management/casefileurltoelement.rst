.. aimms:procedure:: CaseFileURLtoElement(url, caseFileElement[, checkURLExists])

.. _CaseFileURLtoElement:

CaseFileURLtoElement
====================

For each case file that has been accessed during an AIMMS session, a new
element is created in the predefined set :aimms:set:`AllCases`. The predefined
string parameter :aimms:set:`CaseFileURL` is updated accordingly. When working with a
selection of case files, for example in a multiple case view, or in
statements with the case dot notation, you should actually create a
subset of :aimms:set:`AllCases`. In that process, it may be useful to find the
corresponding element in :aimms:set:`AllCases` given the url of a case file.

.. code-block:: aimms

    CaseFileURLtoElement(
        url,                          ! (input) a scalar string expression
        caseFileElement,              ! (output) element in AllCases
        [checkURLExists]              ! (optional) 0 or 1
        )

Arguments
---------

    *url*
        A string referencing the url of a case file. This url can point to an
        existing file on your local file system, or to a network location. The
        given url does not need to be present in :aimms:set:`AllCases` a priori.

    *caseFileElement*
        On return, this element parameter is set to the element in :aimms:set:`AllCases`
        that corresponds to the given url. In other words, the following
        condition will be true: ``CaseFileUrl(caseFileElement) = url``.

    *checkURLExists (optional)*
        If this value is set to 1 then the procedure always returns 0 if the
        specified url cannot be found in the underlying file system. If set to 0
        and the underlying file does not exist, the procedure returns 1 if the
        corresponding element already existed in :aimms:set:`AllCases`. The default value
        is 0.

Return Value
------------

    The procedure returns 1 on success. If any error occurs, the procedure
    returns 0 and ``CurrentErrorMessage`` will contain a proper error
    message.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Disk_files_and_folders``.

    -  If your application is linked to the AIMMS PRO server, the url can
       also point to a case file stored at the server.

    -  If *url* exists, but is not in :aimms:set:`CaseFileURL`, an element will be added to
       :aimms:set:`AllCases`.

    -  If *url* does not exist, but there is a corresponding entry
       :aimms:set:`CaseFileURL`, the procedure returns is 1 if checkURLExists is set to 0
       and it returns 0 if checkURLExists is set to 1.

.. seealso::

    The procedures :aimms:func:`CaseDialogSelectMultiple`
