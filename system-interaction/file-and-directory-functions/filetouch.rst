.. aimms:procedure:: FileTouch(filename, newtime)

.. _FileTouch:

FileTouch
=========

The procedure :aimms:func:`FileTouch` changes the modification time of a file.

.. code-block:: aimms

    FileTouch(
            filename,     ! (input) scalar string expression
            [newtime]     ! (optional) scalar string expression
            )

Arguments
---------

    *filename*
        A scalar string expression representing an existing file name.

    *newtime*
        This time is represented using AIMMS' standard date and time format:
        "YYYY-MM-DD hh:mm:ss". If omitted the modification time of the file is
        set to the current time.

Return Value
------------

    The procedure returns 1 on success. If it failed to set the file time,
    then it returns 0 and the pre-defined identifier :aimms:set:`CurrentErrorMessage` will contain
    a proper error message.
