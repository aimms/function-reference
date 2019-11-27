.. aimms:procedure:: CaseFileSetCurrent(url)

.. _CaseFileSetCurrent:

CaseFileSetCurrent
==================

The procedure :aimms:func:`CaseFileSetCurrent` sets the predefined element
parameter :aimms:set:`CurrentCase` and, as a result, updates the corresponding field in
the status bar of the IDE.

.. code-block:: aimms

    CaseFileSetCurrent(
        url      ! (input) a scalar string expression
        )

Arguments
---------

    *url*
        A string referencing the url of the case file that should be loaded.
        This url can point to a file on your local file system, or to a network
        location. If you specify the empty string, the element parameter
        ``CurrentCase`` will be emptied.

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
