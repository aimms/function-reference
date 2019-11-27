.. aimms:procedure:: FileSelect(filename[, directory][, extension][, title])

.. _FileSelect:

FileSelect
==========

With the procedure :aimms:func:`FileSelect` you can let the user select an
existing file name using Windows' standard file selection dialog box.
Usually you use this procedure to select some input file (i.e. a file
for reading), because other than ``FileSelectNew``, this procedure only
allows the user to select existing files.

.. code-block:: aimms

    FileSelect(
            filename,        ! (input/output) scalar string identifier
            [directory,]     ! (optional) scalar string expression
            [extension,]     ! (optional) scalar string expression
            [title]          ! (optional) scalar string expression
            )

Arguments
---------

    *filename*
        A scalar string identifier holding the file name that the user selected.
        If on entry this strings represents a valid file name, then this file
        name is used to initialize the dialog box.

    *directory (optional)*
        A scalar string representing an existing directory. The dialog box will
        initially only show the files that are located in this directory. If
        this argument is omitted, then the current project directory will be
        used.

    *extension (optional)*
        A scalar string representing a file extension. The dialog box will
        initially only show those files that match this extension. If this
        argument is omitted, then all files are shown.

    *title (optional)*
        A scalar string that is used as the title of the selection dialog box.
        If this argument is omitted, then a default title is used.

Return Value
------------

    The procedure returns 1 if the user actually has selected a file. If
    some error occurs or if the user presses the **Cancel** button, the
    procedure returns 0.

.. note::

    If :aimms:func:`FileSelect` returns 0, then the first argument may not contain a
    valid file name. So you must always check the return value, and, if it
    is 0, either abort the current procedure or continue with some default
    file name.

.. seealso::

    The procedure :aimms:func:`FileSelectNew`.
