.. aimms:procedure:: DirectorySelect(directoryname[, directory][, title])

.. _DirectorySelect:

DirectorySelect
===============

With the procedure :aimms:func:`DirectorySelect` you can let the user select an
existing directory using Windows' standard directory selection dialog
box.

.. code-block:: aimms

    DirectorySelect(
            directoryname,   ! (input/output) scalar string parameter
            [directory,]     ! (optional input) scalar string expression
            [title]          ! (optional input) scalar string expression
            )

Arguments
---------

    *directoryname*
        A scalar string parameter. On return this parameter will represent the
        selected directory name. If the selected directory is a sub directory
        below the current project directory, then the directory name will be
        presented using a relative path. In other cases the directory name is
        presented using a full path specification. In both cases, the returned
        directory string is terminated by a :math:`\backslash` character.

    *directory (optional)*
        A scalar string representing an existing directory. The dialog box will
        initially select this directory. If omitted, then the current project
        directory will be used.

    *title (optional)*
        A scalar string that is used as the title of the selection dialog box.
        If this argument is omitted, then a default title is used.

Return Value
------------

    The procedure returns 1 if the user did select a directory. If some
    error occurs or if the user presses the **Cancel** button, then the
    procedure returns 0.

.. note::

    If :aimms:func:`DirectorySelect` returns 0, then the first argument may not
    contain a valid directory path. So you must always check the return
    value, and, if it is 0, either abort the current procedure or continue
    with some default directory name.

.. seealso::

    The procedures :aimms:func:`FileSelect`, :aimms:func:`DirectoryGetCurrent`.
