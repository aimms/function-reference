.. aimms:procedure:: DirectoryGetSubdirectories(directory, filter, subdirectorynames, recursive, attributeFilter)

.. _DirectoryGetSubdirectories:

DirectoryGetSubdirectories
==========================

The procedure :aimms:func:`DirectoryGetSubdirectories` creates a list of
subdirectory names present in a directory.

.. code-block:: aimms

    DirectoryGetSubdirectories(
            directory,         ! (input) scalar string expression
            filter,            ! (input) scalar string expression
            subdirectorynames, ! (output) a one-dimensional string parameter
            recursive,         ! (optional) default 0
            attributeFilter    ! (optional) default: empty set
            )

Arguments
---------

    *directory*
        A scalar string expression representing the directory you want to
        search. The empty string is interpreted as the current directory.

    *filter*
        The pattern file names should match. The empty string is interpreted as
        all files.

    *subdirectorynames*
        A one-dimensional string parameter indexed over a subset of the
        predeclared set :aimms:set:`Integers`. This parameter will be filled with the names
        of the folders matching the pattern as specified in the first argument.

    *recursive*
        An optional scalar expression. When zero the procedure
        :aimms:func:`DirectoryGetSubdirectories` doesn't work recursively; it scans only
        the directory specified, not its subdirectories. When non-zero, these
        subdirectories will also be searched.

    *attributeFilter*
        files that have one of the specified attributes will not be included in
        the result. This argument is a subset of :aimms:set:`AllFileAttributes`.

Return Value
------------

    The procedure returns the number of subdirectories found on success,
    which may be 0. If it fails, then it returns -1, and the pre-defined
    identifier :aimms:set:`CurrentErrorMessage` will contain a proper error message.

Example
-------

    Using the declarations 

    .. code-block:: aimms

                Set FolderNumbers {
                    SubsetOf    :  Integers;
                    Index       :  fn;
                }

    .. code-block:: aimms

                StringParameter FolderNames {
                   IndexDomain  :  (fn);
                }

    the statements

    .. code-block:: aimms

                DirectoryGetSubdirectories("", "*.*", FolderNames, 
                    recursive: 1, attributeFilter: { 'Executable'} );
                display FolderNames ;

    will result in 

    .. code-block:: aimms

                FolderNames := data { 1 : "backup",  2 : "log" } ;

    to be printed in the listing
    file.

.. note::

    -  The ``directory`` argument can specify either a relative or an
       absolute folder path.

    -  Hidden and system files and subdirectories are not searched, nor are
       devices. On Linux systems, files and subdirectories that start with a
       '.' are considered hidden files and are not searched. The names "."
       and ".." are never included in the result.

.. seealso::

    -  The procedure :aimms:func:`DirectoryGetFiles` to find the names of the files in a
       particular directory.

    -  The procedures :aimms:func:`DirectoryGetCurrent` and :aimms:func:`DirectorySelect` to obtain the current
       directory and to select a particular directory.
