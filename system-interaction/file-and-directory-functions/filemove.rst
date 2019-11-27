.. aimms:procedure:: FileMove(source, destination[, confirm])

.. _FileMove:

FileMove
========

The procedure :aimms:func:`FileMove` moves one or more files to either a new name
(a rename) or to another directory.

.. code-block:: aimms

    FileMove(
            source,       ! (input) scalar string expression
            destination,  ! (input) scalar string expression
            [confirm]     ! (optional) 0 or 1
            )

Arguments
---------

    *source*
        A scalar string expression representing the file(s) you want to move.
        The string may contain wild-card characters such as '\*' and '?',
        allowing you to move a whole group of files at once.

    *destination*
        A scalar string expression representing the destination file name or
        destination directory.

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

.. seealso::

    The procedures :aimms:func:`FileCopy`, :aimms:func:`DirectoryMove`, :aimms:func:`FileExists`.
