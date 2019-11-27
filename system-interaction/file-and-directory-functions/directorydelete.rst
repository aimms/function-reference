.. aimms:procedure:: DirectoryDelete(directory, delete\_readonly\_files)

.. _DirectoryDelete:

DirectoryDelete
===============

The procedure :aimms:func:`DirectoryDelete` deletes a directory from your disk. If
this directory contains files, then these files are deleted as well.

.. code-block:: aimms

    DirectoryDelete(
            directory,                ! (input) scalar string expression
            [delete_readonly_files]   ! (optional, default 0) scalar expression
            )

Arguments
---------

    *directory*
        A scalar string expression representing the directory you want to
        delete.

    *delete\_readonly\_files*
        A scalar expression indicating whether read-only files must be deleted
        without further notice (value :math:`{}\neq{}` 0), or whether the
        procedure should fail on read-only files (value 0).

Return Value
------------

    The procedure returns 1 on success. If it fails, then it returns 0, and
    the pre-defined identifier :aimms:set:`CurrentErrorMessage` will contain a proper error
    message.

.. seealso::

    The procedures :aimms:func:`DirectoryExists`, :aimms:func:`FileDelete`.
