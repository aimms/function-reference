.. aimms:procedure:: DirectoryCreate(directoryname)

.. _DirectoryCreate:

DirectoryCreate
===============

The procedure :aimms:func:`DirectoryCreate` creates a new directory on your disk.

.. code-block:: aimms

    DirectoryCreate(
            directoryname      ! (input) scalar string expression
            )

Arguments
---------

    *directoryname*
        A scalar string expression representing the new directory name. If the
        name does not contain a full path, then the it is assumed to be relative
        to the current project directory.

Return Value
------------

    The procedure returns 1 if the directory is created successfully. If it
    fails, then it returns 0, and the pre-defined identifier :aimms:set:`CurrentErrorMessage` will
    contain a proper error message.

.. note::

    If the new directory path contains references to non-existing
    directories, then the procedure tries to create each of these
    directories.

.. seealso::

    The procedures :aimms:func:`DirectoryExists`, :aimms:func:`DirectoryDelete`.
