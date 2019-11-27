.. aimms:procedure:: FileEdit(filename[, find][, encoding])

.. _FileEdit:

FileEdit
========

The procedure :aimms:func:`FileEdit` opens a specific file in the internal AIMMS
text file editor. Optionally, you can set the cursor on a specific piece
of text within the file.

.. code-block:: aimms

    FileEdit(
            filename,     ! (input) scalar string expression
            find,         ! (optional) scalar string expression
            encoding      ! (optional) scalar element expression
            )

Arguments
---------

    *filename*
        A scalar string expression representing the file name that you want to
        edit.

    *find (optional)*
        A scalar string expression that is used to position the cursor over a
        specific piece of text in the file. If this argument is omitted (or if
        the specified text cannot be found), then the cursor will be positioned
        at the top of the file.

    *encoding (optional)*
        A scalar element expression that results in an element of :aimms:set:`AllCharacterEncodings`. If
        this argument is not specified, the value of the option
        ``default_input_character_encoding`` is used.

Return Value
------------

    The procedure returns 1 on success, and 0 if it could not open the file
    in the editor.

.. note::

    If you want to use another external text editor to edit a specific file,
    then you can use the procedure :aimms:func:`Execute`.

.. seealso::

    The procedures :aimms:func:`FileView`, :aimms:func:`Execute`.
