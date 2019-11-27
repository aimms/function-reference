.. aimms:procedure:: DirectoryCopy(source, destination[, confirm])

.. _DirectoryCopy:

DirectoryCopy
=============

The procedure :aimms:func:`DirectoryCopy` copies one or more directories to a new
or other directory.

.. code-block:: aimms

    DirectoryCopy(
            source,       ! (input) scalar string expression
            destination,  ! (input) scalar string expression
            [confirm]     ! (optional) 0 or 1
            )

Arguments
---------

    *source*
        A scalar string expression representing the directories(s) you want to
        copy. The string may contain wild-card characters such as '\*' and '?',
        allowing you to copy a whole group of directories at once.

    *destination*
        A scalar string expression representing the destination directory.

    *confirm (optional)*
        An integer value that indicates whether you want to let the user confirm
        any copy operation that would overwrite existing files. If this argument
        is omitted, then the default behavior is that files are overwritten
        without any notice.

Return Value
------------

    The procedure returns 1 on success. If it fails, then it returns 0, and
    the pre-defined identifier :aimms:set:`CurrentErrorMessage` will contain a proper error
    message.

.. note::

    If the destination name does not exist, AIMMS will create a directory
    with the specified name with the same contents as the source directory.
    If the destination directory does already exists as a directory, AIMMS
    will copy the contents of the source directory into a directory with the
    same name as the source directory contained in the destination
    directory.

.. seealso::

    The procedures :aimms:func:`DirectoryMove`, :aimms:func:`FileCopy`, :aimms:func:`DirectoryExists`.
