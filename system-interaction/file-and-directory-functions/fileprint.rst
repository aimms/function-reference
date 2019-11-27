.. aimms:procedure:: FilePrint(filename[, encoding])

.. _FilePrint:

FilePrint
=========

The procedure :aimms:func:`FilePrint` prints a specific text file using the
currently selected printer.

.. code-block:: aimms

    FilePrint(
            filename,     ! (input) scalar string expression
            encoding      ! (optional) scalar element expression
            )

Arguments
---------

    *filename*
        A scalar string expression representing the text file that you want to
        print.

    *encoding (optional)*
        A scalar element expression that results in an element of :aimms:set:`AllCharacterEncodings`. If
        this argument is not specified, the value of the option
        ``default_input_character_encoding`` is used.

Return Value
------------

    The procedure returns 1 on success, and 0 if it could not print the
    file.

.. note::

    The file is printed using the paper and font settings that are specified
    in the **Text Printing** dialog box, which is accessible from the
    ``Settings`` menu.

.. seealso::

    The procedure :aimms:func:`FileEdit`.
