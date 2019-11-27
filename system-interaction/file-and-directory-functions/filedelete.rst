.. aimms:procedure:: FileDelete(filename, delete\_readonly\_files)

.. _FileDelete:

FileDelete
==========

The procedure :aimms:func:`FileDelete` deletes one or more files from your disk.

.. code-block:: aimms

    FileDelete(
            filename,                ! (input) scalar string expression
            [delete_readonly_files]  ! (optional, default 0) scalar expression
            )

Arguments
---------

    *filename*
        A scalar string expression representing the file(s) you want to delete.
        The string may contain wild-card characters such as '\*' and '?',
        allowing you to delete a whole group of files at once.

    *delete\_readonly\_files*
        A scalar expression indicating whether read-only files must be deleted
        without further notice (value :math:`{}\neq{}` 0), or whether the
        procedure should fail on a read-only file (value 0).

Return Value
------------

    The procedure returns 1 on success. If it fails, then it returns 0, and
    the pre-defined identifier :aimms:set:`CurrentErrorMessage` will contain a proper error
    message.

.. seealso::

    The procedures :aimms:func:`FileExists`, :aimms:func:`DirectoryDelete`.
