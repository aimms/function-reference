.. aimms:procedure:: FileTime(filename, file\_time)

.. _FileTime:

FileTime
========

The procedure :aimms:func:`FileTime` retrieves the last modification time of an
existing file.

.. code-block:: aimms

    FileTime(
            filename,     ! (input) scalar string expression
            file_time     ! (output) scalar string identifier
            )

Arguments
---------

    *filename*
        A scalar string expression representing an existing file name.

    *file\_time*
        A scalar string identifier to hold the file modification time of the
        specified file. This time is represented using AIMMS' standard date and
        time format: "YYYY-MM-DD hh:mm:ss"

Return Value
------------

    The procedure returns 1 on success. If it failed to retrieve the file
    time, then it returns 0 and the pre-defined identifier :aimms:set:`CurrentErrorMessage` will
    contain a proper error message.

.. seealso::

    The procedure :aimms:func:`FileExists`.
