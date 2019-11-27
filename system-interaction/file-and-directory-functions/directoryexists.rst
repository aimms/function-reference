.. aimms:procedure:: DirectoryExists(directoryname)

.. _DirectoryExists:

DirectoryExists
===============

With the procedure :aimms:func:`DirectoryExists` you can check whether a specific
directory name currently exists.

.. code-block:: aimms

    DirectoryExists(
            directoryname      ! (input) scalar string expression
            )

Arguments
---------

    *directoryname*
        A scalar string expression representing a valid directory name. The file
        name may contain a partial path relative to the project directory, or a
        full path.

Return Value
------------

    The procedure returns 1 if the given directory name exists, or 0
    otherwise.

.. note::

    Note that if you want use some static directory name in your model, then
    you have to specify two slashes behind each directory, as in
    ``"c:\\windows\\temp"``.

.. seealso::

    The procedure :aimms:func:`DirectoryDelete`.
