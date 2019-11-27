.. aimms:procedure:: DirectoryMove(source, destination[, confirm])

.. _DirectoryMove:

DirectoryMove
=============

The procedure :aimms:func:`DirectoryMove` moves one or more directories to either
a new name (a rename) or to another directory.

.. code-block:: aimms

    DirectoryMove(
            source,        ! (input) scalar string expression
            destination,   ! (input) scalar string expression
            confirm        ! (optional) 0 or 1
            )

Arguments
---------

    *source*
        A scalar string expression representing the file(s) you want to move.
        The string may contain wild-card characters such as '\*' and '?',
        allowing you to move a whole group of directories at once.

    *destination*
        A scalar string expression representing the destination directory.

    *confirm (optional)*
        An integer value that indicates whether or not you want to let the user
        confirm any move operation that would overwrite existing files. If this
        argument is omitted, then the default behavior is that files are
        overwritten without any notice.

Return Value
------------

    The procedure returns 1 on success. If it fails, then it returns 0, and
    the pre-defined identifier :aimms:set:`CurrentErrorMessage` will contain a proper error
    message.

.. note::

    If the destination name does not exist, AIMMS will move the source
    directory to the specified position. If the destination directory does
    already exists as a directory, AIMMS will move the source directory into
    the (existing) destination directory, retaining the original name of the
    source directory.

.. seealso::

    The procedures :aimms:func:`DirectoryCopy`, :aimms:func:`FileMove`, :aimms:func:`DirectoryExists`.
