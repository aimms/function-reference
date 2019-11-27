.. aimms:procedure:: FileAppend(filename, appendname)

.. _FileAppend:

FileAppend
==========

The procedure :aimms:func:`FileAppend` appends the contents of one file to the end
of another file. Both files must be text files.

.. code-block:: aimms

    FileAppend(
            filename,       ! (input) scalar string expression
            appendname      ! (input) scalar string expression
            )

Arguments
---------

    *filename*
        A scalar string expression representing the file name to which you want
        to append the contents of the second file.

    *appendname*
        A scalar string expression representing the file name that you want to
        append.

Return Value
------------

    The procedure returns 1 on success. If it fails, then it returns 0, and
    the pre-defined identifier :aimms:set:`CurrentErrorMessage` will contain a proper error
    message.

.. note::

    -  If the first file (the file to which you append) does not exist, then
       this file will be created. The contents of the appended file will
       always start on a new line in the resulting file.

    -  When appending files with different character encodings, the result
       is unpredictable.

.. seealso::

    The procedures :aimms:func:`FileCopy`, :aimms:func:`FileExists`.
