.. aimms:procedure:: DataFileGetComment(datafile, comment)

.. _DataFileGetComment:

DataFileGetComment
==================

The predefined set :aimms:set:`AllDataFiles` (and its subsets :aimms:set:`AllCases` and
:aimms:set:`AllDataSets`), is an integer set. The mapping of these integers onto
the cases and datasets in the project is maintained by the data manager,
and is not editable. With the procedure :aimms:func:`DataFileGetComment` you can
obtain the comment that is specified in the data manager for any element
of the set :aimms:set:`AllDataFiles` (cases or datasets).

.. code-block:: aimms

    DataFileGetComment(
            datafile,     ! (input) element in the set AllDataFiles
            comment       ! (output) scalar string parameter
            )

Arguments
---------

    *datafile*
        An element in the set :aimms:set:`AllDataFiles`.

    *comment*
        A scalar string valued parameter. On return this parameter will contain
        the comment of the datafile. If no comment is specified, then an empty
        string is returned.

Return Value
------------

    The procedure returns 1 if the given datafile still exists, and 0
    otherwise.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

.. seealso::

    The procedures :aimms:func:`DataFileExists`, :aimms:func:`DataFileGetName`.
