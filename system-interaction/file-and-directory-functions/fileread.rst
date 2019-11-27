.. aimms:procedure:: FileRead(filename[, encoding])

.. _FileRead:

FileRead
========

With the procedure :aimms:func:`FileRead` you can read the contents of a file into
a string parameter.

.. code-block:: aimms

    FileRead(
            filename,     ! (input) scalar string expression
            encoding      ! (optional) scalar element expression
            )

Arguments
---------

    *filename*
        A scalar string expression representing a valid file name. The file name
        may contain a partial path relative to the project directory, or a full
        path.

    *encoding (optional)*
        A scalar element expression that results in an element of :aimms:set:`AllCharacterEncodings`. If
        this argument is not specified, the value of the option
        ``default_input_character_encoding`` is used.

Return Value
------------

    The procedure returns a string containing the contents of the file.

.. note::

    -  This procedure will not automatically reread a file when its contents
       has changed. It is therefore better to use it in a procedure than in
       a parameter definition.

    -  In case the file does not exist, no error message will be returned
       and the result will be the empty string. In case there is any doubt
       the file exists it is advised to first check using the procedure
       ``FileExists``.

.. seealso::

    The procedure :aimms:procedure:`FileExists`.
