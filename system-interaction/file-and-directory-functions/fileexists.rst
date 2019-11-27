.. aimms:procedure:: FileExists(filename)

.. _FileExists:

FileExists
==========

With the procedure :aimms:func:`FileExists` you can check whether a specific file
name currently exists.

.. code-block:: aimms

    FileExists(
            filename      ! (input) scalar string expression
            )

Arguments
---------

    *filename*
        A scalar string expression representing a valid file name. The file name
        may contain a partial path relative to the project directory, or a full
        path.

Return Value
------------

    The procedure returns 1 if the given file name exists, and 0 otherwise.

.. note::

    Note that if you want use some static file name in your model, then you
    have to specify two slashes behind each directory, as in
    ``"c:\\windows\\temp\\filename.dat"``

.. seealso::

    The procedure :aimms:func:`FileDelete`
