.. aimms:procedure:: FileGetSize(filename, fileSize)

.. _FileGetSize:

FileGetSize
===========

The procedure :aimms:func:`FileGetSize` retrieves the size on disk of an existing
file.

.. code-block:: aimms

    FileGetSize(
            filename,     ! (input) scalar string expression
            fileSize      ! (output) scalar numerical identifier
            )

Arguments
---------

    *filename*
        A scalar string expression representing an existing file name.

    *fileSize*
        A scalar identifier to hold the size of the file, or -1 if the size
        could not be retrieved.

Return Value
------------

    The procedure returns 1 on success. If it failed to retrieve the file
    size, then it returns 0 and the pre-defined identifier :aimms:set:`CurrentErrorMessage` will
    contain a proper error message.

.. seealso::

    The procedure :aimms:func:`FileExists`.
