.. aimms:procedure:: DataFileGetPath(datafile, path)

.. _DataFileGetPath:

DataFileGetPath
===============

The predefined set :aimms:set:`AllDataFiles` (and its subsets :aimms:set:`AllCases` and
:aimms:set:`AllDataSets`), is an integer set. The mapping of these integers onto
the cases and datasets in the project is maintained by the data manager,
and is not editable. With the procedure :aimms:func:`DataFileGetPath` you can
obtain the path in the data manager for any element of the set
:aimms:set:`AllDataFiles` (cases or datasets). The path of a datafile consists of
a sequence folder names and the name of the datafile itself, separated
by backslash characters.

.. code-block:: aimms

    DataFileGetPath(
            datafile,     ! (input) element in the set AllDataFiles
            path          ! (output) scalar string parameter
            )

Arguments
---------

    *datafile*
        An element in the set :aimms:set:`AllDataFiles`.

    *path*
        A scalar string valued parameter. On return this parameter will contain
        the path of the datafile.

Return Value
------------

    The procedure returns 1 if the given datafile still exists, and 0
    otherwise.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

.. seealso::

    The procedures :aimms:func:`DataFileExists`, :aimms:func:`DataFileGetName`, :aimms:func:`DataFileGetAcronym`.
